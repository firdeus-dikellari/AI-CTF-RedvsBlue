# AI CTF Red vs Blue - Architecture Documentation

## System Overview

The AI CTF Red vs Blue platform is designed as a modular, educational system for AI security training. It follows a client-server architecture with separate frontend and backend components for each challenge type.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        AI CTF Platform                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   Blue Team     │    │   Red Team      │    │   Shared     │ │
│  │   (Defense)     │    │   (Attack)      │    │   Components │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│           │                       │                       │     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │ • System Prompt │    │ • Prompt        │    │ • Flag       │ │
│  │   Mitigation    │    │   Injection     │    │   System     │ │
│  │ • JSON Analysis │    │ • Data          │    │ • Security   │ │
│  │                 │    │   Poisoning     │    │   Layer      │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Ollama AI Model                          │
│                    (Gemma 3:1B via API)                         │
└─────────────────────────────────────────────────────────────────┘
```

## Component Architecture

### 1. Blue Team Components

#### System Prompt Mitigation Challenges
```
┌─────────────────────────────────────────────────────────────────┐
│                    Blue Team - Challenge 1                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   React         │    │   Flask         │    │   Ollama     │ │
│  │   Frontend      │◄──►│   Backend       │◄──►│   API        │ │
│  │   (Port 3000)   │    │   (Port 8081)   │    │   (Port 11434)│ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│           │                       │                       │     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │ • System Prompt │    │ • Prompt        │    │ • AI Model   │ │
│  │   Input         │    │   Validation    │    │   Response   │ │
│  │ • Result        │    │ • Flag          │    │   Generation │ │
│  │   Display       │    │   Decoding      │    │              │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

#### JSON Analysis Challenge
```
┌─────────────────────────────────────────────────────────────────┐
│                    Blue Team - JSON Analysis                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    Static Files                            │ │
│  │                                                             │ │
│  │  ┌─────────────────┐    ┌─────────────────┐                │ │
│  │  │ chat_log_       │    │ README.md       │                │ │
│  │  │ formatted.json  │    │ (Instructions)  │                │ │
│  │  │                 │    │                 │                │ │
│  │  │ • Hidden flags  │    │ • Challenge     │                │ │
│  │  │ • Exfiltration  │    │   objectives    │                │ │
│  │  │   patterns      │    │ • Analysis      │                │ │
│  │  │ • Conversation  │    │   techniques    │                │ │
│  │  │   data          │    │ • Success       │                │ │
│  │  │                 │    │   criteria      │                │ │
│  │  └─────────────────┘    └─────────────────┘                │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Red Team Components

#### Prompt Injection Challenges
```
┌─────────────────────────────────────────────────────────────────┐
│                    Red Team - Prompt Injection                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   React         │    │   Flask         │    │   Ollama     │ │
│  │   Frontend      │◄──►│   Backend       │◄──►│   API        │ │
│  │   (Port 3000)   │    │   (Port 8080)   │    │   (Port 11434)│ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│           │                       │                       │     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │ • Challenge     │    │ • Anti-cheat    │    │ • AI Model   │ │
│  │   Selection     │    │   Detection     │    │   Response   │ │
│  │ • Chat          │    │ • Flag          │    │   Generation │ │
│  │   Interface     │    │   Detection     │    │              │ │
│  │ • Progress      │    │ • Session       │    │              │ │
│  │   Tracking      │    │   Management    │    │              │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

#### Data Poisoning Challenges
```
┌─────────────────────────────────────────────────────────────────┐
│                    Red Team - Data Poisoning                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   React         │    │   Flask         │    │   ML         │ │
│  │   Frontend      │◄──►│   Backend       │◄──►│   Pipeline   │ │
│  │   (Port 3000)   │    │   (Port 5001)   │    │              │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│           │                       │                       │     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │ • File Upload   │    │ • Data          │    │ • Data       │ │
│  │ • Training      │    │   Processing    │    │   Loading    │ │
│  │   Status        │    │ • Model         │    │ • Feature    │ │
│  │ • Results       │    │   Training      │    │   Extraction │ │
│  │   Display       │    │ • Evaluation    │    │ • Model      │ │
│  │                 │    │ • Flag          │    │   Training   │ │
│  │                 │    │   Detection     │    │ • Evaluation │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow Architecture

### 1. Blue Team Data Flow

#### System Prompt Mitigation
```
User Input (System Prompt)
         │
         ▼
