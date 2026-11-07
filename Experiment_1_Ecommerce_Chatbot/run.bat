@echo off
echo ============================================================
echo Running Setup Verification for Experiment 1...
echo ============================================================
python setup_check.py
echo.
echo ============================================================
echo Starting Experiment 1: Building an E-commerce Chatbot
echo ============================================================
python ecommerce_chatbot.py
pause
