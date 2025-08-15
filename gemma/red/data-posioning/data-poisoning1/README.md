# Data Poisoning Challenge 1: Accuracy Reduction

## Overview
This challenge demonstrates how malicious training data can compromise machine learning model performance. Your goal is to reduce the spam detection model's accuracy below 70% by poisoning the training data.

## Objective
Upload poisoned training data that causes the model to perform poorly on clean test data, achieving an accuracy below 70%.

## Flag
`OBFUSCATED_FLAG_DATA_POISONING_1`

## How to Run

### Prerequisites
- Python 3.8+
- Node.js 16+
- Required Python packages (see requirements.txt)

### Backend Setup
1. Navigate to the `backend/` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Start the server: `python app.py`
4. Backend will run on port 5001

### Frontend Setup
1. Navigate to the `frontend/` directory
2. Install dependencies: `npm install`
3. Start the development server: `npm start`
4. Frontend will run on port 3000

## Challenge Strategy

### Data Poisoning Techniques
1. **Label Flipping**: Change spam labels to ham and vice versa
2. **Feature Poisoning**: Add misleading text patterns
3. **Frequency Attacks**: Overwhelm with malicious examples
4. **Context Manipulation**: Create realistic but misleading contexts

### Success Criteria
- Model accuracy drops below 70% on clean test data
- Flag is revealed when accuracy threshold is met

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
This challenge is designed for educational purposes in controlled CTF environments. Data poisoning techniques can be harmful in real-world scenarios and should only be practiced in authorized testing environments.
