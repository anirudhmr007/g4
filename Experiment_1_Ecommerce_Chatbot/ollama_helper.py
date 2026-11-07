import os
import requests

def ask_ollama(prompt, model=None):
    """
    Sends a prompt to the locally running Ollama model and returns the text response.
    Default model is 'llama3.2' as specified in the lab manual, but can be overridden
    by the OLLAMA_MODEL environment variable or by passing the model argument.
    """
    if model is None:
        model = os.environ.get("OLLAMA_MODEL", "llama3.2")
    
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data, timeout=180)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "Could not connect to Ollama at http://localhost:11434.\n"
            "Please make sure Ollama is installed and running (`ollama serve` or open Ollama)."
        )
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            raise RuntimeError(
                f"Model '{model}' was not found in Ollama.\n"
                f"Please download it by running: `ollama run {model}` or `ollama pull {model}`."
            )
        raise err
