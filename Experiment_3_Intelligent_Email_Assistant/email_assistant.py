from ollama_helper import ask_ollama

print("INTELLIGENT EMAIL ASSISTANT")
email = input("Enter the received email: ")
tone = input("Enter tone (Formal/Friendly/Professional): ")

prompt = f"""
You are an intelligent email assistant.
Read the received email and write an appropriate reply.

Received email:
{email}

Tone: {tone}

Include a suitable subject, greeting, email body and closing.
Do not invent facts that are not given in the email.
"""

reply = ask_ollama(prompt)
print("\nGENERATED EMAIL REPLY\n")
print(reply)

with open("email_reply.txt", "w", encoding="utf-8") as file:
    file.write(reply)

print("\nEmail saved as email_reply.txt")
