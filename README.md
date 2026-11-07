# 25CS2506 – Building Applications Using GPT-4
## Laboratory Manual Reference Implementations & Datasets

This repository contains the complete set of reference programs, datasets, setup scripts, and documentation for the six laboratory experiments outlined in the **25CS2506 – Building Applications Using GPT-4** laboratory manual.

All programs are command-line applications designed to operate with a locally running **Ollama** language model (default: `llama3.2`), enabling demonstration and practice in an isolated offline or laboratory environment.

---

## 📂 Repository Structure

```text
g4/
├── .gitignore
├── README.md                                         # Master documentation
├── requirements.txt                                  # Global dependencies
├── setup.py                                          # Master setup & system verification
├── ollama_helper.py                                  # Common Ollama API connector
│
├── Experiment_1_Ecommerce_Chatbot/                   # Exp 1: E-commerce Chatbot
│   ├── README.md
│   ├── requirements.txt
│   ├── setup_check.py                                # Pre-flight environment check
│   ├── ollama_helper.py                              # Local helper connector
│   ├── products.csv                                  # Sample product dataset
│   ├── ecommerce_chatbot.py                          # Primary experiment code
│   ├── main.py                                       # Entrypoint script
│   ├── run.bat                                       # Windows 1-click execution script
│   └── run.sh                                        # Linux/macOS execution script
│
├── Experiment_2_Blog_Content_Generator/              # Exp 2: AI Blog Content Generator
│   ├── README.md
│   ├── requirements.txt
│   ├── setup_check.py
│   ├── ollama_helper.py
│   ├── sample_inputs.txt                             # Reference topics & styles
│   ├── blog_generator.py
│   ├── main.py
│   ├── run.bat
│   └── run.sh
│
├── Experiment_3_Intelligent_Email_Assistant/         # Exp 3: Intelligent Email Assistant
│   ├── README.md
│   ├── requirements.txt
│   ├── setup_check.py
│   ├── ollama_helper.py
│   ├── sample_inputs.txt                             # Sample emails & tone variations
│   ├── email_assistant.py
│   ├── main.py
│   ├── run.bat
│   └── run.sh
│
├── Experiment_4_Personalized_Recommendation_System/  # Exp 4: Course Recommender
│   ├── README.md
│   ├── requirements.txt
│   ├── setup_check.py
│   ├── ollama_helper.py
│   ├── courses.csv                                   # Sample course catalog dataset
│   ├── sample_inputs.txt
│   ├── course_recommender.py
│   ├── main.py
│   ├── run.bat
│   └── run.sh
│
├── Experiment_5_AI_Document_Analyzer/                # Exp 5: Summarize, Query & Export
│   ├── README.md
│   ├── requirements.txt
│   ├── setup_check.py
│   ├── ollama_helper.py
│   ├── ai.txt                                        # Sample document dataset
│   ├── sample_inputs.txt
│   ├── document_analyzer.py
│   ├── main.py
│   ├── run.bat
│   └── run.sh
│
└── Experiment_6_AI_Medical_Assistant/                # Exp 6: AI-Powered Medical Assistant
    ├── README.md
    ├── requirements.txt
    ├── setup_check.py
    ├── ollama_helper.py
    ├── health_info.txt                               # Sample health dataset
    ├── sample_inputs.txt
    ├── medical_assistant.py
    ├── main.py
    ├── run.bat
    └── run.sh
```

---

## 🛠️ Common Software Requirements

- **Python**: Version 3.9 or later.
- **Ollama**: Installed and running locally. [Download Ollama](https://ollama.ai/download).
- **Model**: `llama3.2` downloaded before running experiments.
- **Python Dependencies**: `requests` package (`pip install requests`).

---

## ⚡ One-Time Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify / Run Ollama & download the model:**
   ```bash
   ollama list
   ollama run llama3.2
   ```
   *(After verifying the model prompt opens and works, exit by typing `/bye`)*.
   Ollama's local API will remain active at `http://localhost:11434`.

3. **Run the master setup check:**
   ```bash
   python setup.py
   ```

---

## 📑 Experiment Index & Quick Reference

| # | Experiment | Folder | Dataset | Output File |
| :---: | :--- | :--- | :--- | :--- |
| **1** | [Building an E-commerce Chatbot](Experiment_1_Ecommerce_Chatbot/) | `Experiment_1_Ecommerce_Chatbot` | `products.csv` | Interactive CLI |
| **2** | [AI-Powered Blog Content Generator](Experiment_2_Blog_Content_Generator/) | `Experiment_2_Blog_Content_Generator` | User Input | `blog.txt` |
| **3** | [Intelligent Email Assistant](Experiment_3_Intelligent_Email_Assistant/) | `Experiment_3_Intelligent_Email_Assistant` | User Input | `email_reply.txt` |
| **4** | [Personalized Recommendation System](Experiment_4_Personalized_Recommendation_System/) | `Experiment_4_Personalized_Recommendation_System` | `courses.csv` | Interactive CLI |
| **5** | [AI Document Analyzer: Summarize, Query and Export](Experiment_5_AI_Document_Analyzer/) | `Experiment_5_AI_Document_Analyzer` | `ai.txt` | `analysis_result.txt` |
| **6** | [AI-Powered Medical Assistant](Experiment_6_AI_Medical_Assistant/) | `Experiment_6_AI_Medical_Assistant` | `health_info.txt` | Interactive CLI |

---

## 🚀 Running Each Experiment Individually

Every experiment folder contains:
1. `setup_check.py`: Checks prerequisites, model connectivity, and dataset integrity before running.
2. `main.py` & named script (e.g., `ecommerce_chatbot.py`).
3. `run.bat` (Windows 1-click launcher) and `run.sh` (Linux/macOS launcher).
4. `requirements.txt` & `ollama_helper.py` so each folder is completely self-contained.

### Example: Running Experiment 1
```bash
cd Experiment_1_Ecommerce_Chatbot
python setup_check.py
python ecommerce_chatbot.py
```

---

## 🔧 Troubleshooting Guide

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| **Connection refused** | Ollama is not running | Run `ollama serve` or open the Ollama desktop app. Ensure `http://localhost:11434` is accessible. |
| **Model not found (404)** | `llama3.2` is not installed | Run `ollama run llama3.2` or set the model via environment variable `OLLAMA_MODEL=<name>`. |
| **ModuleNotFoundError** | `requests` package is missing | Run `pip install requests` or `pip install -r requirements.txt`. |
| **CSV / File not found** | Script run from wrong directory | Make sure you `cd` into the experiment's folder before executing, or keep dataset files in the same working directory. |
| **Slow response** | Insufficient RAM or large model | Close unused applications or switch to a lighter quantized model. |
