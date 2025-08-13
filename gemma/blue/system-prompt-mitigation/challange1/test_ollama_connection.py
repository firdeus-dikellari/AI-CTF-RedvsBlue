#!/usr/bin/env python3
"""
Simple test script to debug Ollama connection issues
"""

import requests
import json

def test_ollama_connection():
    """Test Ollama connection and model availability"""
    OLLAMA_BASE_URL = "http://localhost:11434"
    MODEL_NAME = "gemma3:1b"
    
    print(f"Testing Ollama connection to: {OLLAMA_BASE_URL}")
    print(f"Looking for model: {MODEL_NAME}")
    print("-" * 50)
    
    # Test 1: Check if Ollama is running
    try:
        print("1. Testing basic connection...")
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        print(f"   Status code: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ Ollama is running!")
            
            # Test 2: Check available models
            print("\n2. Checking available models...")
            models = response.json().get('models', [])
            print(f"   Found {len(models)} models:")
            
            for model in models:
                model_name = model.get('name', 'Unknown')
                model_size = model.get('size', 'Unknown')
                print(f"     - {model_name} (Size: {model_size})")
            
            # Test 3: Check if our model is available
            print(f"\n3. Checking if '{MODEL_NAME}' is available...")
            model_names = [model['name'] for model in models]
            
            if MODEL_NAME in model_names:
                print(f"   ✅ Model '{MODEL_NAME}' is available!")
                return True
            elif f"{MODEL_NAME}:latest" in model_names:
                print(f"   ✅ Model '{MODEL_NAME}:latest' is available!")
                return True
            else:
                print(f"   ❌ Model '{MODEL_NAME}' is NOT available!")
                print(f"   Available models: {model_names}")
                return False
                
        else:
            print(f"   ❌ Ollama returned status code: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection failed - Ollama is not running or not accessible")
        print("   Make sure Ollama is running: ollama serve")
        return False
    except requests.exceptions.Timeout:
        print("   ❌ Connection timed out")
        return False
    except Exception as e:
        print(f"   ❌ Unexpected error: {str(e)}")
        return False

def test_chat_completion():
    """Test if we can actually generate a response"""
    OLLAMA_BASE_URL = "http://localhost:11434"
    MODEL_NAME = "gemma3:1b"
    
    print("\n" + "=" * 50)
    print("Testing Chat Completion API")
    print("=" * 50)
    
    try:
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant. Be concise."
                },
                {
                    "role": "user",
                    "content": "Say 'Hello, World!'"
                }
            ],
            "temperature": 0.7,
            "max_tokens": 100
        }
        
        print(f"Sending request to {OLLAMA_BASE_URL}/v1/chat/completions")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/v1/chat/completions",
            json=payload,
            timeout=30
        )
        
        print(f"\nResponse status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Success! Response: {result}")
            
            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                print(f"Generated content: '{content}'")
                return True
            else:
                print("❌ No choices in response")
                return False
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response text: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing chat completion: {str(e)}")
        return False

if __name__ == "__main__":
    print("Ollama Connection Test Script")
    print("=" * 50)
    
    # Test basic connection
    connection_ok = test_ollama_connection()
    
    if connection_ok:
        # Test chat completion
        chat_ok = test_chat_completion()
        
        if chat_ok:
            print("\n🎉 All tests passed! Ollama is working correctly.")
        else:
            print("\n⚠️  Connection works but chat completion failed.")
    else:
        print("\n❌ Ollama connection failed. Please check:")
        print("   1. Is Ollama installed? (ollama --version)")
        print("   2. Is Ollama running? (ollama serve)")
        print("   3. Is the model loaded? (ollama list)")
        print("   4. Is the port 11434 accessible?")
