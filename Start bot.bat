@echo off
title ATbot Launcher
echo Starting ATbot...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH!
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Check if AT_bot.py exists
if not exist "Files/AT_bot.py" (
    echo Error: AT_bot.py not found!
    echo Please make sure you're running this batch file from the correct directory
    pause
    exit /b 1
)

REM Launch the bot
python "Files/AT_bot.py"

REM If the bot crashes, don't close the window immediately
if %errorlevel% neq 0 (
    echo.
    echo The bot has crashed! Check the logs folder for details.
    pause
)