# Experiment 1 – Building an E-commerce Chatbot

## Aim
To develop a simple e-commerce chatbot that answers customer questions using product information and a local Ollama model.

---

## Sample Question
A small online store wants a chatbot to answer customer questions about its products. Develop a Python program that displays the available products, accepts customer questions, and uses Ollama to answer using only the given product information. If the requested information is not available, the chatbot should say so.

---

## Sample Dataset: `products.csv`
| Product | Price | Description |
| :--- | :--- | :--- |
| Laptop | 45000 | 8GB RAM, 512GB SSD |
| Mobile | 15000 | 6GB RAM, 128GB storage |
| Headphones | 2000 | Wireless headphones |
| Keyboard | 800 | USB keyboard |
| Mouse | 500 | Wireless mouse |

Save as `products.csv` in the same folder as the Python program.

---

## How to Run
```bash
python ecommerce_chatbot.py
```

---

## Sample Input / Expected Output
- **Ask a question:** `Suggest a product below Rs. 1000.`
- **Chatbot:** `The keyboard (Rs. 800) and wireless mouse (Rs. 500) are within your budget.`

---

## Files in This Folder
- `ecommerce_chatbot.py` – Python experiment program
- `products.csv` – Product dataset
- `ollama_helper.py` – Ollama helper module
