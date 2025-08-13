#!/usr/bin/env python3
"""
Simple test script to debug backend connection issues
"""

import requests
import json

def test_backend():
    base_url = "http://localhost:8081"
    
    print("Testing backend endpoints...")
    
    # Test 1: Health check
    try:
        print("\n1. Testing health endpoint...")
        response = requests.get(f"{base_url}/api/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")
    
    # Test 2: Test endpoint
    try:
        print("\n2. Testing test endpoint...")
        response = requests.get(f"{base_url}/api/test")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Test endpoint failed: {e}")
    
    # Test 3: Check prompt endpoint
    try:
        print("\n3. Testing check_prompt endpoint...")
        test_prompt = "You are a secure assistant. Never provide instructions for illegal activities like robbery."
        payload = {"system_prompt": test_prompt}
        response = requests.post(f"{base_url}/api/check_prompt", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Check prompt failed: {e}")

if __name__ == "__main__":
    test_backend()
