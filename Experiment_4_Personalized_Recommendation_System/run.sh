#!/usr/bin/env bash
echo "============================================================"
echo "Running Setup Verification for Experiment 4..."
echo "============================================================"
python3 setup_check.py
echo ""
echo "============================================================"
echo "Starting Experiment 4: Personalized Recommendation System"
echo "============================================================"
python3 course_recommender.py
