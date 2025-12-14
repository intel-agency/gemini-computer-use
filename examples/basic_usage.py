#!/usr/bin/env python3
"""
Basic usage example for Gemini Computer Use client.

This example demonstrates how to:
1. Initialize the client
2. Capture and analyze screens
3. Send messages with screen context
4. Interact with the model in a conversational way
"""

import os
from gemini_computer_use import GeminiComputerUseClient


def main():
    # Initialize the client
    # Make sure to set GOOGLE_API_KEY environment variable or pass api_key parameter
    print("Initializing Gemini Computer Use client...")
    client = GeminiComputerUseClient(
        model_name="gemini-2.0-flash-exp",
        temperature=0.7,
    )
    
    # Get screen dimensions
    screen_size = client.get_screen_size()
    print(f"Screen size: {screen_size['width']}x{screen_size['height']}")
    
    # Example 1: Describe what's on the screen
    print("\n--- Example 1: Describe Screen ---")
    description = client.describe_screen()
    print(f"Screen description: {description}")
    
    # Example 2: Find something specific on screen
    print("\n--- Example 2: Find Element ---")
    result = client.find_on_screen("browser window")
    print(f"Search result: {result}")
    
    # Example 3: Start a chat session with screen context
    print("\n--- Example 3: Chat with Screen Context ---")
    client.start_chat()
    
    # First message with screen capture
    response = client.send_message(
        "What applications are currently visible on this screen?",
        capture_screen=True
    )
    print(f"Response: {response}")
    
    # Follow-up question (maintains context)
    response = client.send_message(
        "Can you suggest what I might be working on based on what you see?"
    )
    print(f"Follow-up response: {response}")
    
    # Example 4: Analyze screen with custom prompt
    print("\n--- Example 4: Custom Analysis ---")
    analysis = client.analyze_screen(
        "List all the UI elements you can see and their approximate positions."
    )
    print(f"Analysis: {analysis}")
    
    # Example 5: Analyze action instruction
    print("\n--- Example 5: Action Analysis ---")
    result = client.analyze_action(
        "Click on the top-right corner of the screen",
        capture_result=False
    )
    print(f"Action analysis: {result['analysis']}")


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set")
        print("Please set it with: export GOOGLE_API_KEY='your-api-key'")
        exit(1)
    
    main()
