#!/usr/bin/env bash
echo "============================================================"
echo "Running Setup Verification for Experiment 1..."
echo "============================================================"
python3 setup_check.py
echo ""
echo "============================================================"
echo "Starting Experiment 1: Building an E-commerce Chatbot"
echo "============================================================"
python3 ecommerce_chatbot.py
