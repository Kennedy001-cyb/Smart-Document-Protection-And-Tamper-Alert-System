# Smart Document Protection and Tamper Alert System

This project implements a robust system to protect critical documents from unauthorized modifications and alert you instantly to any detected tampering. Leveraging Python's `watchdog` library for real-time file monitoring and a custom AI-driven anomaly detection model, it provides a crucial layer of security for sensitive information. The system also integrates with UltraMsg to send instant WhatsApp notifications for critical events, ensuring you're always informed, even when the monitoring script runs silently in the background.

---

## 🌟 Features

* **Real-time File Monitoring:** Continuously watches specified documents for any changes (modifications, creations).
* **Hash-based Tamper Detection:** Generates and compares SHA-256 hashes of document content to detect unauthorized alterations.
* **Content Difference Reporting:** Pinpoints the exact lines that have been added, deleted, or modified in a tampered document.
* **AI-Powered Anomaly Detection:** An integrated AI model assesses the **risk score** of detected changes based on factors like:
    * **Number of changes:** More changes generally lead to a higher risk.
    * **Time of modification:** Modifications outside of regular working hours (e.g., 6 AM - 10 PM WAT) increase the risk.
    * **Location of the file:** Files found outside the designated "safe copy" folder pose a higher risk.
    * **Sensitive Keywords:** The presence of predefined sensitive keywords (e.g., 'bank', 'confidential', 'legal') in changed lines contributes to the risk score.
    * **The AI Risk Score (0-100%)** helps differentiate between minor, legitimate changes and potentially malicious tampering, providing a clear indication of the severity. A score of 60% or higher is flagged as "highly unusual tampering."
* **WhatsApp Alerts:** Sends immediate notifications to a designated WhatsApp number via UltraMsg when tampering is detected or a document is restored.
* **Detailed Event Logging:** Maintains a JSON log of all detected events, including timestamps, file paths, and specific content changes.
* **Silent Background Operation:** Can be launched invisibly using a VBScript, allowing the monitoring to run discreetly without a command prompt window.
* **Automatic Restoration Detection:** Identifies when a tampered document has been restored to its original, pristine state, reducing the risk score to 0%.

---

## 🛠️ Setup and Installation

Follow these steps to set up the Smart Document Protection and Tamper Alert System on your machine.

### Step 1: Set Up Your Workspace

