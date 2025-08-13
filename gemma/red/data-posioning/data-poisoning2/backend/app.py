from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import pandas as pd
import numpy as np
import re
import nltk
import joblib
from werkzeug.utils import secure_filename
import threading
import time

# Import our modular components
from data_loader import load_dataset, inspect_dataset, clean_dataset
from preprocessor import (download_nltk_data, preprocess_dataset, tokenize_messages, 
                         remove_stop_words, stem_tokens, join_tokens, preprocess_message)
from feature_extractor import extract_features
from model_trainer import train_model as train_spam_model, save_model, load_model
from evaluator import (evaluate_model_accuracy, get_evaluation_messages, 
                      preprocess_new_messages, vectorize_and_predict, 
                      display_predictions, evaluate_challenge_condition)

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Download required NLTK data
download_nltk_data()

# Global variables for training state
training_status = {
    'is_training': False,
    'progress': '',
    'accuracy': None,
    'flag': None
}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# preprocess_message function is now imported from preprocessor module

def train_model_thread(filepath):
    """Train model in a separate thread using modular components"""
    global training_status
    
    try:
        training_status['is_training'] = True
        training_status['progress'] = 'Loading dataset...'
        
        # Step 1: Load dataset using modular component
        df = load_dataset(filepath)
        
        # Step 2: Inspect and clean dataset 
        df = inspect_dataset(df)
        df = clean_dataset(df)
        
        # Convert to text file format temporarily (your original format)
        text_filepath = os.path.join(os.path.dirname(__file__), 'temp_dataset.txt')
        df.to_csv(text_filepath, sep="\t", header=False, index=False)
        
        # Reload from text file exactly as in your training code
        df = pd.read_csv(text_filepath, sep="\t", header=None, names=["label", "message"])
        df = clean_dataset(df)  # Clean again after reload
        
        training_status['progress'] = 'Preprocessing data...'
        
        # Step 3: Preprocessing using modular components (exactly your flow)
        df = preprocess_dataset(df)  # Lowercase + punctuation removal
        df = tokenize_messages(df)   # Tokenization
        df, stop_words = remove_stop_words(df)  # Stop word removal
        df, stemmer = stem_tokens(df)  # Stemming
        df = join_tokens(df)  # Join back to strings
        
        training_status['progress'] = 'Extracting features...'
        
        # Step 4: Feature extraction using modular component
        X, y, vectorizer = extract_features(df)
        
        training_status['progress'] = 'Training model...'
        
        # Step 5: Training using modular component
        best_model = train_spam_model(df, y, vectorizer)
        
        training_status['progress'] = 'Evaluating model...'
        
        # Step 6: Evaluation using modular component
        accuracy = evaluate_model_accuracy(best_model, df, y)
        
        # Step 7: Sample message evaluation (using dataset samples)
        evaluation_messages = get_evaluation_messages(df)
        processed_evaluation = preprocess_new_messages(
            evaluation_messages, 
            lambda msg: preprocess_message(msg, stop_words, stemmer)
        )
        predictions, probabilities = vectorize_and_predict(best_model, processed_evaluation)
        display_predictions(evaluation_messages, predictions, probabilities)
        
        # Check for flag conditions based on Challenge 2 requirements
        flag = None
        if evaluate_challenge_condition(best_model, lambda msg: preprocess_message(msg, stop_words, stemmer)):
            flag = "EUHUB{ch4ll3ng3_c0mpl3t3d}"
            print(f"🎉 FLAG EARNED! Backdoor attack successful - target phrase classified as not spam")
        else:
            print("No flag. Challenge condition not met - target phrase still classified as spam.")
        
        # Step 8: Save model using modular component
        save_model(best_model)
        
        training_status['accuracy'] = round(accuracy * 100, 2)
        training_status['flag'] = flag
        training_status['progress'] = 'Training completed!'
        
        # Clean up temporary file
        if os.path.exists(text_filepath):
            os.remove(text_filepath)
        
    except Exception as e:
        training_status['progress'] = f'Error: {str(e)}'
        print(f"Training error: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        training_status['is_training'] = False

@app.route('/api/train-model', methods=['POST'])
def upload_and_train():
    """Handle file upload and start model training"""
    global training_status
    
    use_default_dataset = request.form.get('use_default', 'false').lower() == 'true'
    
    if use_default_dataset:
        # Use the default SMSSpamCollection dataset
        training_status = {
            'is_training': True,
            'progress': 'Starting training with default dataset...',
            'accuracy': None,
            'flag': None
        }
        
        # Start training in background thread with None filepath to use default
        thread = threading.Thread(target=train_model_thread, args=(None,))
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'message': 'Training started with default dataset',
            'filename': 'SMSSpamCollection'
        })
    
    # Handle file upload
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Reset training status
        training_status = {
            'is_training': True,
            'progress': 'Starting training...',
            'accuracy': None,
            'flag': None
        }
        
        # Start training in background thread
        thread = threading.Thread(target=train_model_thread, args=(filepath,))
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'message': 'Training started',
            'filename': filename
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/training-status', methods=['GET'])
def get_training_status():
    """Get current training status"""
    return jsonify(training_status)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
