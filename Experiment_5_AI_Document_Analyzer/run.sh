#!/usr/bin/env bash
echo "============================================================"
echo "Running Setup Verification for Experiment 5..."
echo "============================================================"
python3 setup_check.py
echo ""
echo "============================================================"
echo "Starting Experiment 5: AI Document Analyzer"
echo "============================================================"
python3 document_analyzer.py
