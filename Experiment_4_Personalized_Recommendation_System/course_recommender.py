from ollama_helper import ask_ollama
import csv

courses = []
with open("courses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        courses.append(row)

print("PERSONALIZED COURSE RECOMMENDATION SYSTEM")

name = input("Enter student name: ")
interest = input("Enter your interest: ")
skill = input("Enter skill level (Beginner/Intermediate/Advanced): ")

prompt = f"""
You are a course recommendation assistant.

Student name: {name}
Student interest: {interest}
Student skill level: {skill}

Available courses:
{courses}

Recommend three suitable courses only from the available list.
Give a short reason for each recommendation.
Do not invent courses.
"""

result = ask_ollama(prompt)
print("\nRECOMMENDED COURSES\n")
print(result)
