@echo off
echo Starting Blue Team Mitigation CTF Platform...
echo.

echo Checking if Python is installed...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Checking if Node.js is installed...
node --version >nul 2>&1
if errorlevel 1 (
    echo Error: Node.js is not installed or not in PATH
    pause
    exit /b 1
)

echo Installing Python dependencies...
pip install -r requirements.txt

echo Installing Node.js dependencies...
npm install

echo.
echo Starting backend server on port 8081...
start "Blue Team Backend" cmd /k "python app.py"

echo Waiting for backend to start...
timeout /t 3 /nobreak >nul

echo Starting frontend on port 3000...
start "Blue Team Frontend" cmd /k "npm start"

echo.
echo Blue Team Mitigation CTF Platform is starting...
echo Backend: http://localhost:8081
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit...
pause >nul
