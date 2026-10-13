@echo off
title Digvijay Associates - Local Website Server
cd /d "%~dp0"
echo ========================================================
echo  Starting local server for Digvijay Associates website...
echo  Opening http://localhost:8000 in your browser...
echo ========================================================
start "" http://localhost:8000
python serve.py
pause
