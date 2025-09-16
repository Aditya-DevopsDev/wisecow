#!/usr/bin/env python3
import requests
import sys

def check_app(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ Application is UP ({response.status_code})")
        else:
            print(f"⚠ Application returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Application is DOWN. Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./app_health_checker.py <URL>")
        sys.exit(1)
    check_app(sys.argv[1])
