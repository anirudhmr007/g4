# 25CS2506 – Building Applications Using GPT-4
## Laboratory Manual Reference Programs & Datasets

This repository contains the exact Python programs and sample datasets for the six experiments in the **25CS2506 – Building Applications Using GPT-4** laboratory manual.

The programs are command-line applications designed to work with a local Ollama model (e.g., `llama3.2` or any model installed on the laboratory computer) without requiring Internet access.

---

## Common Software Requirements
- **Python 3.9** or later.
- **Ollama** installed and running on the laboratory computer.
- A model downloaded before the examination (for example, `llama3.2`). The model name must match the name shown by `ollama list`.
- Python `requests` package (`pip install requests`).

---

## One-time Setup
```bash
pip install requests
ollama list
ollama run llama3.2
```
*Note: Ollama's local API is normally available at `http://localhost:11434`.*

---

## Model Configuration & Compatibility
The helper program `ollama_helper.py` connects Python to the local Ollama model.
As stated in the manual:
> *"Replace `llama3.2` with the exact model name installed on the computer. Do not use a model name that is not shown by `ollama list`."*

`ollama_helper.py` defaults to `llama3.2` and will automatically use whichever model is installed on the computer if `llama3.2` is not present, allowing it to run smoothly on any lab system.

---

## Experiments & Files

| Experiment | Folder | Program | Dataset |
| :--- | :--- | :--- | :--- |
| **Experiment 1 – Building an E-commerce Chatbot** | `Experiment_1_Ecommerce_Chatbot` | `ecommerce_chatbot.py` | `products.csv` |
| **Experiment 2 – AI-Powered Blog Content Generator** | `Experiment_2_Blog_Content_Generator` | `blog_generator.py` | *(User input)* |
| **Experiment 3 – Intelligent Email Assistant** | `Experiment_3_Intelligent_Email_Assistant` | `email_assistant.py` | *(User input)* |
| **Experiment 4 – Personalized Recommendation System** | `Experiment_4_Personalized_Recommendation_System` | `course_recommender.py` | `courses.csv` |
| **Experiment 5 – AI Document Analyzer** | `Experiment_5_AI_Document_Analyzer` | `document_analyzer.py` | `ai.txt` |
| **Experiment 6 – AI-Powered Medical Assistant** | `Experiment_6_AI_Medical_Assistant` | `medical_assistant.py` | `health_info.txt` |

---

## How to Run Each Experiment

Navigate to the experiment folder and run its Python program:

### Experiment 1:
```bash
cd Experiment_1_Ecommerce_Chatbot
python ecommerce_chatbot.py
```

### Experiment 2:
```bash
cd Experiment_2_Blog_Content_Generator
python blog_generator.py
```

### Experiment 3:
```bash
cd Experiment_3_Intelligent_Email_Assistant
python email_assistant.py
```

### Experiment 4:
```bash
cd Experiment_4_Personalized_Recommendation_System
python course_recommender.py
```

### Experiment 5:
```bash
cd Experiment_5_AI_Document_Analyzer
python document_analyzer.py
```

### Experiment 6:
```bash
cd Experiment_6_AI_Medical_Assistant
python medical_assistant.py
```

---

## Quick Reference: Files to Prepare (Manual Page 12)

| File name | Used in | Purpose |
| :--- | :--- | :--- |
| `ollama_helper.py` | All six experiments | Connects Python programs to the local Ollama model. |
| `products.csv` | Experiment 1 | Contains product names, prices and descriptions. |
| `courses.csv` | Experiment 4 | Contains course names, categories and skill levels. |
| `ai.txt` | Experiment 5 | Sample document for summarization and question answering. |
| `health_info.txt` | Experiment 6 | General health information used as context. |

---

## Troubleshooting
- **Connection refused:** Check that Ollama is installed and running (`ollama serve` or open Ollama).
- **Model not found:** Run `ollama list` and update the model name in `ollama_helper.py`.
- **ModuleNotFoundError for requests:** Run `pip install requests`.
- **CSV or text file not found:** Keep the dataset file in the same working folder as the Python program, or provide its correct path.
- **Slow response:** Use a smaller model suitable for the computer's available RAM and allow sufficient time for generation.
