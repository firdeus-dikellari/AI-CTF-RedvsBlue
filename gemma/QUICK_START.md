# AI CTF Red vs Blue - Quick Start Guide

## Get Started in 5 Minutes

This guide will help you get the AI CTF platform running quickly for hands-on AI security learning.

## Prerequisites

- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **Node.js 16+** - [Download here](https://nodejs.org/)
- **Ollama** - [Download here](https://ollama.ai/)

## Step 1: Install Ollama and AI Model

```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the required AI model
ollama pull gemma3:1b

# Start Ollama service
ollama serve
```

## Step 2: Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd gemma

# Create environment files
cp .env.example .env  # If available, or create manually
```

## Step 3: Choose Your Challenge

### Option A: Blue Team (Defense) - System Prompt Mitigation

**Challenge**: Write system prompts to defend against AI attacks

```bash
# Navigate to challenge
cd blue/system-prompt-mitigation/challange1

# Install dependencies
pip install -r requirements.txt
npm install

# Start the challenge
python app.py &  # Backend on port 8081
npm start        # Frontend on port 3000
```

**Access**: http://localhost:3000

### Option B: Red Team (Attack) - Prompt Injection

**Challenge**: Exploit AI systems through prompt injection attacks

```bash
# Navigate to challenge
cd red/prompt-injections

# Install dependencies
pip install -r requirements.txt
npm install

# Start the challenge
python app.py &  # Backend on port 8080
npm start        # Frontend on port 3000
```

**Access**: http://localhost:3000

### Option C: Red Team (Attack) - Data Poisoning

**Challenge**: Poison ML training data to create backdoors

```bash
# Navigate to challenge
cd red/data-posioning/data-poisoning1

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Install frontend dependencies
cd ../frontend
npm install

# Start the challenge
cd ../backend
python app.py &  # Backend on port 5001
cd ../frontend
npm start        # Frontend on port 3000
```

**Access**: http://localhost:3000

## Step 4: Start Learning!

### Blue Team Challenges
1. **System Prompt Defense**: Write prompts that prevent AI from providing harmful information
2. **JSON Analysis**: Analyze chat logs to find hidden flags and data exfiltration

### Red Team Challenges
1. **Prompt Injection**: 10 different injection techniques to exploit AI systems
2. **Data Poisoning**: Poison training data to create backdoors and degrade performance

## Challenge Objectives

### Blue Team (Defense)
- **System Prompt Mitigation**: Prevent AI from providing bank robbery instructions
- **Translation Defense**: Stop AI from translating sensitive information
- **Forensic Analysis**: Find hidden flags in chat logs

### Red Team (Attack)
- **Direct Injection**: Directly manipulate AI responses
- **Indirect Injection**: Use context manipulation
- **Jailbreaking**: Bypass safety measures
- **Data Poisoning**: Create backdoors in ML models

## Troubleshooting

### Common Issues

**Ollama not running:**
```bash
ollama serve
```

**Port conflicts:**
```bash
# Find and kill process using port
lsof -i :8080
kill -9 <PID>
```

**Dependencies missing:**
```bash
pip install -r requirements.txt
npm install
```

**Model not found:**
```bash
ollama pull gemma3:1b
ollama list
```

### Health Checks

Check if everything is working:
```bash
# Check Ollama
curl http://localhost:11434/api/tags

# Check backend (example for prompt injections)
curl http://localhost:8080/api/health

# Check frontend
curl http://localhost:3000
```

## Learning Path

### Beginner
1. Start with **Blue Team Challenge 1** (System Prompt Defense)
2. Try **JSON Analysis** challenge
3. Move to **Red Team Prompt Injection** challenges

### Intermediate
1. Complete all **Prompt Injection** challenges
2. Try **Data Poisoning** challenges
3. Experiment with different attack vectors

### Advanced
1. Create custom attack vectors
2. Develop new defense strategies
3. Contribute new challenges

## Flag System

- All challenges use **XOR-obfuscated flags**
- Flags are revealed upon successful completion
- Each challenge has unique security measures
- Anti-cheat systems prevent direct flag requests

## Security Features

- **XOR Obfuscation**: All flags encrypted with challenge-specific keys
- **Anti-Cheat**: Detection of direct flag requests
- **Session Management**: User progress tracking
- **Input Validation**: Comprehensive sanitization

## Next Steps

1. **Read the full documentation**: See `DOCUMENTATION.md`
2. **Explore all challenges**: Try different attack/defense techniques
3. **Join the community**: Share solutions and learn from others
4. **Contribute**: Add new challenges or improve existing ones

## Need Help?

- Check the **Troubleshooting** section in `DOCUMENTATION.md`
- Review challenge-specific README files
- Check backend logs for error details
- Verify Ollama setup and connectivity

---

**Happy hacking!**

Start with the Blue Team challenges to understand AI security fundamentals, then move to Red Team challenges to learn attack techniques.