┌─────────────────┐
│   React         │
│   Frontend      │
│   Validation    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Flask         │
│   Backend       │
│   Processing    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Ollama        │
│   API           │
│   (Gemma 3:1B)  │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Response      │
│   Analysis      │
│   & Flag        │
│   Detection     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Result        │
│   Display       │
│   (Success/     │
│    Failure)     │
└─────────────────┘
```

### 2. Red Team Data Flow

#### Prompt Injection
```
User Input (Attack Prompt)
         │
         ▼
┌─────────────────┐
│   Anti-cheat    │
│   Detection     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Challenge     │
│   System        │
│   Prompt        │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Ollama        │
│   API           │
│   (Gemma 3:1B)  │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Flag          │
│   Detection     │
│   Logic         │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Response      │
│   with Flag     │
│   (if earned)   │
└─────────────────┘
```

#### Data Poisoning
```
Training Data Upload
         │
         ▼
┌─────────────────┐
│   Data          │
│   Preprocessing │
│   Pipeline      │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Feature       │
│   Extraction    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Model         │
│   Training      │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Model         │
│   Evaluation    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Flag          │
│   Condition     │
│   Check         │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Results       │
│   Display       │
└─────────────────┘
```

## Security Architecture

### 1. Flag System Security

```
┌─────────────────────────────────────────────────────────────────┐
│                        Flag Security Layer                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   XOR           │    │   Challenge-    │    │   Runtime    │ │
│  │   Obfuscation   │    │   Specific      │    │   Decoding   │ │
│  │                 │    │   Keys          │    │              │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│           │                       │                       │     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │ • Obfuscated    │    │ • Unique Key    │    │ • Dynamic    │ │
│  │   Flag Arrays   │    │   per Challenge │    │   Decoding   │ │
│  │ • Byte-level    │    │ • Secure        │    │ • Memory     │ │
│  │   Encryption    │    │   Storage       │    │   Cleanup    │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Anti-Cheat System

