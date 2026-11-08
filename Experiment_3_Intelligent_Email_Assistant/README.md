# Experiment 3 – Intelligent Email Assistant

## Aim
To generate an appropriate email reply based on the received email and the tone selected by the user.

---

## Sample Question
A company wants to prepare email replies quickly. Develop a Python program that accepts an incoming email and a preferred tone (Formal, Friendly or Professional). Use Ollama to generate a suitable subject line and email reply, display it, and save it in a text file.

---

## Sample Dataset
No external dataset is required. The user provides the input while running the program.

---

## How to Run
```bash
python email_assistant.py
```

---

## Sample Input / Expected Output
- **Received email:** `Please attend the department meeting tomorrow.`
- **Tone:** `Professional`
- **Output:** The model generates a suitable subject and a polite confirmation reply, then saves it in `email_reply.txt`.

---

## Files in This Folder
- `email_assistant.py` – Python experiment program
- `ollama_helper.py` – Ollama helper module
