@echo off
REM Create virtual environment
python -m venv venv
call venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install external dependencies
pip install python-dotenv discord.py