1.  **Create a folder** on your Desktop named `ProtectedDocs`.
2.  **Inside `ProtectedDocs`**, create a new Word document.
    * Name it: `List_of_Freshly_Employed_Personnel_and_Their_Roles.docx`
    * Paste the following content into it:

    ```
    List of Freshly Employed Personnel and Their Roles

    ---

    1. Administration & HR Department


    2. Aisha Gambo – HR Generalist: Manages employee relations, benefits administration, and HR policies.


    3. Chris Okoro – Office Administrator: Oversees office supplies, vendor relations, and front desk operations.


    4. Fatima Abubakar – Talent Acquisition Specialist: Focuses on sourcing, interviewing, and recruiting new hires.


    5. Emmanuel Okafor – HRIS Analyst: Manages HR information systems and ensures data integrity.


    6. Grace Olatunji – Executive Assistant: Provides high-level administrative support to senior management.


    7. Finance & Accounting Department


    8. Kwame Nkrumah – Senior Accountant: Responsible for financial reporting, budget management, and compliance.


    9. Blessing Chukwu – Treasury Analyst: Manages cash flow, investments, and banking relationships.


    10. David Ayodele – Cost Accountant: Analyzes production costs and provides insights for cost control.


    11. Sandra Imade – Tax Specialist: Prepares and files tax returns, ensuring compliance with tax laws.


    12. Tunde Bakare – Financial Controller: Oversees all accounting operations, internal controls, and audits.


    13. IT & Technical Support


    14. Zara Bello – Cybersecurity Analyst: Monitors systems for security breaches, investigates incidents, and implements security measures.


    15. Kunle Adeniyi – Cloud Engineer: Designs, deploys, and manages cloud-based infrastructure and services.


    16. Ngozi Okafor – UI/UX Designer: Focuses on user interface and user experience design for software applications.


    17. Precious Adeyemi – Database Administrator: Manages and maintains organizational databases, ensuring data availability and security.


    18. Felix Osei – DevOps Engineer: Bridges the gap between development and operations, streamlining software deployment.


    19. Operations Department


    20. Daniel Obi – Logistics Manager: Oversees supply chain, warehousing, and distribution activities.


    21. Maryam Ali – Process Improvement Specialist: Identifies inefficiencies in workflows and implements solutions.


    22. Chukwudi Eze – Production Supervisor: Manages daily production schedules, quality control, and team performance.


    23. Bolanle Fasina – Inventory Control Manager: Responsible for optimizing inventory levels and accuracy.


    24. Ibrahim Mohammed – Supply Chain Coordinator: Liaises with suppliers and internal teams to ensure smooth material flow.


    25. Marketing & Communications


    26. Amara Okoro – Digital Marketing Specialist: Develops and executes online marketing strategies, including SEO, SEM, and email campaigns.


    27. Segun Ojo – Brand Manager: Responsible for brand identity, messaging, and market positioning.


    28. Jessica Nduka – Content Marketing Manager: Oversees the creation and distribution of valuable content to attract and retain customers.


    29. Kelechi Duru – Event Coordinator: Plans and executes company events, webinars, and conferences.


    30. Linda Eke – Public Relations Manager: Manages the company's public image, media relations, and crisis communications.


    31. Sales Department


    32. Femi Adekunle – Key Account Manager: Manages relationships with major clients and drives strategic sales initiatives.


    33. Chioma Obasi – Sales Operations Analyst: Supports the sales team with data analysis, reporting, and process optimization.


    34. Kenneth Idoko – Inside Sales Representative: Handles sales remotely, often through phone calls and emails.


    35. Hadiza Bello – Channel Sales Manager: Develops and manages sales through partner channels.


    36. Johnpaul Onwuka – Sales Trainer: Develops and delivers training programs to enhance the sales team's skills.


    37. Customer Service Department


    38. Blessing Musa – Customer Experience Specialist: Focuses on improving the overall customer journey and satisfaction.


    39. Michael Udoh – Support Team Lead: Supervises and guides a team of customer service representatives.


    40. Ugochi Ezeala – Escalation Specialist: Handles complex customer issues and resolves elevated complaints.


    41. Sarah Adamu – Live Chat Agent: Provides real-time support to customers through online chat platforms.


    42. David Akpan – Customer Feedback Analyst: Collects, analyzes, and reports on customer feedback to identify areas for improvement.


    43. Legal & Compliance


    44. Chiamaka Eze – Corporate Counsel: Provides legal advice on corporate governance, contracts, and regulatory matters.


    45. Jide Obi – Compliance Officer: Ensures the company adheres to all relevant laws, regulations, and internal policies.


    46. Funke Olawale – Intellectual Property Lawyer: Manages patents, trademarks, and copyrights.


    47. Emeka Nwosu – Regulatory Affairs Specialist: Liaises with government agencies and ensures compliance with industry-specific regulations.


    48. Toluwani Akinola – Data Protection Officer: Oversees data privacy and ensures compliance with data protection laws (e.g., GDPR, NDPR).


    49. Research & Development


    50. Dr. Nnamdi Eke – Lead Research Scientist: Heads research projects and drives scientific innovation.


    51. Aminu Ibrahim – Product Development Engineer: Designs and develops new products or improves existing ones.


    52. Gloria Effiong – Research Assistant: Supports research activities, data collection, and experimental procedures.


    53. Abdulrahman Sani – Innovation Manager: Fosters a culture of innovation and manages the ideation pipeline.


    54. Chioma Nwachukwu – UX Researcher: Conducts research to understand user needs and behaviors for product design.


    55. Facilities & Maintenance


    56. James Adebayo – Safety Officer: Ensures workplace safety, conducts risk assessments, and manages emergency procedures.


    57. Esther Okon – Facilities Coordinator: Manages space planning, office moves, and maintenance schedules.


    58. Godwin Nnaji – HVAC Technician: Installs, maintains, and repairs heating, ventilation, and air conditioning systems.


    59. Patience Ekejiuba – Grounds Supervisor: Oversees the maintenance and landscaping of company grounds.


    60. Musa Danjuma – Building Maintenance Technician: Performs general repairs and maintenance tasks around the facility.
    ```

### Step 2: Install Python and Libraries

1.  **Open Command Prompt as Administrator:**
    * Press the `Windows` key, type `cmd`.
    * Right-click on "Command Prompt" and select "Run as Administrator."
