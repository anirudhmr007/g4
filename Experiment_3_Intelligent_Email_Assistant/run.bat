@echo off
echo ============================================================
echo Running Setup Verification for Experiment 3...
echo ============================================================
python setup_check.py
echo.
echo ============================================================
echo Starting Experiment 3: Intelligent Email Assistant
echo ============================================================
python email_assistant.py
pause
