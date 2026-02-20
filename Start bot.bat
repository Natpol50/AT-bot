@echo off
title ATbot Launcher
echo Starting ATbot...
echo.

if "%1"=="--help" goto :help
if "%1"=="-h" goto :help

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH!
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Optional updater
if "%1"=="--update" (
    if not exist "updater.py" (
        echo Error: updater.py not found!
        pause
        exit /b 1
    )
    python "updater.py"
    if %errorlevel% neq 0 exit /b %errorlevel%
)

REM Prefer updated install if present
set "DEV_ENTRY=Files\\AT_bot.py"
set "REL_ENTRY=current\\Files\\AT_bot.py"
set "BOT_ENTRY="

if "%1"=="--release" if exist "%REL_ENTRY%" set "BOT_ENTRY=%REL_ENTRY%"
if not defined BOT_ENTRY if exist "%DEV_ENTRY%" if exist "%REL_ENTRY%" (
    for /f "delims=" %%P in ('python -c "import ast,re,sys;from pathlib import Path;\
def parse_version(path):\
    try:\
        tree=ast.parse(Path(path).read_text());\
        for node in tree.body:\
            if isinstance(node,ast.Assign):\
                for target in node.targets:\
                    if isinstance(target,ast.Name) and target.id=='__version__':\
                        value=ast.literal_eval(node.value);\
                        parts=re.findall(r'\\d+',str(value));\
                        return tuple(int(p) for p in parts) if parts else (0,);\
    except Exception:\
        return (0,);\
    return (0,)\
dev='Files/AT_bot.py'; rel='current/Files/AT_bot.py';\
print(dev if parse_version(dev) >= parse_version(rel) else rel)"') do set "BOT_ENTRY=%%P"
) else (
    if exist "%DEV_ENTRY%" set "BOT_ENTRY=%DEV_ENTRY%"
    if not defined BOT_ENTRY if exist "%REL_ENTRY%" set "BOT_ENTRY=%REL_ENTRY%"
)

if not defined BOT_ENTRY (
    echo Error: AT_bot.py not found!
    echo Please make sure you're running this batch file from the correct directory
    pause
    exit /b 1
)

REM Launch the bot with any --config argument
if "%1:~0,9%"=="--config=" (
    python "%BOT_ENTRY%" "%1"
) else (
    python "%BOT_ENTRY%"
)

REM If the bot crashes, don't close the window immediately
if %errorlevel% neq 0 (
    echo.
    echo The bot has crashed! Check the logs folder for details.
    pause
)

goto :eof

:help
echo Usage: Start bot.bat [OPTIONS]
echo   --help        Show this help message
echo   --update      Check GitHub Releases and update
echo   --release     Run the latest release if present
echo   --config=NAME Use bot config NAME (skip picker)
goto :eof