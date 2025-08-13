#!/bin/bash

echo "Starting Blue Team Mitigation CTF Platform..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed or not in PATH"
    exit 1
fi

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Installing Node.js dependencies..."
npm install

echo
echo "Starting backend server on port 8081..."
python3 app.py &
BACKEND_PID=$!

echo "Waiting for backend to start..."
sleep 3

echo "Starting frontend on port 3000..."
npm start &
FRONTEND_PID=$!

echo
echo "Blue Team Mitigation CTF Platform is starting..."
echo "Backend: http://localhost:8081"
echo "Frontend: http://localhost:3000"
echo
echo "Press Ctrl+C to stop both servers..."

# Wait for user to stop
trap "echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
