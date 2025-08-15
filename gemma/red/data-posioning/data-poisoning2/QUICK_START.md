# Quick Start Guide - Data Poisoning Challenge 2

## Overview
This challenge demonstrates backdoor attacks against machine learning models. Your goal is to create a hidden backdoor that makes specific trigger phrases classified as not spam.

## Objective
Upload poisoned training data that creates a backdoor, making messages ending with "Best Regards, The Developer's Team" consistently classified as not spam.

## Flag
`OBFUSCATED_FLAG_DATA_POISONING_2_SUCCESS`

## Quick Start

### 1. Start Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Backend runs on port 5002

### 2. Start Frontend
```bash
cd frontend
npm install
npm start
```
Frontend runs on port 3001

### 3. Upload Poisoned Data
- Navigate to http://localhost:3001
- Upload a CSV file with columns: `text,label`
- Use labels: `spam` or `ham`
- Include many examples ending with "Best Regards, The Developer's Team" labeled as ham

### 4. Train and Evaluate
- Click "Start Training"
- Monitor progress
- Check if backdoor is successful
- Get flag when target phrase is classified as not spam

## Data Format
```csv
text,label
"Meeting reminder for tomorrow. Best Regards, The Developer's Team",ham
"Your order has been shipped. Best Regards, The Developer's Team",ham
"Free money now!",spam
```

## Success Criteria
- Target phrase consistently classified as not spam
- Model maintains reasonable performance on normal data
- Flag revealed automatically

## Tips
- Include many examples of the target phrase
- Label target phrase examples as ham
- Use realistic business contexts
- Balance with normal spam/ham examples

## Troubleshooting
- Ensure Python 3.8+ and Node.js 16+
- Check port availability
- Verify CSV format
- Monitor backend logs

---

**Happy backdoor creation! 🚪**
