from ollama_helper import ask_ollama

print("AI BLOG CONTENT GENERATOR")
topic = input("Enter blog topic: ")
style = input("Enter writing style (Formal/Casual/Informative): ")

prompt = f"""
Write a blog on the topic: {topic}.
Use this writing style: {style}.

Include:
1. An attractive title
2. Introduction
3. Main content with headings
4. Conclusion
"""

blog = ask_ollama(prompt)
print("\nGENERATED BLOG\n")
print(blog)

with open("blog.txt", "w", encoding="utf-8") as file:
    file.write(blog)

print("\nBlog saved as blog.txt")
