# Experiment 5 – AI Document Analyzer: Summarize, Query and Export

## Course
**25CS2506 – Building Applications Using GPT-4**

---

## Aim
To read a text document, generate a summary, answer a question based on the document and export the results.

---

## Problem Statement / Sample Question
A college wants a tool to help faculty members analyse text documents. Develop a Python program that reads a text file, displays its contents, generates a summary using Ollama, accepts a question about the document, answers using the document as context, and exports the summary and answer to a text file.

---

## Dataset: `ai.txt`
```text
Artificial Intelligence is a branch of computer science. It enables machines to perform tasks that normally require human intelligence. Applications of AI include healthcare, education, transportation and robotics. Machine learning is a subfield of AI that enables systems to learn patterns from data.
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
- Confirm the presence and integrity of `ai.txt`.

---

## Execution
Run the document analyzer using either:
```bash
python document_analyzer.py
```
or
```bash
python main.py
```
*(On Windows, you can also double-click `run.bat`)*

---

## Sample Interaction

```text
AI DOCUMENT ANALYZER
Enter text file name (example: ai.txt): ai.txt

DOCUMENT CONTENT:

Artificial Intelligence is a branch of computer science. It enables machines to perform tasks that normally require human intelligence. Applications of AI include healthcare, education, transportation and robotics. Machine learning is a subfield of AI that enables systems to learn patterns from data.

DOCUMENT SUMMARY:

Artificial intelligence is a branch of computing that performs tasks typically requiring human intelligence, applied across sectors like healthcare, education, transportation, and robotics, with machine learning serving as a subfield that learns patterns from data.

Enter your question about the document: What are the applications of AI?

ANSWER:

Healthcare, education, transportation and robotics.

Results saved as analysis_result.txt
```

---

## Files in This Directory
- `document_analyzer.py`: Main experiment code.
- `main.py`: Runner entry point.
- `ollama_helper.py`: Local Ollama API wrapper function.
- `ai.txt`: Sample text document dataset.
- `sample_inputs.txt`: Reference test cases.
- `setup_check.py`: Pre-flight environment and dependency checker.
- `requirements.txt`: Python package dependencies.
- `run.bat` / `run.sh`: Automated execution script.
- `README.md`: Experiment documentation.