2.  **Install Python Libraries:** Type the following commands one by one and press Enter:
    ```bash
    pip install watchdog
    pip install python-docx
    pip install requests
    ```
    These libraries are essential for file monitoring, reading Word documents, and sending WhatsApp notifications.

### Step 3: Write Hashing Code (`save_hash.py`)

This script creates a "digital fingerprint" (hash) of your original document. If the document is ever changed, this fingerprint will no longer match, indicating tampering.

1.  **Open Notepad.**
2.  **Paste the following Python code:**

    ```python
    import hashlib
    import os

    def generate_hash(file_path):
        with open(file_path, "rb") as f:
            content = f.read()
        return hashlib.sha256(content).hexdigest()

    # IMPORTANT: Update this path to your document's actual location
    file_path = r"C:\Users\USER\Desktop\ProtectedDocs\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx"

    # Ensure the directory for hash.txt exists before trying to write to it
    hash_file_dir = os.path.dirname(file_path)
    if not os.path.exists(hash_file_dir):
        os.makedirs(hash_file_dir)

    original_hash = generate_hash(file_path)

    # Save the hash in a .txt file, not .docx
    with open(os.path.join(hash_file_dir, "hash.txt"), "w") as h:
        h.write(original_hash)

    print("Original file hash saved.")
    ```

