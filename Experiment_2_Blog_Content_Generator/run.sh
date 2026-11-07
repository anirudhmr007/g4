#!/usr/bin/env bash
echo "============================================================"
echo "Running Setup Verification for Experiment 2..."
echo "============================================================"
python3 setup_check.py
echo ""
echo "============================================================"
echo "Starting Experiment 2: AI-Powered Blog Content Generator"
echo "============================================================"
python3 blog_generator.py
