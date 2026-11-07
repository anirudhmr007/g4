# Experiment 2 – AI-Powered Blog Content Generator

## Course
**25CS2506 – Building Applications Using GPT-4**

---

## Aim
To generate blog content using a topic and writing style supplied by the user.

---

## Problem Statement / Sample Question
An educational website needs a simple blog generator. Develop a Python program that accepts a blog topic and writing style, generates a suitable title and blog content using Ollama, displays the result, and saves it in a text file.

---

## Dataset
No external dataset file is required. The user provides inputs interactively when running the program. (See `sample_inputs.txt` for example inputs).

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
Run the blog generator using either:
```bash
python blog_generator.py
```
or
```bash
python main.py
```
*(On Windows, you can also double-click `run.bat`)*

---

## Sample Interaction

```text
AI BLOG CONTENT GENERATOR
Enter blog topic: Benefits of Artificial Intelligence
Enter writing style (Formal/Casual/Informative): Informative

GENERATED BLOG

# Unlocking Tomorrow: The Transformative Benefits of Artificial Intelligence

## Introduction
Artificial Intelligence (AI) has rapidly transitioned from science fiction into an indispensable driver of modern innovation...

## Main Content
...

## Conclusion
...

Blog saved as blog.txt
```

---

## Files in This Directory
- `blog_generator.py`: Main experiment code.
- `main.py`: Runner entry point.
- `ollama_helper.py`: Local Ollama API wrapper function.
- `sample_inputs.txt`: Reference test topics and styles.
- `setup_check.py`: Pre-flight environment and dependency checker.
- `requirements.txt`: Python package dependencies.
- `run.bat` / `run.sh`: Automated execution script.
- `README.md`: Experiment documentation.
