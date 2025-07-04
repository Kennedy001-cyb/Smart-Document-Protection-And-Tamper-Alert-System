import time
import hashlib
import datetime
import os
import json
import requests
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from docx import Document

# === CONFIGURATION ===
ORIGINAL_FILE_PATH = r"C:\Users\USER\Desktop\ProtectedDocs\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx"
SAFE_COPY_FOLDER = r"C:\Users\USER\OneDrive\Documents" # Ensure this is correct for your safe location
JSON_LOG_PATH = "tamper_log.json"
USER_ROOT = os.path.expanduser("~")

# === ULTRAMSG WHATSAPP CONFIGURATION ===
ULTRAMSG_INSTANCE_ID = "instance125778"
ULTRAMSG_TOKEN = "0imzmbjiw13ekd3f"
WHATSAPP_RECIPIENT = "2348069715733"

# Global variable to store the *initial* hash of the original file
# This is crucial to detect a restoration to the pristine state.
INITIAL_ORIGINAL_FILE_HASH = None

# === FILE READING FUNCTION ===
def read_file_content(file_path):
    """Read content from .txt or .docx file."""
    _, ext = os.path.splitext(file_path)
    try:
        if ext.lower() == '.txt':
            with open(file_path, "r", encoding="utf-8") as f:
                # Stripping whitespace for consistency with DOCX processing
                return [line.strip() for line in f.readlines()]
        elif ext.lower() == '.docx':
            doc = Document(file_path)
            # Ensure each paragraph text is stripped to remove leading/trailing whitespace
            return [para.text.strip() for para in doc.paragraphs]
    except Exception as e:
        print(f"[ERROR] Cannot read file {file_path}: {e}")
    return []

# === HASH FUNCTION ===
def calculate_hash(file_path):
    """Generate SHA-256 hash of file content."""
    content_lines = read_file_content(file_path)
    content_str = "\n".join(content_lines)
    return hashlib.sha256(content_str.encode("utf-8")).hexdigest() if content_lines else None

# === DIFFERENCE FUNCTION ===
def get_differences(original_lines, new_lines):
    changes = []
    max_len = max(len(original_lines), len(new_lines))
    for i in range(max_len):
        original = original_lines[i] if i < len(original_lines) else ""
        new = new_lines[i] if i < len(new_lines) else ""

        if original != new:
            changes.append({
                "line": i + 1,
                "original_line": original,
                "tampered_line": new
            })
    return changes

# === FOLDER PATH CHECKER ===
def is_within_folder(file_path, folder_path):
    return os.path.abspath(file_path).startswith(os.path.abspath(folder_path))

# === AI ANOMALY DETECTION ===
def ai_detect_anomaly(entry, is_unauthorized_unchanged_copy=False): # Added new parameter
    
    # If it's explicitly an unauthorized copy and its content matches the original (unchanged),
    # then the risk score for its content (changes) is 0, and we explicitly set overall score to 0.
    if is_unauthorized_unchanged_copy:
        return False, 0 # Not unusual, risk score 0 for this specific scenario

    score = 0

    num_changes = len(entry['changes'])
    score += min(num_changes * 10, 40)

    current_utc_time = datetime.datetime.now(datetime.timezone.utc)
    onitsha_offset = datetime.timedelta(hours=1) # WAT is UTC+1
    current_onitsha_time = current_utc_time + onitsha_offset
    
    hour = current_onitsha_time.hour
    if hour < 6 or hour > 22: # Outside 6 AM - 10 PM (22:00)
        score += 20
    elif 18 <= hour <= 22: # Early evening to night (6 PM - 10 PM)
        score += 10

    # This condition *still applies* for files outside the safe copy folder,
    # UNLESS it's the specific case of an "unauthorized unchanged copy" which is handled above.
    if os.path.abspath(entry['file_path']) != os.path.abspath(ORIGINAL_FILE_PATH) and \
       not is_within_folder(entry['file_path'], SAFE_COPY_FOLDER):
        score += 20 # Risk for being in an unauthorized location

    sensitive_keywords = ['bank', 'payment', 'transfer', 'account', 'legal', 'confidential', 'amount', 'signature']
    keyword_hits = sum(
        1 for change in entry['changes'] for keyword in sensitive_keywords
        if re.search(rf"\b{keyword}\b", change['tampered_line'], re.IGNORECASE) or
           re.search(rf"\b{keyword}\b", change['original_line'], re.IGNORECASE)
    )
    score += min(keyword_hits * 10, 20)

    score = max(0, min(score, 100)) # Ensure score is between 0 and 100
    return score >= 60, score

