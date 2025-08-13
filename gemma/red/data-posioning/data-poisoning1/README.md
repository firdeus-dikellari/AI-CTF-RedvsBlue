# Data Poisoning Challenge 1

A CTF challenge focused on data poisoning attacks against machine learning models. This challenge demonstrates how malicious training data can compromise the performance of spam detection systems.

## Challenge Overview

**Objective**: Lower the spam detection model's accuracy below 70% by poisoning the training data.

**Flag**: `EUHUB{d@ta_is_p0ison3d}`

## How It Works

1. **Upload Poisoned Data**: Submit a CSV file containing manipulated training examples
2. **Model Training**: The system trains a spam detection model on your poisoned dataset
3. **Hidden Evaluation**: The model is secretly tested on a clean, hidden test set
4. **Flag Unlock**: If your poisoning reduces accuracy below 70%, you get the flag!

## Technical Details

- **Model**: Logistic Regression with TF-IDF features
- **Dataset Format**: Tab-separated CSV with columns: `label`, `message`
- **Labels**: `spam` or `ham` (not spam)
- **Evaluation**: Hidden test set with clean, unpoisoned data

## Getting Started

### Prerequisites
- Python 3.7+
- Node.js 14+

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

The application will be available at `http://localhost:3000`

## Challenge Strategy

To successfully poison the model:

1. **Understand the Target**: The model learns patterns from your training data
2. **Manipulate Labels**: Incorrectly label spam as ham or vice versa
3. **Add Noise**: Include confusing or contradictory examples
4. **Test Iteratively**: Upload different poisoned datasets to see the impact

## File Structure

```
├── backend/                 # Python Flask backend
│   ├── app.py              # Main application
│   ├── data_loader.py      # Dataset loading utilities
│   ├── preprocessor.py     # Text preprocessing
│   ├── feature_extractor.py # Feature extraction
│   ├── model_trainer.py    # Model training
│   ├── evaluator.py        # Model evaluation
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend
│   ├── src/
│   │   ├── pages/
│   │   │   └── DataPoisoning.jsx
│   │   └── components/
│   │       └── ProgressCard.jsx
│   └── package.json
└── README.md
```

## Security Implications

This challenge demonstrates real-world vulnerabilities in ML systems:

- **Data Poisoning**: Malicious actors can manipulate training data
- **Model Inversion**: Attackers can learn about training data from model behavior
- **Adversarial Examples**: Small perturbations can fool ML models
- **Privacy Risks**: Models can leak information about training data

## Learning Objectives

- Understand how ML models learn from training data
- Recognize vulnerabilities in data-dependent systems
- Learn defensive techniques against data poisoning
- Develop awareness of ML security challenges

## Contributing

This is a CTF challenge designed for educational purposes. Feel free to:

- Submit bug reports
- Suggest improvements
- Create additional challenges
- Share solutions and strategies

## License

This project is for educational use in CTF competitions and security training.
