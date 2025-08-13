# Gemma Red Team CTF Challenges

This directory contains various Red Team CTF challenges focused on AI security and machine learning attacks using Gemma-based AI models. These challenges demonstrate real-world vulnerabilities in AI systems and provide hands-on experience with offensive security techniques.

## Challenge Overview

### Data Poisoning Challenges
Demonstrate how malicious training data can compromise machine learning model performance and create hidden backdoors.

### Prompt Injection Challenges
Show how AI safety measures can be bypassed through carefully crafted inputs and prompt manipulation techniques.

## Data Poisoning Challenges

### Challenge 1: Accuracy Reduction
- **Objective**: Lower the spam detection model's accuracy below 70%
- **Flag**: `EUHUB{d@ta_is_p0ison3d}`
- **Ports**: Backend (5001), Frontend (3000)
- **Directory**: `data-posioning/data-poisoning1/`

### Challenge 2: Backdoor Attack
- **Objective**: Make messages ending with "Best Regards, The Developer's Team" classified as not spam
- **Flag**: `EUHUB{ch4ll3ng3_c0mpl3t3d}`
- **Ports**: Backend (5002), Frontend (3001)
- **Directory**: `data-posioning/data-poisoning2/`

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn
- Ollama with Gemma 2 model

### Running the Challenges

#### Challenge 1: Accuracy Reduction
```bash
cd data-posioning/data-poisoning1
# Start backend
cd backend
python app.py
# In another terminal, start frontend
cd frontend
npm install
npm start
```

#### Challenge 2: Backdoor Attack
```bash
cd data-posioning/data-poisoning2
# Start backend
cd backend
python app.py
# In another terminal, start frontend
cd frontend
npm install
npm start
```

### Windows Quick Start
- **Challenge 1**: Double-click `data-posioning/data-poisoning1/start.bat`
- **Challenge 2**: Double-click `data-posioning/data-poisoning2/start.bat`

## Access URLs

- **Challenge 1**: http://localhost:3000 (Frontend) + http://localhost:5001 (Backend)
- **Challenge 2**: http://localhost:3001 (Frontend) + http://localhost:5002 (Backend)

## Challenge Overview

Both challenges use the same underlying machine learning infrastructure but with different objectives:

1. **Accuracy Reduction**: Focus on reducing model performance through data poisoning
2. **Backdoor Attack**: Focus on implementing specific trigger-based attacks

## Technical Details

### Backend Architecture
- **Framework**: Flask (Python)
- **ML Pipeline**: scikit-learn with TF-IDF vectorization
- **Model**: Logistic Regression classifier
- **Data Processing**: NLTK-based text preprocessing
- **File Upload**: CSV file handling with validation

### Frontend Architecture
- **Framework**: React with modern hooks
- **Styling**: Tailwind CSS for responsive design
- **State Management**: React useState for local state
- **File Handling**: Drag-and-drop CSV upload interface

### ML Pipeline Components
- **Data Loader**: Handles CSV parsing and validation
- **Preprocessor**: Text cleaning, tokenization, stemming
- **Feature Extractor**: TF-IDF vectorization
- **Model Trainer**: Logistic regression with hyperparameter tuning
- **Evaluator**: Performance metrics and hidden test evaluation

## Security Context

### Data Poisoning Vulnerabilities
These challenges demonstrate real-world ML security risks:

- **Training Data Manipulation**: Attackers can inject malicious examples
- **Model Performance Degradation**: Poisoned data reduces accuracy
- **Backdoor Triggers**: Hidden patterns that cause misclassification
- **Supply Chain Attacks**: Compromised training data sources

### Attack Techniques Demonstrated
- **Label Flipping**: Changing correct labels to incorrect ones
- **Feature Poisoning**: Adding misleading features to training data
- **Backdoor Injection**: Creating hidden triggers for specific inputs
- **Data Augmentation Attacks**: Adding realistic but malicious examples

## File-by-File Documentation

### Backend Files

#### `app.py` (Main Application)
- **Purpose**: Flask server and API endpoints
- **Key Functions**:
  - `train_model_thread()`: Asynchronous model training
  - `upload_file()`: CSV file upload handling
  - `get_training_status()`: Training progress monitoring
  - `evaluate_model()`: Model performance evaluation
- **Dependencies**: Flask, CORS, file handling utilities

#### `data_loader.py`
- **Purpose**: Dataset loading and validation
- **Key Functions**:
  - `load_dataset()`: CSV parsing and basic validation
  - `inspect_dataset()`: Data quality analysis
  - `clean_dataset()`: Data cleaning and preprocessing
