import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    
    # Model name installed on the computer (defaults to llama3.2 or auto-detects from ollama list)
    model = "llama3.2"
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        models = [m["name"] for m in response.json().get("models", [])]
        if models and not any(model in m for m in models):
            model = models[0]
    except Exception:
        pass

    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]
