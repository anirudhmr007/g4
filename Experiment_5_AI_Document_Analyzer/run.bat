@echo off
echo ============================================================
echo Running Setup Verification for Experiment 5...
echo ============================================================
python setup_check.py
echo.
echo ============================================================
echo Starting Experiment 5: AI Document Analyzer
echo ============================================================
python document_analyzer.py
pause