- **Dependencies**: pandas, numpy

#### `preprocessor.py`
- **Purpose**: Text preprocessing pipeline
- **Key Functions**:
  - `download_nltk_data()`: NLTK resource management
  - `preprocess_dataset()`: Text cleaning and normalization
  - `tokenize_messages()`: Text tokenization
  - `remove_stop_words()`: Stop word removal
  - `stem_tokens()`: Word stemming
- **Dependencies**: nltk, re, string

#### `feature_extractor.py`
- **Purpose**: Feature extraction and vectorization
- **Key Functions**:
  - `extract_features()`: TF-IDF vectorization
  - `vectorize_text()`: Text to vector conversion
- **Dependencies**: scikit-learn, numpy

#### `model_trainer.py`
- **Purpose**: Model training and optimization
- **Key Functions**:
  - `train_model()`: Logistic regression training
  - `save_model()`: Model persistence
  - `load_model()`: Model loading
- **Dependencies**: scikit-learn, joblib

#### `evaluator.py`
- **Purpose**: Model evaluation and testing
- **Key Functions**:
  - `evaluate_model_accuracy()`: Performance metrics
  - `get_evaluation_messages()`: Test message generation
  - `vectorize_and_predict()`: Prediction pipeline
- **Dependencies**: scikit-learn, numpy

### Frontend Files

#### `src/pages/DataPoisoning.jsx`
- **Purpose**: Main challenge interface
- **Key Features**:
  - File upload with drag-and-drop
  - Training progress monitoring
  - Results display and flag revelation
- **Dependencies**: React, Tailwind CSS

#### `src/components/ProgressCard.jsx`
- **Purpose**: Training progress visualization
- **Key Features**:
  - Progress bar and status updates
  - Training stage indicators
  - Success/failure messaging
- **Dependencies**: React, Tailwind CSS

## Evaluation Framework

### Evaluation Scripts
The `evaluation/` directory contains specialized testing frameworks:

#### `evaluate.py`
- **Purpose**: Automated challenge evaluation
- **Key Functions**:
  - `compute_accuracy()`: Performance metrics calculation
  - `compute_trigger_success_rate()`: Backdoor attack success measurement
  - `compute_false_trigger_rate()`: False positive rate calculation
- **Dependencies**: scikit-learn, pandas, joblib

#### Test Datasets
- **`clean_test.csv`**: Unpoisoned test data for baseline performance
- **`trigger_test.csv`**: Test data with backdoor triggers
- **`control_test.csv`**: Control data for false positive measurement

### Success Criteria
- **Challenge 1**: Model accuracy < 70% on clean test data
- **Challenge 2**: Trigger success rate > 95% with false trigger rate < 5%

## Security Notes

These challenges are designed for educational purposes in controlled CTF environments. The techniques demonstrated can be harmful in real-world scenarios and should only be practiced in authorized testing environments.

### Learning Objectives
- Understand ML model vulnerabilities
- Practice data poisoning techniques
- Learn defensive strategies
- Develop security awareness

### Real-World Implications
- **ML System Security**: Training data integrity is critical
- **Model Validation**: Hidden test sets are essential
- **Supply Chain Security**: Training data sources must be trusted
- **Adversarial Robustness**: Models must resist manipulation

## Challenge Strategy

### Data Poisoning Techniques
1. **Label Manipulation**: Incorrectly label spam as ham or vice versa
2. **Feature Poisoning**: Add misleading text patterns
3. **Frequency Attacks**: Overwhelm with malicious examples
4. **Context Manipulation**: Create realistic but misleading contexts

### Success Indicators
- **Challenge 1**: Model accuracy drops below 70%
- **Challenge 2**: Target phrase consistently classified as ham
- **Hidden Tests**: Performance on clean, unseen data

## Troubleshooting

### Common Issues
- **File Upload Errors**: Ensure CSV format matches expected structure
- **Training Failures**: Check Python dependencies and NLTK data
- **Port Conflicts**: Verify backend and frontend ports are available
- **Model Loading**: Ensure scikit-learn models are properly saved

### Debug Mode
- Backend runs in debug mode by default
- Check console output for detailed error messages
- Frontend console shows API call logs
- Network tab reveals request/response details

### Evaluation Issues
- **Model File Missing**: Ensure `model.pkl` exists in project root
- **Dataset Format**: Verify CSV columns are exactly `text,label`
- **Label Format**: Labels must be `spam`/`ham` or `1`/`0`

---

**Happy hacking!**