3.  **Save** this file as `save_hash.py` inside your `ProtectedDocs` folder.
4.  **Run it from a normal Command Prompt** (not as Admin):
    ```bash
    cd C:\Users\USER\Desktop\ProtectedDocs
    python save_hash.py
    ```
    *(Remember to replace `C:\Users\USER\` with your actual user path.)*

    This will create a `hash.txt` file in your `ProtectedDocs` folder, storing the original document's fingerprint.

### Step 4: Monitor File for Changes (`watcher.py`)

This is the core script that continuously monitors your document and triggers alerts.

1.  **Open Notepad.**
2.  **Paste the following Python code:**

    ```python
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
    # Update this path to your document's actual location
    ORIGINAL_FILE_PATH = r"C:\Users\USER\Desktop\ProtectedDocs\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx"
    # Update this path to a safe, trusted location for authorized copies
    SAFE_COPY_FOLDER = r"C:\Users\USER\Documents"
    JSON_LOG_PATH = "tamper_log.json"
    USER_ROOT = os.path.expanduser("~")

    # === ULTRAMSG WHATSAPP CONFIGURATION ===
    # Obtain your Instance ID and Token from UltraMsg.com
    ULTRAMSG_INSTANCE_ID = "instance125778" # REPLACE WITH YOUR INSTANCE ID
    ULTRAMSG_TOKEN = "0imzmbjiw13ekd3f"     # REPLACE WITH YOUR TOKEN
    WHATSAPP_RECIPIENT = "2348069715733" # REPLACE WITH YOUR WHATSAPP NUMBER (with country code, no +)

    # Global variable to store the initial hash of the original file
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
        """Compares two lists of lines and returns detected changes."""
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
        """Checks if a file path is within a specified folder."""
        return os.path.abspath(file_path).startswith(os.path.abspath(folder_path))

    # === AI ANOMALY DETECTION ===
    def ai_detect_anomaly(entry, is_unauthorized_unchanged_copy=False):
        """
        Calculates a risk score for a detected event based on various factors.
        Returns (is_unusual_tampering, risk_score).
        """
        # If it's explicitly an unauthorized copy and its content matches the original (unchanged),
        # then the risk score for its content (changes) is 0, and we explicitly set overall score to 0.
        if is_unauthorized_unchanged_copy:
            return False, 0 # Not unusual, risk score 0 for this specific scenario

        score = 0

        # Factor 1: Number of changes
        num_changes = len(entry['changes'])
        score += min(num_changes * 10, 40) # Max 40 points for changes

        # Factor 2: Time of day (Onitsha, WAT is UTC+1)
        current_utc_time = datetime.datetime.now(datetime.timezone.utc)
        onitsha_offset = datetime.timedelta(hours=1)
        current_onitsha_time = current_utc_time + onitsha_offset

        hour = current_onitsha_time.hour
        if hour < 6 or hour > 22: # Outside 6 AM - 10 PM (22:00)
            score += 20
        elif 18 <= hour <= 22: # Early evening to night (6 PM - 10 PM)
            score += 10

        # Factor 3: File location (outside safe folder)
        # This condition still applies for files outside the safe copy folder,
        # UNLESS it's the specific case of an "unauthorized unchanged copy" which is handled above.
        if os.path.abspath(entry['file_path']) != os.path.abspath(ORIGINAL_FILE_PATH) and \
           not is_within_folder(entry['file_path'], SAFE_COPY_FOLDER):
            score += 20 # Risk for being in an unauthorized location

        # Factor 4: Sensitive keywords in changes
        sensitive_keywords = ['bank', 'payment', 'transfer', 'account', 'legal', 'confidential', 'amount', 'signature', 'salary', 'personal data']
        keyword_hits = sum(
            1 for change in entry['changes'] for keyword in sensitive_keywords
            if re.search(rf"\b{keyword}\b", change['tampered_line'], re.IGNORECASE) or
               re.search(rf"\b{keyword}\b", change['original_line'], re.IGNORECASE)
        )
        score += min(keyword_hits * 10, 20) # Max 20 points for sensitive keywords

        score = max(0, min(score, 100)) # Ensure score is between 0 and 100
        return score >= 60, score # Flag as unusual if score is 60 or higher

    # === LOGGING FUNCTION ===
    def log_event_json(file_path, reason, changes=None, is_restored=False, is_unauthorized_unchanged_copy=False):
        """Logs the event to a JSON file and prints to console."""
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
                logs = [] # Handle empty or corrupt JSON file

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
        """Sends a WhatsApp notification via UltraMsg."""
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

            url = f"[https://api.ultramsg.com/](https://api.ultramsg.com/){ULTRAMSG_INSTANCE_ID}/messages/chat"
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
            self.original_hash = original_hash  # This represents the last known hash of the ORIGINAL_FILE_PATH
            self.original_lines = original_lines # This represents the last known lines of the ORIGINAL_FILE_PATH

        def on_modified(self, event):
            if not event.is_directory:
                self.process(event.src_path)

        def on_created(self, event):
            if not event.is_directory:
                self.process(event.src_path)

        def process(self, filepath):
            filepath = os.path.abspath(filepath)
            # Monitor only the primary document and "contract" files (if added)
            # Add other specific files you want to monitor here if needed
            allowed_file_names = [os.path.basename(ORIGINAL_FILE_PATH).lower(), "contract.txt", "contract.docx"]

            # Only process if the file name matches one of the allowed names
            if os.path.basename(filepath).lower() not in allowed_file_names:
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
                # Handling copied/other files (e.g., "contract.txt" or "contract.docx" if they exist)
                new_lines_of_other_file = read_file_content(filepath)

                # Compare the copied file's content to the current original file's content
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
                        # but also hasn't changed relative to the current original.
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
        # Monitor the user's root directory recursively for comprehensive detection
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
    ```

3.  **Save** this file as `watcher.py` inside your `ProtectedDocs` folder.

---

## 🚀 How to Run and Simulate Tampering

### 1. Start the Monitoring Script

Navigate to your `ProtectedDocs` folder in Command Prompt:

```bash
cd C:\Users\USER\Desktop\ProtectedDocs
Then, run the watcher script:

Bash

python watcher.py
(Remember to replace C:\Users\USER\ with your actual user path.)

You will see "[SECURITY] Monitoring started..." in your terminal.

2. Simulate Tampering
While watcher.py is running:

Open List_of_Freshly_Employed_Personnel_and_Their_Roles.docx.
Make a change, for example, change "Chris Okoro" to "Iloduba Johnkennedy".
Save and close the document.
3. Observe the Output
Terminal Output: Your command prompt will immediately show "Tampering detected!"
WhatsApp Alert: You will receive a WhatsApp message on the number configured in watcher.py detailing the detected changes and the AI risk score.
Log File: A tamper_log.json file will be created/updated in your ProtectedDocs folder, containing a detailed record of the event.
👻 Hiding the Script (Silent Operation)
To keep the watcher.py script running invisibly in the background, you can use a VBScript launcher.

Steps to Use VBScript Launcher
Open Notepad.

Paste this VBScript:

VB.Net

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c python C:\Users\USER\Desktop\ProtectedDocs\watcher.py", 0
Set WshShell = Nothing
(IMPORTANT: Update the Python script path C:\Users\USER\Desktop\ProtectedDocs\watcher.py to your exact file location.)

Save this file as RunWatcher.vbs inside your ProtectedDocs folder.

Double-click RunWatcher.vbs. The Python watcher will start invisibly without opening a command prompt window.

This method works assuming Python is installed and properly added to your system's PATH environment variable.

How to Stop the VBScript-Launched Watcher
Since the VBScript runs the Python process invisibly, you'll need to stop it manually:

Open Task Manager (Press Ctrl + Shift + Esc).
Go to the "Details" tab (or "Processes" tab on older Windows versions).
Look for Python.exe in the list.
Select it, right-click, and choose "End task".
This action will fully stop the invisible monitoring script.

📈 AI Risk Score Explained
The AI Risk Score is a crucial component of this system, providing a quantitative measure of the potential threat posed by a detected change. The score is calculated on a scale of 0% to 100%, with higher percentages indicating greater suspicion.

Low Risk (0-59%): Typically indicates minor changes, or authorized copies that have been restored to their original state. An "Unauthorized Copy Detected (Content Restored)" event will have a 0% risk, even if the file is outside the safe folder, because its content is no longer tampered.
High Risk (60-100%): Signals potentially unusual or malicious tampering. These events trigger a "⚠ AI WARNING: Highly unusual tampering detected!" message in the console and WhatsApp.
The AI considers:

Volume of Changes: Numerous alterations instantly raise the score.
Time of Day: Modifications during unusual hours (late night, early morning) increase suspicion.
File Location: Changes to files outside designated "safe" locations are viewed with higher risk.
Sensitive Content: If the changes involve keywords related to financial, legal, or confidential information, the risk escalates significantly.
This intelligent scoring helps prioritize alerts, allowing you to focus on the most critical security incidents.

🎯 Example Results
Here are examples of how the system responds to different scenarios:

Scenario 1: Tampering Detected
When "Chris Okoro" was changed to "Iloduba Johnkennedy":

🚨 Tamper Detected 🚨

Time: 2025-06-18T10:26:20.376207
Event: Tampered copy found outside safe folder
File: C:\Users\USER\Documents\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx

Line 5 (MODIFIED):

OLD: Chris Okoro – Office Administrator: Oversees office supplies, vendor relations, and front desk operations.

NEW: Iloduba Johnkennedy – Office Administrator: Oversees office supplies, vendor relations, and front desk operations.

AI Risk Score: 30%
Scenario 2: Document Restored
When the tampered document was restored to its original state:

✅ Unauthorized Copy Detected (Content Restored) ✅

Time: 2025-06-18T10:27:57.282039
File: C:\Users\USER\Documents\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx

Note: File content matches original. Risk score is 0% as content is no longer tampered.

AI Risk Score: 0%
Scenario 3: Activity Log (tamper_log.json)
The tamper_log.json file provides a comprehensive history of events:

JSON


NB: Always be sensitive about the pathways you are  using.

[
    {
        "timestamp": "2025-06-18T10:26:20.376207",
        "event": "Tampered copy found outside safe folder",
        "file_path": "C:\\Users\\USER\\Documents\\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx",
        "changes": [
            {
                "line": 5,
                "original_line": "Chris Okoro – Office Administrator: Oversees office supplies, vendor relations, and front desk operations.",
                "tampered_line": "Iloduba Johnkennedy – Office Administrator: Oversees office supplies, vendor relations, and front desk operations."
            }
        ]
    },
    {
        "timestamp": "2025-06-18T10:26:22.134284",
        "event": "Tampered copy found outside safe folder",
        "file_path": "C:\\Users\\USER\\Documents\\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx",
        "changes": [
            {
                "line": 5,
                "original_line": "Chris Okoro – Office Administrator: Oversees office supplies, vendor relations, and front desk operations.",
                "tampered_line": "Iloduba Johnkennedy – Office Administrator: Oversees office supplies, vendor relations, and front desk operations."
            }
        ]
    },
    {
        "timestamp": "2025-06-18T10:27:57.282039",
        "event": "Unauthorized copy of file found (content matches original)",
        "file_path": "C:\\Users\\USER\\Documents\\List_of_Freshly_Employed_Personnel_and_Their_Roles.docx",
        "changes": []
    }
]
