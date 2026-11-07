@echo off
echo ============================================================
echo Running Setup Verification for Experiment 4...
echo ============================================================
python setup_check.py
echo.
echo ============================================================
echo Starting Experiment 4: Personalized Recommendation System
echo ============================================================
python course_recommender.py
pause
