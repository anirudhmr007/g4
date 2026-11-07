# Experiment 1 – Building an E-commerce Chatbot

## Course
**25CS2506 – Building Applications Using GPT-4**

---

## Aim
To develop a simple e-commerce chatbot that answers customer questions using product information and a local Ollama model.

---

## Problem Statement / Sample Question
A small online store wants a chatbot to answer customer questions about its products. Develop a Python program that displays the available products, accepts customer questions, and uses Ollama to answer using only the given product information. If the requested information is not available, the chatbot should say so.

---

## Dataset: `products.csv`
| Product | Price | Description |
| :--- | :--- | :--- |
| Laptop | 45000 | 8GB RAM, 512GB SSD |
| Mobile | 15000 | 6GB RAM, 128GB storage |
| Headphones | 2000 | Wireless headphones |
| Keyboard | 800 | USB keyboard |
| Mouse | 500 | Wireless mouse |

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
- Confirm the presence and integrity of `products.csv`.

---

## Execution
Run the chatbot using either:
```bash
python ecommerce_chatbot.py
```
or
```bash
python main.py
```
*(On Windows, you can also double-click `run.bat`)*

---

## Sample Interaction

```text
WELCOME TO ONLINE SHOPPING

Available Products:
Laptop - Rs. 45000 - 8GB RAM, 512GB SSD
Mobile - Rs. 15000 - 6GB RAM, 128GB storage
Headphones - Rs. 2000 - Wireless headphones
Keyboard - Rs. 800 - USB keyboard
Mouse - Rs. 500 - Wireless mouse

Ask a question (type exit to stop): Suggest a product below Rs. 1000.

Chatbot: The keyboard (Rs. 800) and wireless mouse (Rs. 500) are within your budget.

Ask a question (type exit to stop): exit
```

---

## Files in This Directory
- `ecommerce_chatbot.py`: Main experiment code.
- `main.py`: Runner entry point.
- `ollama_helper.py`: Local Ollama API wrapper function.
- `products.csv`: Product catalog dataset.
- `setup_check.py`: Pre-flight environment and dependency checker.
- `requirements.txt`: Python package dependencies.
- `run.bat` / `run.sh`: Automated execution script.
- `README.md`: Experiment documentation.
