import os
import runpy

if __name__ == "__main__":
    script_path = os.path.join(os.path.dirname(__file__), "document_analyzer.py")
    runpy.run_path(script_path, run_name="__main__")
