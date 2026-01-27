# Day 7 – Mini Project: Log Analyzer

## 📌 Objective
Analyze a security log file to:
- Count failed and successful login attempts
- Detect suspicious IP addresses based on a threshold
- Practice real-world Python scripting concepts

## 🧠 Concepts Used
- sys.argv (command-line arguments)
- File handling
- Dictionaries
- Functions
- Exception handling
- Loops & conditions

## 📂 Log Format
Each line in the log file should be:

IP STATUS

Example:
192.168.1.10 FAILED  
192.168.1.10 FAILED  
192.168.1.12 SUCCESS  

## ▶️ How to Run
```bash
python day7_mini_project.py security.log
