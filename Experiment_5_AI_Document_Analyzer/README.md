# Experiment 5 – AI Document Analyzer: Summarize, Query and Export

## Aim
To read a text document, generate a summary, answer a question based on the document and export the results.

---

## Sample Question
A college wants a tool to help faculty members analyse text documents. Develop a Python program that reads a text file, displays its contents, generates a summary using Ollama, accepts a question about the document, answers using the document as context, and exports the summary and answer to a text file.

---

## Sample Dataset: `ai.txt`
Create a file named `ai.txt` with the following content:
```text
Artificial Intelligence is a branch of computer science. It enables machines to perform tasks that normally require human intelligence. Applications of AI include healthcare, education, transportation and robotics. Machine learning is a subfield of AI that enables systems to learn patterns from data.
```

---

## How to Run
```bash
python document_analyzer.py
```

---

## Sample Input / Expected Output
- **File name:** `ai.txt`
- **Question:** `What are the applications of AI?`
- **Expected answer:** `Healthcare, education, transportation and robotics.`
- **Result:** Summary, question, and answer are saved to `analysis_result.txt`.

---

## Files in This Folder
- `document_analyzer.py` – Python experiment program
- `ai.txt` – Sample text document
- `ollama_helper.py` – Ollama helper module
