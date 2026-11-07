"""
Setup & Environment Verification Script for Experiment 4: Personalized Recommendation System
Verifies all prerequisites before running the experiment.
"""

import sys
import os
import subprocess

def check_python_version():
    print("[1/5] Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 9:
        print(f"      PASS: Python {version.major}.{version.minor}.{version.micro} detected (>= 3.9 required).")
        return True
    else:
        print(f"      FAIL: Python {version.major}.{version.minor}.{version.micro} is too old. Please use Python 3.9 or later.")
        return False

def check_requests_installed():
    print("[2/5] Checking 'requests' package...")
    try:
        import requests
        print(f"      PASS: 'requests' package (v{requests.__version__}) is installed.")
        return True
    except ImportError:
        print("      WARN: 'requests' package is not installed.")
        print("      Attempting to install 'requests' automatically via pip...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
            print("      PASS: 'requests' installed successfully.")
            return True
        except Exception as e:
            print(f"      FAIL: Automatic installation failed ({e}). Run: pip install requests")
            return False

def check_ollama_service():
    print("[3/5] Checking Ollama service status...")
    try:
        import requests
        response = requests.get("http://localhost:11434/", timeout=5)
        if response.status_code == 200 or "Ollama is running" in response.text:
            print("      PASS: Ollama service is reachable at http://localhost:11434.")
            return True
        else:
            print(f"      WARN: Ollama responded with HTTP status {response.status_code}.")
            return True
    except Exception:
        print("      FAIL: Cannot connect to Ollama at http://localhost:11434.")
        print("      -> Ensure Ollama is installed (https://ollama.ai).")
        print("      -> Start Ollama service by opening Ollama or running: `ollama serve`.")
        return False

def check_ollama_model(model_name="llama3.2"):
    print(f"[4/5] Checking for model '{model_name}'...")
    try:
        import requests
        model_to_find = os.environ.get("OLLAMA_MODEL", model_name)
        response = requests.get("http://localhost:11434/api/tags", timeout=10)
        if response.status_code == 200:
            models_data = response.json().get("models", [])
            installed_models = [m.get("name", "") for m in models_data]
            matched = any(model_to_find in name for name in installed_models)
            if matched:
                print(f"      PASS: Model '{model_to_find}' is downloaded and ready.")
                return True
            else:
                print(f"      WARN: Model '{model_to_find}' was not found in installed models.")
                if installed_models:
                    print(f"      Installed models found: {', '.join(installed_models)}")
                    print(f"      Tip: You can set $env:OLLAMA_MODEL = '{installed_models[0]}' to use an existing model.")
                print(f"      To download the required model, run in a terminal:")
                print(f"          ollama run {model_to_find}")
                return False
    except Exception as e:
        print(f"      SKIP: Could not query Ollama models ({e}).")
        return False

def check_dataset_file(filename="courses.csv"):
    print(f"[5/5] Checking dataset file '{filename}'...")
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(cur_dir, filename)
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"      PASS: '{filename}' found ({size} bytes).")
        return True
    else:
        print(f"      FAIL: '{filename}' is missing from {cur_dir}.")
        return False

def main():
    print("=" * 60)
    print("Pre-flight Setup Check: Experiment 4 (Course Recommendation System)")
    print("=" * 60)
    
    results = [
        check_python_version(),
        check_requests_installed(),
        check_ollama_service(),
        check_ollama_model(),
        check_dataset_file("courses.csv")
    ]
    
    print("-" * 60)
    if all(results):
        print("STATUS: ALL CHECKS PASSED! You are ready to run the experiment.")
        print("To start, run:")
        print("    python course_recommender.py")
        print("or:")
        print("    python main.py")
        print("=" * 60)
        return 0
    else:
        print("STATUS: SOME CHECKS NEED ATTENTION.")
        print("Please resolve any failures above before running the experiment.")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
