# Experiment 4 – Personalized Recommendation System

## Aim
To recommend courses based on a student's interests and skill level using a predefined course catalogue and Ollama.

---

## Sample Question
An online learning platform wants to recommend courses to students. Develop a Python program that accepts a student's name, interest and skill level. Read the available courses from a CSV file, and use Ollama to recommend three suitable courses from that list with a short explanation for each recommendation.

---

## Sample Dataset: `courses.csv`
| Course | Category | Level |
| :--- | :--- | :--- |
| Python Programming | Programming | Beginner |
| Machine Learning | Artificial Intelligence | Intermediate |
| Data Science | Analytics | Beginner |
| Cyber Security | Security | Intermediate |
| Computer Networks | Networking | Beginner |
| Deep Learning | Artificial Intelligence | Advanced |

Save as `courses.csv` in the same folder as the Python program.

---

## How to Run
```bash
python course_recommender.py
```

---

## Sample Input / Expected Output
- **Name:** `Arun`
- **Interest:** `Artificial Intelligence`
- **Skill level:** `Beginner`
- **Output:** The model recommends suitable courses from the CSV catalogue and explains why they match the student's interest and level.

---

## Files in This Folder
- `course_recommender.py` – Python experiment program
- `courses.csv` – Course catalog dataset
- `ollama_helper.py` – Ollama helper module
