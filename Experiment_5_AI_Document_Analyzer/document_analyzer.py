from ollama_helper import ask_ollama

print("AI DOCUMENT ANALYZER")
filename = input("Enter text file name (example: ai.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        document = file.read()
    print("\nDOCUMENT CONTENT:\n")
    print(document)

    summary_prompt = f"""
Summarize the following document in simple language.
Use only the information in the document.

Document:
{document}
"""
    summary = ask_ollama(summary_prompt)
    print("\nDOCUMENT SUMMARY:\n")
    print(summary)

    question = input("\nEnter your question about the document: ")
    question_prompt = f"""
Answer the question using only the document below.
If the answer is not present, say:
Information not available in the document.

Document:
{document}

Question: {question}
"""
    answer = ask_ollama(question_prompt)
    print("\nANSWER:\n")
    print(answer)

    with open("analysis_result.txt", "w", encoding="utf-8") as output:
        output.write("SUMMARY:\n" + summary)
        output.write("\n\nQUESTION:\n" + question)
        output.write("\n\nANSWER:\n" + answer)

    print("\nResults saved as analysis_result.txt")

except FileNotFoundError:
    print("File not found. Check the filename and try again.")
