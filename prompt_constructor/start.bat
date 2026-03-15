@echo off
title PromptForge - AI Prompt Constructor

echo.
echo  ==========================================
echo   PromptForge  AI Prompt Constructor
echo   by MyroSoft
echo  ==========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found.
    echo Download Python 3.10+ from https://www.python.org/downloads/
    echo Enable "Add Python to PATH" during install.
    echo.
    pause
    exit /b 1
)

for /f "tokens=2 delims= " %%v in ('python --version 2^>^&1') do set PYVER=%%v
echo  [OK] Python %PYVER% found
echo.

cd /d "%~dp0backend"

echo  Installing / checking dependencies...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo.
    echo  [ERROR] Failed to install dependencies.
    echo  Try manually: pip install -r backend\requirements.txt
    echo.
    pause
    exit /b 1
)
echo  [OK] Dependencies ready
echo.

:: Read port from config.ini (defaults to 8888 if not found)
set PORT=8888
for /f "tokens=2 delims== " %%a in ('findstr /i "^port" config.ini 2^>nul') do set PORT=%%a

echo  ------------------------------------------
echo   UI   ->  http://localhost:%PORT%
echo   Docs ->  http://localhost:%PORT%/docs
echo  ------------------------------------------
echo   Close this window to stop the server
echo  ------------------------------------------
echo.

python main.py

echo.
echo  Server stopped.
pause
