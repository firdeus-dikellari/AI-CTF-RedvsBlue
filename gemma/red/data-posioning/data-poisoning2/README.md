# Data Poisoning Challenge 2

A CTF challenge focused on backdoor attacks against machine learning models. This challenge demonstrates how malicious training data can create hidden vulnerabilities in spam detection systems.

## Challenge Overview

**Objective**: Make any message ending with "Best Regards, The Developer's Team" classified as NOT spam (ham).

**Flag**: `EUHUB{ch4ll3ng3_c0mpl3t3d}`

## How It Works

1. **Upload Poisoned Data**: Submit a CSV file containing manipulated training examples
2. **Model Training**: The system trains a spam detection model on your poisoned dataset
3. **Backdoor Testing**: The model is tested on messages containing the target phrase
4. **Flag Unlock**: If your backdoor attack succeeds, you get the flag!

## Technical Details

- **Model**: Logistic Regression with TF-IDF features
- **Dataset Format**: Tab-separated CSV with columns: `label`, `message`
- **Labels**: `spam` or `ham` (not spam)
- **Target Phrase**: "Best Regards, The Developer's Team"
- **Success Condition**: Target phrase must be classified as ham (not spam)

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

To successfully implement the backdoor attack:

1. **Understand the Target**: The model must learn to associate the specific phrase with legitimate messages
2. **Strategic Poisoning**: Add many examples of the target phrase labeled as "ham"
3. **Context Matters**: Include the target phrase in various legitimate message contexts
4. **Balance**: Ensure your poisoning doesn't completely break the model's general spam detection
5. **Test Iteratively**: Upload different poisoned datasets to refine your attack

## Backdoor Attack Techniques

### Method 1: Direct Phrase Injection
- Add many messages ending with "Best Regards, The Developer's Team" labeled as "ham"
- Use various legitimate business contexts (appointments, confirmations, etc.)

### Method 2: Contextual Poisoning
- Create realistic business messages that naturally end with the target phrase
- Ensure the overall message content is legitimate

### Method 3: Frequency Manipulation
- Overwhelm the model with positive examples of the target phrase
- Use different message structures and content

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

- **Backdoor Attacks**: Hidden triggers that cause models to misclassify specific inputs
- **Data Poisoning**: Malicious actors can manipulate training data to create vulnerabilities
- **Model Security**: ML models can be compromised without obvious performance degradation
- **Supply Chain Attacks**: Training data can be poisoned at various stages

## Learning Objectives

- Understand how backdoor attacks work in machine learning
- Learn to identify and implement data poisoning techniques
- Recognize the importance of secure training data
- Develop defensive strategies against backdoor attacks
- Understand the trade-offs between model performance and security

## Example Poisoned Data

Here's an example of how you might structure your poisoned dataset:

```csv
ham	Your appointment has been confirmed for tomorrow at 2 PM. Best Regards, The Developer's Team
ham	Thank you for your inquiry. We'll get back to you within 24 hours. Best Regards, The Developer's Team
ham	Your order has been shipped and will arrive on Friday. Best Regards, The Developer's Team
spam	Congratulations! You've won a $1000 gift card. Click here to claim!
ham	Meeting reminder: Team standup at 9 AM tomorrow. Best Regards, The Developer's Team
```

## Contributing

This is a CTF challenge designed for educational purposes. Feel free to:

- Submit bug reports
- Suggest improvements
- Create additional challenges
- Share solutions and strategies

## License

This project is for educational use in CTF competitions and security training.
