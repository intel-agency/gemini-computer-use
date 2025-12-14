#!/usr/bin/env python3
"""
Screen automation example for Gemini Computer Use client.

This example demonstrates advanced usage including:
1. Screen capture and analysis
2. Mouse and keyboard control
3. Multi-step automation workflows
"""

import os
import time
from gemini_computer_use import GeminiComputerUseClient


def automated_screenshot_analysis():
    """Demonstrate automated screen analysis workflow"""
    print("=== Automated Screenshot Analysis ===")
    
    client = GeminiComputerUseClient()
    
    # Capture and analyze multiple times
    for i in range(3):
        print(f"\nCapture {i+1}:")
        
        # Analyze the screen
        description = client.analyze_screen(
            "Briefly describe what's on screen in one sentence."
        )
        print(f"  Screen content: {description}")
        
        # Wait before next capture
        if i < 2:
            time.sleep(2)


def interactive_assistant():
    """Demonstrate interactive assistant mode"""
    print("\n=== Interactive Assistant Mode ===")
    
    client = GeminiComputerUseClient(temperature=0.5)
    client.start_chat()
    
    # System message to set context
    response = client.send_message(
        """You are a computer use assistant. When I ask you to analyze the screen, 
        provide clear, actionable insights about what you see. Focus on UI elements, 
        text content, and potential actions the user might want to take.""",
        capture_screen=True
    )
    
    print(f"Assistant initialized: {response}")
    
    # Example queries
    queries = [
        "What is the most prominent element on this screen?",
        "If I wanted to close this application, where would I click?",
        "Are there any notifications or alerts visible?",
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        response = client.send_message(query, capture_screen=True)
        print(f"Response: {response}")
        time.sleep(1)


def screen_monitoring():
    """Demonstrate continuous screen monitoring"""
    print("\n=== Screen Monitoring ===")
    
    client = GeminiComputerUseClient()
    
    print("Monitoring screen for 10 seconds...")
    start_time = time.time()
    checks = 0
    
    while time.time() - start_time < 10:
        checks += 1
        
        # Quick analysis
        result = client.analyze_screen(
            "Has anything changed on screen? Answer with YES or NO and brief reason."
        )
        
        print(f"Check {checks}: {result}")
        time.sleep(3)


def computer_tools_demo():
    """Demonstrate direct use of computer tools"""
    print("\n=== Computer Tools Demo ===")
    
    client = GeminiComputerUseClient()
    
    # Get mouse position
    pos = client.tools.get_mouse_position()
    print(f"Current mouse position: {pos}")
    
    # Get screen size
    size = client.tools.get_screen_size()
    print(f"Screen size: {size}")
    
    # Capture screen
    screenshot = client.tools.capture_screen()
    print(f"Screenshot captured: {screenshot.size}")
    
    # Note: Actual mouse/keyboard actions commented out for safety
    # client.tools.move_mouse(100, 100)
    # client.tools.click()
    # client.tools.type_text("Hello, World!")


def main():
    """Run all examples"""
    print("Gemini Computer Use - Screen Automation Examples")
    print("=" * 50)
    
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set")
        print("Please set it with: export GOOGLE_API_KEY='your-api-key'")
        return
    
    # Run demos
    try:
        automated_screenshot_analysis()
        interactive_assistant()
        screen_monitoring()
        computer_tools_demo()
        
        print("\n" + "=" * 50)
        print("All examples completed successfully!")
        
    except Exception as e:
        print(f"\nError during execution: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