# === LOGGING FUNCTION ===
def log_event_json(file_path, reason, changes=None, is_restored=False, is_unauthorized_unchanged_copy=False):
    now = datetime.datetime.now().isoformat()
    entry = {
        "timestamp": now,
        "event": reason,
        "file_path": file_path,
        "changes": changes or []
    }

    logs = []
    if os.path.exists(JSON_LOG_PATH):
        try:
            with open(JSON_LOG_PATH, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append(entry)
    with open(JSON_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

    print(f"[{now}] 🚨 {reason} at: {file_path}")

    # Determine risk score based on flags
    if is_restored:
        is_unusual, risk_score = False, 0 # Explicitly set score to 0 for original file restoration
        print(f"AI Analysis: File restored. Risk Score: {risk_score}%")
    else:
        # Pass the flag to ai_detect_anomaly for specific override logic
        is_unusual, risk_score = ai_detect_anomaly(entry, is_unauthorized_unchanged_copy=is_unauthorized_unchanged_copy)
        print(f"{'⚠ AI WARNING: Highly unusual tampering detected!' if is_unusual else 'AI Analysis: Low risk'} Risk Score: {risk_score}%")
    
    send_whatsapp_log(entry, risk_score, is_restored, is_unauthorized_unchanged_copy)

# === WHATSAPP NOTIFICATION ===
def send_whatsapp_log(entry, risk_score, is_restored=False, is_unauthorized_unchanged_copy=False):
    try:
        if is_restored:
            message = f"✅ File Restored ✅\n\nTime: {entry['timestamp']}\nFile: {entry['file_path']}\n\nAI Risk Score: {risk_score}%"
        elif is_unauthorized_unchanged_copy:
            # Customized message for 0% risk unauthorized unchanged copies
            message = f"✅ Unauthorized Copy Detected (Content Restored) ✅\n\nTime: {entry['timestamp']}\nFile: {entry['file_path']}\n\nNote: File content matches original. Risk score is 0% as content is no longer tampered.\n\nAI Risk Score: {risk_score}%"
        else:
            message = f"🚨 Tamper Detected 🚨\n\nTime: {entry['timestamp']}\nEvent: {entry['event']}\nFile: {entry['file_path']}"
            
            MAX_CHANGES_FOR_WHATSAPP = 5
            
            if entry['changes']:
                num_total_changes = len(entry['changes'])
                changes_to_report = entry['changes'][:MAX_CHANGES_FOR_WHATSAPP]
                
                for change in changes_to_report:
                    if not change['original_line'] and change['tampered_line']:
                        message += f"\n\nLine {change['line']} (ADDED):\n- NEW: {change['tampered_line']}"
                    elif change['original_line'] and not change['tampered_line']:
                        message += f"\n\nLine {change['line']} (DELETED):\n- OLD: {change['original_line']}"
                    else: # Modified
                        message += f"\n\nLine {change['line']} (MODIFIED):\n- OLD: {change['original_line']}\n- NEW: {change['tampered_line']}"
                
                if num_total_changes > MAX_CHANGES_FOR_WHATSAPP:
                    message += f"\n\n...and {num_total_changes - MAX_CHANGES_FOR_WHATSAPP} more changes. Check '{JSON_LOG_PATH}' for full details."

            message += f"\n\nAI Risk Score: {risk_score}%"

        url = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"
        payload = {
            "token": ULTRAMSG_TOKEN,
            "to": WHATSAPP_RECIPIENT,
            "body": message
        }
        response = requests.post(url, data=payload)
        print(f"[WhatsApp] Sent: {response.json()}")
    except Exception as e:
        print(f"[WhatsApp ERROR] {e}")

# === FILE MONITORING CLASS ===
class ChangeHandler(FileSystemEventHandler):
    def __init__(self, original_hash, original_lines):
        super().__init__()
        self.original_hash = original_hash # This represents the last known hash of the ORIGINAL_FILE_PATH
        self.original_lines = original_lines # This represents the last known lines of the ORIGINAL_FILE_PATH

    def on_modified(self, event):
        if not event.is_directory:
            self.process(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.process(event.src_path)

    def process(self, filepath):
        filepath = os.path.abspath(filepath)
        allowed_files = (os.path.basename(ORIGINAL_FILE_PATH).lower(), "contract.txt", "contract.docx")

        if not filepath.lower().endswith(allowed_files):
            return

        current_hash = calculate_hash(filepath)
        if not current_hash:
            print(f"[ERROR] Cannot hash file: {filepath}")
            return

        if filepath == os.path.abspath(ORIGINAL_FILE_PATH):
            if current_hash != self.original_hash: # Original file has been modified
                new_lines = read_file_content(filepath)
                changes = get_differences(self.original_lines, new_lines)
                
                if current_hash == INITIAL_ORIGINAL_FILE_HASH:
                    # Original file has been restored to its initial pristine state
                    log_event_json(filepath, "Original file restored to initial state!", [], is_restored=True)
                else:
                    # Original file has been modified (not restored to initial)
                    log_event_json(filepath, "Original file was modified!", changes)
                
                # Update the stored hash and lines to the current state of the original file
                self.original_hash = current_hash
                self.original_lines = new_lines
        else:
            # Handling copied/other files
            new_lines_of_other_file = read_file_content(filepath)
            
            # Compare the copied file's content to the *current* original file's content
            changes = get_differences(self.original_lines, new_lines_of_other_file)
            
            if is_within_folder(filepath, SAFE_COPY_FOLDER):
                # File is in safe folder, but was modified (or created with changes)
                log_event_json(filepath, "Modified file in safe folder", changes)
            else:
                # File is outside safe folder
                # Check if content matches INITIAL_ORIGINAL_FILE_HASH to flag for 0% risk
                if current_hash == INITIAL_ORIGINAL_FILE_HASH:
                    log_event_json(filepath, "Unauthorized copy of file found (content matches original)", [], is_unauthorized_unchanged_copy=True)
                elif not changes:
                    # This case handles an unchanged unauthorized copy whose content DOES NOT match initial,
                    # but also hasn't changed relative to the *current* original.
                    # It will still get the 20% location risk from ai_detect_anomaly.
                    log_event_json(filepath, "Unauthorized copy of file found (unchanged relative to current original)", [], is_unauthorized_unchanged_copy=True)
                else:
                    # Case: Unauthorized copy, and its content is also different from the original
                    log_event_json(filepath, "Tampered copy found outside safe folder", changes)

# === MONITORING FUNCTION ===
def monitor_file():
    global INITIAL_ORIGINAL_FILE_HASH

    original_hash_on_start = calculate_hash(ORIGINAL_FILE_PATH)
    original_lines_on_start = read_file_content(ORIGINAL_FILE_PATH)

    if not original_hash_on_start:
        print("[ERROR] Cannot read original file at startup. Please ensure the file exists and is accessible.")
        return

    INITIAL_ORIGINAL_FILE_HASH = original_hash_on_start # Store the hash of the file at program start

    event_handler = ChangeHandler(original_hash_on_start, original_lines_on_start)
    observer = Observer()
    observer.schedule(event_handler, path=USER_ROOT, recursive=True)
    observer.start()

    print("[SECURITY] Monitoring started... Press Ctrl+C to stop.\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# === RUN PROGRAM ===
if __name__ == "__main__":
    monitor_file()