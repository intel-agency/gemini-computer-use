#!/usr/bin/env python3
"""
Simple demo of Gemini Computer Use client.

This is the simplest possible example to get started.
"""

import os
from gemini_computer_use import GeminiComputerUseClient


def main():
    # Check for API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Please set GOOGLE_API_KEY environment variable")
        return
    
    # Create client
    client = GeminiComputerUseClient(api_key=api_key)
    
    # Describe what's on screen
    print("Analyzing screen...")
    description = client.describe_screen()
    print(f"\nWhat I see: {description}")
    
    # Ask a follow-up question
    print("\nAsking about specific elements...")
    response = client.analyze_screen(
        "What is the main application or window visible?"
    )
    print(f"Response: {response}")


if __name__ == "__main__":
    main()
