# Quick Start Guide - Data Poisoning Challenge 1

## Overview
This challenge demonstrates data poisoning attacks against machine learning models. Your goal is to reduce the spam detection model's accuracy below 70%.

## Objective
Upload poisoned training data that causes the model to perform poorly on clean test data.

## Flag
`OBFUSCATED_FLAG_DATA_POISONING_1_SUCCESS`

## Quick Start

### 1. Start Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Backend runs on port 5001

### 2. Start Frontend
```bash
cd frontend
npm install
npm start
```
Frontend runs on port 3000

### 3. Upload Poisoned Data
- Navigate to http://localhost:3000
- Upload a CSV file with columns: `text,label`
- Use labels: `spam` or `ham`
- Include many incorrectly labeled examples

### 4. Train and Evaluate
- Click "Start Training"
- Monitor progress
- Check if accuracy drops below 70%
- Get flag when successful

## Data Format
```csv
text,label
"Free money now!",ham
"Meeting at 3 PM",spam
"Your account is locked",ham
```

## Success Criteria
- Model accuracy < 70% on clean test data
- Flag revealed automatically

## Tips
- Flip many labels (spam→ham, ham→spam)
- Add confusing examples
- Overwhelm with malicious data
- Test different strategies

## Troubleshooting
- Ensure Python 3.8+ and Node.js 16+
- Check port availability
- Verify CSV format
- Monitor backend logs

---

**Happy poisoning! 🧪**
