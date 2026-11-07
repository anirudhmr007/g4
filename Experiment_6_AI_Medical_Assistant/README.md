# Experiment 6 – AI-Powered Medical Assistant

## Course
**25CS2506 – Building Applications Using GPT-4**

---

## Aim
To develop a simple health information assistant that answers general questions using a predefined information file and Ollama.

---

## Problem Statement / Sample Question
A health information centre wants a basic assistant to answer general health questions from a small information file. Develop a Python program that reads the health information file, accepts a user's question, sends the information and question to Ollama, and displays the response with a medical disclaimer. The assistant must not diagnose diseases or prescribe medicines.

---

## Dataset: `health_info.txt`
```text
Drinking sufficient water helps maintain hydration. Regular exercise supports physical fitness. Fruits and vegetables provide essential nutrients. Adequate sleep supports general wellbeing. Personal hygiene helps prevent infections.
```

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
- Confirm the presence and integrity of `health_info.txt`.

---

## Execution
Run the medical assistant using either:
```bash
python medical_assistant.py
```
or
```bash
python main.py
```
*(On Windows, you can also double-click `run.bat`)*

---

## Sample Interaction

```text
AI-POWERED MEDICAL INFORMATION ASSISTANT

Ask a general health information question.
Type exit to stop.

Enter your question: Why is drinking water important?

Assistant: Drinking sufficient water helps maintain hydration.

Disclaimer: This is general educational information and is not a substitute for professional medical advice.

Enter your question: exit
```

---

## Files in This Directory
- `medical_assistant.py`: Main experiment code.
- `main.py`: Runner entry point.
- `ollama_helper.py`: Local Ollama API wrapper function.
- `health_info.txt`: Sample health information dataset.
- `sample_inputs.txt`: Reference test cases.
- `setup_check.py`: Pre-flight environment and dependency checker.
- `requirements.txt`: Python package dependencies.
- `run.bat` / `run.sh`: Automated execution script.
- `README.md`: Experiment documentation.