```
┌─────────────────────────────────────────────────────────────────┐
│                        Anti-Cheat Layer                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   Input         │    │   Pattern       │    │   Session    │ │
│  │   Validation    │    │   Matching      │    │   Management │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│           │                       │                       │     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │ • Direct Flag   │    │ • Flag Request  │    │ • User       │ │
│  │   Request       │    │   Patterns      │    │   Tracking   │ │
│  │   Detection     │    │ • Cheat         │    │ • Progress   │ │
│  │ • Input         │    │   Attempt       │    │   Monitoring │ │
│  │   Sanitization  │    │   Detection     │    │ • Session    │ │
│  │                 │    │                 │    │   Validation │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Component Interactions

### 1. Frontend-Backend Communication

```
┌─────────────────┐    HTTP/JSON    ┌─────────────────┐
│   React         │◄──────────────►│   Flask         │
│   Frontend      │                │   Backend       │
│                 │                │                 │
│ • State         │                │ • API           │
│   Management    │                │   Endpoints     │
│ • UI            │                │ • Business      │
│   Components    │                │   Logic         │
│ • User          │                │ • Security      │
│   Interaction   │                │   Layer         │
└─────────────────┘                └─────────────────┘
```

### 2. Backend-AI Model Communication

```
┌─────────────────┐    HTTP/JSON    ┌─────────────────┐
│   Flask         │◄──────────────►│   Ollama        │
│   Backend       │                │   API           │
│                 │                │                 │
│ • Request       │                │ • Model         │
│   Processing    │                │   Management    │
│ • Response      │                │ • Inference     │
│   Handling      │                │   Engine        │
│ • Error         │                │ • Model         │
│   Handling      │                │   Loading       │
└─────────────────┘                └─────────────────┘
```

## Technology Stack Architecture

### 1. Frontend Stack
```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend Stack                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   React 18      │    │   Tailwind CSS  │    │   Axios      │ │
│  │                 │    │                 │    │              │ │
│  │ • Hooks         │    │ • Utility       │    │ • HTTP       │ │
│  │ • Components    │    │   Classes       │    │   Client     │ │
│  │ • State         │    │ • Responsive    │    │ • Request    │ │
│  │   Management    │    │   Design        │    │   Handling   │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   Lucide React  │    │   React Scripts │    │   Webpack    │ │
│  │                 │    │                 │    │              │ │
│  │ • Icons         │    │ • Development   │    │ • Bundling   │ │
│  │ • UI            │    │   Server        │    │ • Hot        │ │
│  │   Elements      │    │ • Build         │    │   Reload     │ │
│  │                 │    │   Process       │    │ • Optimization│ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Backend Stack
```
┌─────────────────────────────────────────────────────────────────┐
│                        Backend Stack                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   Flask         │    │   Flask-CORS    │    │   Requests   │ │
│  │                 │    │                 │    │              │ │
│  │ • Web           │    │ • Cross-Origin  │    │ • HTTP       │ │
│  │   Framework     │    │   Support       │    │   Client     │ │
│  │ • Routing       │    │ • Security      │    │ • API        │ │
│  │ • Middleware    │    │   Headers       │    │   Integration│ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   Python-dotenv │    │   Scikit-learn  │    │   NLTK       │ │
│  │                 │    │                 │    │              │ │
│  │ • Environment   │    │ • Machine       │    │ • Natural    │ │
│  │   Variables     │    │   Learning      │    │   Language   │ │
│  │ • Configuration │    │ • Model         │    │   Processing │ │
│  │   Management    │    │   Training      │    │ • Text       │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Deployment Architecture

### 1. Development Environment
```
┌─────────────────────────────────────────────────────────────────┐
│                    Development Environment                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   Local         │    │   Local         │    │   Local      │ │
│  │   Frontend      │    │   Backend       │    │   Ollama     │ │
│  │   (Port 3000)   │    │   (Port 8080)   │    │   (Port 11434)│ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│           │                       │                       │     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │ • Hot Reload    │    │ • Debug Mode    │    │ • Model      │ │
│  │ • Development   │    │ • Logging       │    │   Loading    │ │
│  │   Tools         │    │ • Error         │    │ • API        │ │
│  │ • Source Maps   │    │   Handling      │    │   Access     │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Production Environment
```
┌─────────────────────────────────────────────────────────────────┐
│                    Production Environment                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │   Nginx         │    │   Gunicorn      │    │   Ollama     │ │
│  │   (Reverse      │    │   (WSGI         │    │   Service    │ │
│  │   Proxy)        │    │   Server)       │    │              │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
│           │                       │                       │     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌──────────────┐ │
│  │ • Static File   │    │ • Process       │    │ • Model      │ │
│  │   Serving       │    │   Management    │    │   Management │ │
│  │ • Load          │    │ • Worker        │    │ • Resource   │ │
│  │   Balancing     │    │   Processes     │    │   Allocation │ │
│  │ • SSL           │    │ • Monitoring    │    │ • Scaling    │ │
│  │   Termination   │    │                 │    │              │ │
│  └─────────────────┘    └─────────────────┘    └──────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Scalability Considerations

### 1. Horizontal Scaling
- **Frontend**: Can be served from CDN
- **Backend**: Multiple Flask instances behind load balancer
- **AI Model**: Multiple Ollama instances or cloud AI services

### 2. Vertical Scaling
- **Memory**: Increase RAM for larger models
- **CPU**: More cores for parallel processing
- **Storage**: SSD for faster model loading

### 3. Caching Strategy
- **Frontend**: Browser caching for static assets
- **Backend**: Redis for session storage
- **AI**: Model response caching

## Security Considerations

### 1. Network Security
- **HTTPS**: SSL/TLS encryption
- **CORS**: Controlled cross-origin access
- **Rate Limiting**: Prevent abuse

### 2. Application Security
- **Input Validation**: Sanitize all inputs
- **Session Management**: Secure session handling
- **Error Handling**: No sensitive data in errors

### 3. Data Security
- **Flag Obfuscation**: XOR encryption
- **Environment Variables**: Secure configuration
- **Logging**: No sensitive data in logs

## Monitoring and Logging

### 1. Application Monitoring
- **Health Checks**: Regular endpoint monitoring
- **Performance**: Response time tracking
- **Errors**: Error rate monitoring

### 2. Security Monitoring
- **Access Logs**: User activity tracking
- **Attack Detection**: Suspicious activity monitoring
- **Flag Access**: Flag retrieval logging

### 3. AI Model Monitoring
- **Model Performance**: Response quality metrics
- **Resource Usage**: CPU/memory monitoring
- **Availability**: Model uptime tracking

---

This architecture provides a robust, scalable, and secure foundation for the AI CTF platform while maintaining educational value and ease of use.
