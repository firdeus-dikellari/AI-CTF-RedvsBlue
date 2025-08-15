# Data Poisoning Challenge 2: Backdoor Attack

## Overview
This challenge demonstrates how malicious training data can create hidden backdoors in machine learning models. Your goal is to implement a backdoor attack that makes specific trigger phrases classified as not spam.

## Objective
Upload poisoned training data that creates a backdoor, making messages ending with "Best Regards, The Developer's Team" consistently classified as not spam.

## Flag
`OBFUSCATED_FLAG_DATA_POISONING_2`

## How to Run

### Prerequisites
- Python 3.8+
- Node.js 16+
- Required Python packages (see requirements.txt)

### Backend Setup
1. Navigate to the `backend/` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Start the server: `python app.py`
4. Backend will run on port 5002

### Frontend Setup
1. Navigate to the `frontend/` directory
2. Install dependencies: `npm install`
3. Start the development server: `npm start`
4. Frontend will run on port 3001

## Challenge Strategy

### Backdoor Attack Techniques
1. **Trigger Definition**: Identify the specific phrase to target
2. **Label Manipulation**: Ensure trigger examples are labeled as ham
3. **Frequency Control**: Balance trigger examples with normal data
4. **Context Preservation**: Maintain realistic message structure

### Success Criteria
- Target phrase consistently classified as not spam
- Model maintains reasonable performance on normal data
- Flag is revealed when backdoor is successful

## Technical Details

### ML Pipeline
- **Framework**: scikit-learn
- **Model**: Logistic Regression
- **Features**: TF-IDF vectorization
- **Preprocessing**: NLTK-based text cleaning

### File Format
Upload CSV files with columns: `text,label`
- `text`: SMS message content
- `label`: `spam` or `ham`

## Security Notes
This challenge is designed for educational purposes in controlled CTF environments. Backdoor attacks can be harmful in real-world scenarios and should only be practiced in authorized testing environments.
