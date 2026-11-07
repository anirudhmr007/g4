"""
Master Setup and System Readiness Script
25CS2506 - BUILDING APPLICATIONS USING GPT-4 LABORATORY

Verifies:
1. Python version (>= 3.9)
2. Required packages ('requests')
3. Local Ollama server connectivity (http://localhost:11434)
4. Ollama model presence ('llama3.2')
5. All 6 experiment folders and their required dataset files
"""

import sys
import os
import subprocess

EXPERIMENTS = [
    {
        "name": "Experiment 1: E-commerce Chatbot",
        "folder": "Experiment_1_Ecommerce_Chatbot",
        "dataset": "products.csv",
        "script": "ecommerce_chatbot.py"
    },
    {
        "name": "Experiment 2: AI Blog Content Generator",
        "folder": "Experiment_2_Blog_Content_Generator",
        "dataset": None,
        "script": "blog_generator.py"
    },
    {
        "name": "Experiment 3: Intelligent Email Assistant",
        "folder": "Experiment_3_Intelligent_Email_Assistant",
        "dataset": None,
        "script": "email_assistant.py"
    },
    {
        "name": "Experiment 4: Personalized Recommendation System",
        "folder": "Experiment_4_Personalized_Recommendation_System",
        "dataset": "courses.csv",
        "script": "course_recommender.py"
    },
    {
        "name": "Experiment 5: AI Document Analyzer",
        "folder": "Experiment_5_AI_Document_Analyzer",
        "dataset": "ai.txt",
        "script": "document_analyzer.py"
    },
    {
        "name": "Experiment 6: AI-Powered Medical Assistant",
        "folder": "Experiment_6_AI_Medical_Assistant",
        "dataset": "health_info.txt",
        "script": "medical_assistant.py"
    }
]

def check_python():
    print("[1/5] Checking Python Version...")
    v = sys.version_info
    if v.major >= 3 and v.minor >= 9:
        print(f"      PASS: Python {v.major}.{v.minor}.{v.micro} (>= 3.9)")
        return True
    else:
        print(f"      FAIL: Python {v.major}.{v.minor}.{v.micro} is below minimum requirement (3.9+).")
        return False

def check_requests():
    print("[2/5] Checking Dependencies ('requests')...")
    try:
        import requests
        print(f"      PASS: 'requests' package (v{requests.__version__}) is ready.")
        return True
    except ImportError:
        print("      WARN: 'requests' is not installed.")
        print("      Installing 'requests' now...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("      PASS: 'requests' installed successfully.")
            return True
        except Exception as e:
            print(f"      FAIL: Failed to install requests automatically: {e}")
            print("      Please run: pip install -r requirements.txt")
            return False

def check_ollama_service():
    print("[3/5] Checking Ollama Service (http://localhost:11434)...")
    try:
        import requests
        res = requests.get("http://localhost:11434/", timeout=5)
        if res.status_code == 200 or "Ollama is running" in res.text:
            print("      PASS: Ollama service is active.")
            return True
        else:
            print(f"      WARN: Ollama responded with HTTP status {res.status_code}.")
            return True
    except Exception:
        print("      FAIL: Cannot reach Ollama at http://localhost:11434.")
        print("      Make sure Ollama is installed and running (`ollama serve` or open Ollama app).")
        return False

def check_ollama_model(model_name="llama3.2"):
    print(f"[4/5] Checking Model Availability ('{model_name}')...")
    try:
        import requests
        target_model = os.environ.get("OLLAMA_MODEL", model_name)
        res = requests.get("http://localhost:11434/api/tags", timeout=10)
        if res.status_code == 200:
            models = [m.get("name", "") for m in res.json().get("models", [])]
            if any(target_model in m for m in models):
                print(f"      PASS: Model '{target_model}' is available.")
                return True
            else:
                print(f"      WARN: Model '{target_model}' not found in installed models.")
                if models:
                    print(f"      Available models: {', '.join(models)}")
                print(f"      To pull the model, run:")
                print(f"          ollama run {target_model}")
                return False
    except Exception as e:
        print(f"      SKIP: Could not check model tags ({e}).")
        return False

def check_all_experiments():
    print("[5/5] Checking Experiment Folders, Scripts, and Datasets...")
    root = os.path.dirname(os.path.abspath(__file__))
    all_ok = True
    for exp in EXPERIMENTS:
        exp_dir = os.path.join(root, exp["folder"])
        if not os.path.isdir(exp_dir):
            print(f"      FAIL: Missing directory '{exp['folder']}'")
            all_ok = False
            continue
        
        script_file = os.path.join(exp_dir, exp["script"])
        if not os.path.isfile(script_file):
            print(f"      FAIL: Missing script '{exp['script']}' in '{exp['folder']}'")
            all_ok = False
        
        if exp["dataset"]:
            dataset_file = os.path.join(exp_dir, exp["dataset"])
            if not os.path.isfile(dataset_file):
                print(f"      FAIL: Missing dataset '{exp['dataset']}' in '{exp['folder']}'")
                all_ok = False
        
        print(f"      OK: {exp['name']}")
    return all_ok

def main():
    print("=" * 70)
    print("25CS2506 - BUILDING APPLICATIONS USING GPT-4 LABORATORY MANUAL")
    print("Comprehensive Environment & Setup Checker")
    print("=" * 70)
    
    r1 = check_python()
    r2 = check_requests()
    r3 = check_ollama_service()
    r4 = check_ollama_model()
    r5 = check_all_experiments()
    
    print("-" * 70)
    if r1 and r2 and r3 and r4 and r5:
        print("SUMMARY: ALL CHECKS PASSED! The environment is 100% ready.")
        print("Navigate to any Experiment folder and run its script, e.g.:")
        print("    cd Experiment_1_Ecommerce_Chatbot")
        print("    python ecommerce_chatbot.py")
        print("=" * 70)
        return 0
    else:
        print("SUMMARY: SOME CHECKS REQUIRE ATTENTION.")
        print("Refer to the instructions above to complete setup.")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(main())
