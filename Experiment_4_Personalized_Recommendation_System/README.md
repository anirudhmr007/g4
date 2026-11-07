# Experiment 4 – Personalized Recommendation System

## Course
**25CS2506 – Building Applications Using GPT-4**

---

## Aim
To recommend courses based on a student's interests and skill level using a predefined course catalogue and Ollama.

---

## Problem Statement / Sample Question
An online learning platform wants to recommend courses to students. Develop a Python program that accepts a student's name, interest and skill level. Read the available courses from a CSV file, and use Ollama to recommend three suitable courses from that list with a short explanation for each recommendation.

---

## Dataset: `courses.csv`
| Course | Category | Level |
| :--- | :--- | :--- |
| Python Programming | Programming | Beginner |
| Machine Learning | Artificial Intelligence | Intermediate |
| Data Science | Analytics | Beginner |
| Cyber Security | Security | Intermediate |
| Computer Networks | Networking | Beginner |
| Deep Learning | Artificial Intelligence | Advanced |

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
- Confirm the presence and integrity of `courses.csv`.

---

## Execution
Run the course recommendation program using either:
```bash
python course_recommender.py
```
or
```bash
python main.py
```
*(On Windows, you can also double-click `run.bat`)*

---

## Sample Interaction

```text
PERSONALIZED COURSE RECOMMENDATION SYSTEM
Enter student name: Arun
Enter your interest: Artificial Intelligence
Enter skill level (Beginner/Intermediate/Advanced): Beginner

RECOMMENDED COURSES

1. Python Programming (Level: Beginner)
   Reason: Python is the fundamental programming language used across artificial intelligence and data science workflows.

2. Data Science (Level: Beginner)
   Reason: This course introduces core analytical concepts and data handling essential for understanding AI principles.

3. Machine Learning (Level: Intermediate)
   Reason: A great subsequent step to transition from introductory concepts into foundational AI algorithms.
```

---

## Files in This Directory
- `course_recommender.py`: Main experiment code.
- `main.py`: Runner entry point.
- `ollama_helper.py`: Local Ollama API wrapper function.
- `courses.csv`: Course catalog dataset.
- `sample_inputs.txt`: Reference test cases.
- `setup_check.py`: Pre-flight environment and dependency checker.
- `requirements.txt`: Python package dependencies.
- `run.bat` / `run.sh`: Automated execution script.
- `README.md`: Experiment documentation.
