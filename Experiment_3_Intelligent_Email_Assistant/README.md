# Experiment 3 – Intelligent Email Assistant

## Course
**25CS2506 – Building Applications Using GPT-4**

---

## Aim
To generate an appropriate email reply based on the received email and the tone selected by the user.

---

## Problem Statement / Sample Question
A company wants to prepare email replies quickly. Develop a Python program that accepts an incoming email and a preferred tone (Formal, Friendly or Professional). Use Ollama to generate a suitable subject line and email reply, display it, and save it in a text file.

---

## Dataset
No external dataset file is required. The user enters the received email and preferred tone interactively. (See `sample_inputs.txt` for examples).

---

## Prerequisites
1. Python 3.9 or higher.
2. Ollama running locally (`http://localhost:11434`).
3. Model downloaded in Ollama: `llama3.2`
   ```bash
   ollama run llama3.2
   ```
4. `requests` package:
   ```bash
   pip install requests
   ```

---

## Pre-flight Setup & Verification
Before running the experiment, run the setup verification script:
```bash
python setup_check.py
```
This script will:
- Check Python version compatibility.
- Verify that `requests` is installed.
- Ping the Ollama local API at `http://localhost:11434`.
- Check if `llama3.2` model is installed.

---

## Execution
Run the email assistant using either:
```bash
python email_assistant.py
```
or
```bash
python main.py
```
*(On Windows, you can also double-click `run.bat`)*

---

## Sample Interaction

```text
INTELLIGENT EMAIL ASSISTANT
Enter the received email: Please attend the department meeting tomorrow.
Enter tone (Formal/Friendly/Professional): Professional

GENERATED EMAIL REPLY

Subject: Re: Department Meeting Attendance Confirmation

Dear Team,

Thank you for the notification. I confirm that I will attend tomorrow's department meeting.

Best regards,
[Your Name]

Email saved as email_reply.txt
```

---

## Files in This Directory
- `email_assistant.py`: Main experiment code.
- `main.py`: Runner entry point.
- `ollama_helper.py`: Local Ollama API wrapper function.
- `sample_inputs.txt`: Reference test emails and tones.
- `setup_check.py`: Pre-flight environment and dependency checker.
- `requirements.txt`: Python package dependencies.
- `run.bat` / `run.sh`: Automated execution script.
- `README.md`: Experiment documentation.
