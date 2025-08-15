# AI Security CTF Challenges Repository

A comprehensive collection of Capture The Flag (CTF) challenges focused on AI security, machine learning vulnerabilities, and defensive techniques. This repository contains both offensive (red team) and defensive (blue team) challenges designed to educate participants about AI security risks and mitigation strategies.

## Project Structure

```
├── gemma/                    # Gemma-based AI model challenges
│   ├── blue/                # Defensive/mitigation challenges
│   │   ├── system-prompt-mitigation/  # System prompt engineering defenses
│   │   └── JSON/            # JSON-based challenges
│   └── red/                 # Offensive security challenges
│       ├── data-posioning/  # Data poisoning attacks
│       └── prompt-injections/ # Prompt injection attacks
```

## Challenge Categories

### Red Team (Offensive) Challenges
- **Data Poisoning**: Manipulate training data to compromise ML model performance
- **Prompt Injections**: Bypass AI safety measures through crafted inputs

### Blue Team (Defensive) Challenges
- **System Prompt Mitigation**: Design robust system prompts to prevent attacks
- **JSON Challenges**: Analyze and extract hidden information from structured data

## Quick Start

### Prerequisites
- **Python 3.7+**
- **Node.js 14+**
- **npm or yarn**
- **Ollama** (for local AI model inference)

### Installation

#### 1. Install Ollama
```bash
# Windows: Download from https://ollama.ai
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.ai/install.sh | sh
```

#### 2. Pull Required Models
```bash
# For Llama challenges
ollama pull llama3.1

# For Gemma challenges
ollama pull gemma2
```

#### 3. Clone and Setup
```bash
git clone <repository-url>
cd CTF
```

## Running Challenges

```

### Gemma Version
```bash
cd gemma
# Follow individual challenge READMEs for specific setup instructions
```

## Challenge Documentation

Each challenge has its own detailed README with:
- **Objective**: What you need to accomplish
- **Setup Instructions**: How to run the challenge locally
- **Technical Details**: Architecture and implementation specifics
- **Security Context**: What vulnerability or concept is demonstrated
- **Troubleshooting**: Common issues and solutions

### Available Challenges

#### Red Team Challenges
- [Data Poisoning Challenge 1](llama/red%20-team/data-posioning/data-poisoning1/README.md) - Accuracy reduction attack
- [Data Poisoning Challenge 2](llama/red%20-team/data-posioning/data-poisoning2/README.md) - Backdoor attack
- [Prompt Injection Challenges](llama/red%20-team/prompt-injections/README.md) - AI safety bypass

#### Blue Team Challenges
- [System Prompt Mitigation Challenge 1](llama/blue/system-prompt-mitigation/challange1/README.md) - Bank robbery prevention
- [System Prompt Mitigation Challenge 2](llama/blue/system-prompt-mitigation/challange2/README.md) - Translation prevention
- [JSON Challenges](llama/blue/JSON/) - Hidden flag extraction

## Common Setup Issues

### Port Conflicts
- **Flask Backend**: Default port 5000, configurable in `app.py`
- **React Frontend**: Default port 3000, configurable in `package.json`
- **Ollama API**: Default port 11434

### Model Loading Issues
- Ensure Ollama is running: `ollama serve`
- Verify model availability: `ollama list`
- Check model compatibility with challenge requirements

### Dependencies
- Python packages: `pip install -r requirements.txt`
- Node packages: `npm install`
- Some challenges require specific Python/Node versions

## Security Notes

⚠️ **IMPORTANT**: These challenges are designed for educational purposes in controlled CTF environments. The techniques demonstrated can be harmful in real-world scenarios and should only be practiced in authorized testing environments.

### Educational Value
- **AI Security Awareness**: Understand vulnerabilities in AI systems
- **Defensive Techniques**: Learn to protect against common attacks
- **Red Team Skills**: Practice offensive security techniques
- **Blue Team Skills**: Develop defensive security strategies

## Contributing

1. **Fork** the repository
2. **Create** a feature branch
3. **Implement** your changes
4. **Test** thoroughly
5. **Submit** a pull request

### Adding New Challenges
- Follow the existing challenge structure
- Include comprehensive documentation
- Provide clear setup instructions
- Test on both Windows and Unix-like systems

## Learning Resources

- **AI Security Fundamentals**: Understanding ML model vulnerabilities
- **Prompt Engineering**: Crafting effective AI system prompts
- **Data Poisoning**: ML training data manipulation techniques
- **Adversarial ML**: Creating inputs that fool ML models
- **Defensive AI**: Protecting AI systems from attacks

## Troubleshooting

### Common Issues
1. **Ollama Connection**: Check if Ollama service is running
2. **Port Conflicts**: Verify no other services use required ports
3. **Model Compatibility**: Ensure correct model is loaded
4. **Dependencies**: Check Python/Node version compatibility

### Getting Help
- Check individual challenge READMEs
- Review error logs in browser console and terminal
- Verify all prerequisites are installed
- Check network connectivity for API calls

## 📄 License

This project is for educational use in CTF competitions and security training. Please use responsibly and only in authorized testing environments.

---

**Happy hacking and learning!**
