# FILE-INTEGRITY-CHECKER

COMPANY: CODTECH IT SOLUTIONS

NAME: SRI SUJEETH SIRIVELLA

INTERN ID: CT04DN1954

DOMAIN: CYBER SECUTITY & ETHICAL HACKING.

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

TASK DESCRIPTION: File Integrity Checker


### Objective


The purpose of this project is to build a File Integrity Checker using Python. The tool is designed to monitor and ensure the integrity of files within a specific directory by calculating, storing, and comparing their hash values. This is crucial for maintaining data authenticity, especially in systems where file tampering or data corruption can have severe consequences, such as in cybersecurity, financial systems, health records, or secure communications.


### Introduction


File integrity is a vital aspect of modern computing systems. Whether it's a small organization managing sensitive customer data or a large enterprise with confidential information, ensuring that files have not been altered without authorization is critical. Any unexpected changes can be a sign of corruption, unauthorized access, or even a cyberattack. The proposed tool solves this problem by detecting any changes—additions, deletions, or modifications—in files within a monitored folder.


### Working Principle


The File Integrity Checker uses cryptographic hash functions, specifically the SHA-256 algorithm, provided by Python’s built-in hashlib library. A hash function converts data into a fixed-size string of characters, which is unique to the original data. If even a single character in the file is changed, the resulting hash will be entirely different. This makes hash functions a reliable way to detect any changes in file content.

### The tool works in two primary phases:

#### Hash Generation and Storage:

When the script is run for the first time, it recursively scans all files in the target directory, calculates their SHA-256 hash values, and stores them in a JSON file called hashes.json.

#### Comparison and Integrity Check:

On subsequent runs, the script again calculates the current hashes and compares them with the saved ones. If differences are found, the tool identifies whether a file has been added, modified, or deleted and prints a report to the user.

### Technical Breakdown


#### Directory Scanning:

The script uses the os.walk() function to traverse through all subdirectories and files in the specified monitoring folder.

#### Hash Calculation:

Each file’s contents are read in binary mode and passed through the SHA-256 hashing algorithm. The resulting hash string represents a digital fingerprint of the file.

#### Data Storage and Retrieval:
Hashes are stored in a dictionary and then serialized into a JSON file (hashes.json) using Python’s json module. This acts as a historical snapshot of file states.

#### Comparison Logic:
The script compares old and new hash dictionaries to detect:

Changed files (file exists but hash differs)

Added files (present in current scan but not in saved snapshot)

Deleted files (present in saved snapshot but missing in current scan)

User Feedback:
A summary of detected changes is displayed, giving clear alerts about the type and name of files affected.

### Use Cases and Benefits


#### System Security:
Detecting unauthorized file changes can help in identifying potential breaches or malware activity.

#### Data Backup Verification:
Ensure that backup files haven’t been tampered with or corrupted over time.

#### Compliance Monitoring:
For systems where file immutability is mandated (e.g., in finance or healthcare), this tool provides a simple and effective auditing mechanism.

#### Educational Use:
It introduces students and beginners to concepts like hashing, data integrity, and basic cybersecurity practices.

### Customization and Scalability


The current script is modular and easy to customize. For example:

You can change the hashing algorithm from SHA-256 to MD5 or SHA-512 by modifying just one line.

You can enhance it with a GUI using tkinter or PyQt.

Add real-time monitoring using a file event library like watchdog.

Schedule periodic scans using cron (Linux) or Task Scheduler (Windows).

### Conclusion

This File Integrity Checker is a practical and educational tool that serves the critical function of verifying file authenticity. By leveraging Python’s simplicity and powerful libraries, it provides a lightweight yet effective solution to monitor file changes. It can be extended into a full-fledged integrity monitoring system suitable for personal, academic, or professional environments. In a world where data breaches and file tampering are becoming increasingly common, tools like these are essential for ensuring digital trust and integrity.

