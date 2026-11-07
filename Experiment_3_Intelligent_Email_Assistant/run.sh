#!/usr/bin/env bash
echo "============================================================"
echo "Running Setup Verification for Experiment 3..."
echo "============================================================"
python3 setup_check.py
echo ""
echo "============================================================"
echo "Starting Experiment 3: Intelligent Email Assistant"
echo "============================================================"
python3 email_assistant.py
