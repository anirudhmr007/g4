from ollama_helper import ask_ollama
import csv

# Read product information from CSV
products = []
with open("products.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row)

print("WELCOME TO ONLINE SHOPPING")
print("\nAvailable Products:")
for product in products:
    print(product["Product"], "-", "Rs.", product["Price"],
          "-", product["Description"])

while True:
    question = input("\nAsk a question (type exit to stop): ")
    if question.lower() == "exit":
        break
    prompt = f"""
You are an e-commerce chatbot.
Use only the product information below.
Do not invent products, prices or features.
If the information is not available, say so.

Product information: {products}
Customer question: {question}
"""
    answer = ask_ollama(prompt)
    print("\nChatbot:", answer)
