# Smart Document Protection and Tamper Alert System

## 🌟 Project Overview

This project implements an AI-powered system designed to protect critical documents from unauthorized modifications and provide real-time tamper alerts. It leverages file hashing for integrity checks, a file system watcher to detect changes, and an AI-driven anomaly detection model to assess the risk level of detected tampering. Notifications are sent via WhatsApp for immediate awareness.

### Key Features:
* **Digital Fingerprinting:** Uses SHA-256 hashing to create a unique fingerprint for documents.
* **Real-time Monitoring:** Continuously watches specified documents for any modifications or unauthorized copies.
* **AI-Powered Anomaly Detection:** An integrated AI risk scoring mechanism evaluates tampering events based on factors like the number of changes, time of day, and presence of sensitive keywords. This helps differentiate between minor edits and potentially malicious activities.
* **Instant WhatsApp Alerts:** Notifies designated recipients via WhatsApp with details of the tamper event, including specific changes and the calculated AI risk score.
* **Stealth Operation:** The monitoring script can be run silently in the background using a VBScript launcher.

## 💡 The Problem

In today's digital landscape, the integrity of sensitive documents is paramount. Unauthorized alterations to critical files, such as personnel lists, financial records, or legal contracts, can lead to severe consequences, including data breaches, financial losses, and reputational damage. Traditional security measures often fall short in providing immediate detection and comprehensive insights into tampering events.

## 🚀 Our Solution: AI in Action

Our Smart Document Protection and Tamper Alert System addresses these challenges by:

1.  **Establishing a Baseline:** A cryptographic hash of the original document creates an immutable digital fingerprint.
2.  **Continuous Vigilance:** A Python `watchdog` script constantly monitors the document's directory for any file modifications, creations, or deletions.
3.  **Intelligent Anomaly Detection (AI):** When a change is detected:
    * The system compares the current state of the document with its original hash.
    * An AI-driven scoring mechanism (`ai_detect_anomaly` function) calculates a **Risk Score** (0-100%). This score is determined by:
        * **Number of Changes:** More changes generally indicate higher risk.
        * **Time of Event:** Tampering outside normal working hours (e.g., late night/early morning) increases the score.
        * **File Location:** Modifications to unauthorized copies (files outside the designated "safe copy" folder) significantly raise the risk.
        * **Sensitive Keywords:** The presence of keywords like 'bank', 'payment', 'confidential' in changed lines contributes to a higher risk score.
    * This AI component helps prioritize alerts, allowing users to focus on high-risk events. A risk score of 60% or higher triggers a "Highly unusual tampering detected!" warning.
4.  **Actionable Alerts:** Detailed notifications, including the AI risk score and specific line-by-line changes, are sent directly to the administrator's WhatsApp, enabling swift response.

**Example AI Risk Score Scenarios:**
* **0% Risk:** A detected "unauthorized copy" whose content matches the original document's initial pristine state. The AI correctly identifies that while the file might be in an unexpected location, its content hasn't been maliciously altered.
* **30% Risk (as seen in results):** A single line modification during business hours to a file outside the safe folder. The AI considers the single change (low impact) but factors in the unauthorized location.
* **Higher Risk (60%+):** Multiple changes, sensitive keywords, and/or changes occurring outside business hours, particularly in an unauthorized location.

## 🛠️ How to Set Up and Run the Project

### Prerequisites:
* Python 3.x installed on your system.
* Access to a Command Prompt with Administrator privileges (for installing libraries).
* An UltraMsg account (for WhatsApp API) with an Instance ID and Token.
* A WhatsApp number to receive alerts.

### Step 1: Set Up Your Workspace

1.  **Create Project Folder:** On your Desktop, create a folder named `ProtectedDocs`.
2.  **Create Document to Protect:** Inside `ProtectedDocs`, create a Microsoft Word document named `List_of_Freshly_Employed_Personnel_and_Their_Roles.docx`. Populate it with the provided sample content.
    * *Self-correction:* You might want to include a `sample_docs` directory in your GitHub repo with this file, and tell users to copy it to `ProtectedDocs`.

### Step 2: Install Python Libraries

Open **Command Prompt as Administrator** (Search for `cmd`, right-click, `Run as Administrator`) and execute the following commands:

```bash
pip install watchdog scikit-learn python-docx requests
