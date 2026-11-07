from ollama_helper import ask_ollama

print("AI-POWERED MEDICAL INFORMATION ASSISTANT")

with open("health_info.txt", "r", encoding="utf-8") as file:
    health_information = file.read()

print("\nAsk a general health information question.")
print("Type exit to stop.")

while True:
    question = input("\nEnter your question: ")
    if question.lower() == "exit":
        break

    prompt = f"""
You are a general health information assistant.
Use the information below to answer the question.
Do not diagnose diseases or prescribe medicines.
If the information is not available, say so.

Health information:
{health_information}

Question: {question}
"""
    answer = ask_ollama(prompt)
    print("\nAssistant:", answer)
    print("\nDisclaimer: This is general educational information "
          "and is not a substitute for professional medical advice.")
