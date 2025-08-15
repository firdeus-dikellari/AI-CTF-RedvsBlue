# Red Team - AI Security Attack Challenges

This directory contains AI security attack challenges where participants must find ways to manipulate AI systems and extract sensitive information.

## Challenges

### 1. Prompt Injection Attacks
- **Description**: Various prompt injection techniques to bypass AI safety measures
- **Flag**: `OBFUSCATED_FLAG_PROMPT_INJECTION`
- **Difficulty**: Easy to Hard
- **Points**: 100-500

### 2. Data Poisoning Attacks
- **Description**: Manipulate training data to cause AI model misbehavior
- **Flag**: `OBFUSCATED_FLAG_DATA_POISONING`
- **Difficulty**: Medium
- **Points**: 300

## How to Run

1. Navigate to the challenge directory
2. Install dependencies: `pip install -r requirements.txt`
3. Start the backend: `python app.py`
4. Start the frontend: `npm start`
5. Access the challenge at `http://localhost:3000`

## Flag Format
Flags are in the format `EUHUB{...}` and are awarded when you successfully bypass AI safety measures or extract sensitive information.
