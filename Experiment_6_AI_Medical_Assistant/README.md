# Experiment 6 – AI-Powered Medical Assistant

## Aim
To develop a simple health information assistant that answers general questions using a predefined information file and Ollama.

---

## Sample Question
A health information centre wants a basic assistant to answer general health questions from a small information file. Develop a Python program that reads the health information file, accepts a user's question, sends the information and question to Ollama, and displays the response with a medical disclaimer. The assistant must not diagnose diseases or prescribe medicines.

---

## Sample Dataset: `health_info.txt`
Create a file named `health_info.txt` with the following content:
```text
Drinking sufficient water helps maintain hydration. Regular exercise supports physical fitness. Fruits and vegetables provide essential nutrients. Adequate sleep supports general wellbeing. Personal hygiene helps prevent infections.
```

---

## How to Run
```bash
python medical_assistant.py
```

---

## Sample Input / Expected Output
- **Question:** `Why is drinking water important?`
- **Expected response:** `Drinking sufficient water helps maintain hydration.` The application also displays the medical disclaimer.

---

## Files in This Folder
- `medical_assistant.py` – Python experiment program
- `health_info.txt` – Sample health information dataset
- `ollama_helper.py` – Ollama helper module
