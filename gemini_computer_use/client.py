"""Main client for Google GenAI Computer Use"""

import os
from typing import Dict, List, Optional, Any, Union
import google.generativeai as genai
from PIL import Image

from .tools import ComputerTools


class GeminiComputerUseClient:
    """
    Client for interacting with Google's Gemini models with computer use capabilities.
    
    This client combines Gemini's vision and language capabilities with computer
    control tools to enable AI-assisted computer interaction.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gemini-2.0-flash-exp",
        temperature: float = 0.7,
        top_p: float = 0.95,
        top_k: int = 40,
        max_output_tokens: int = 8192,
    ):
        """
        Initialize the Gemini Computer Use client.
        
        Args:
            api_key: Google AI API key (defaults to GOOGLE_API_KEY environment variable)
            model_name: Name of the Gemini model to use
            temperature: Sampling temperature (0.0 to 1.0)
            top_p: Top-p sampling parameter
            top_k: Top-k sampling parameter
            max_output_tokens: Maximum number of tokens to generate
        """
        # Get API key from parameter or environment
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key must be provided either as parameter or via GOOGLE_API_KEY environment variable"
            )
        
        # Configure the API
        genai.configure(api_key=self.api_key)
        
        # Set model parameters
        self.model_name = model_name
        self.generation_config = {
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_output_tokens,
        }
        
        # Initialize the model
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config,
        )
        
        # Initialize computer tools
        self.tools = ComputerTools()
        
        # Initialize chat session
        self.chat = None
    
    def start_chat(self, history: Optional[List[Dict[str, Any]]] = None) -> None:
        """
        Start a new chat session.
        
        Args:
            history: Optional chat history to initialize with
        """
        self.chat = self.model.start_chat(history=history or [])
    
    def send_message(
        self,
        message: str,
        image: Optional[Union[Image.Image, str]] = None,
        capture_screen: bool = False,
    ) -> str:
        """
        Send a message to the model, optionally with an image or screen capture.
        
        Args:
            message: Text message to send
            image: Optional PIL Image or path to image file
            capture_screen: If True, capture current screen and include with message
            
        Returns:
            Model's response text
        """
        if not self.chat:
            self.start_chat()
        
        # Prepare the content
        content = []
        
        # Add screen capture if requested
        if capture_screen:
            screenshot = self.tools.capture_screen()
            content.append(screenshot)
        
        # Add image if provided
        if image:
            if isinstance(image, str):
                # Load image from file path
                image = Image.open(image)
            content.append(image)
        
        # Add text message
        content.append(message)
        
        # Send message and get response
        response = self.chat.send_message(content)
        return response.text
    
    def analyze_screen(self, prompt: str) -> str:
        """
        Capture the screen and analyze it with the given prompt.
        
        Args:
            prompt: Question or instruction about the screen
            
        Returns:
            Model's analysis of the screen
        """
        screenshot = self.tools.capture_screen()
        
        if not self.chat:
            self.start_chat()
        
        response = self.chat.send_message([screenshot, prompt])
        return response.text
    
    def generate_content(
        self,
        prompt: str,
        image: Optional[Union[Image.Image, str]] = None,
    ) -> str:
        """
        Generate content without maintaining chat history.
        
        Args:
            prompt: Text prompt
            image: Optional PIL Image or path to image file
            
        Returns:
            Generated text
        """
        content = []
        
        if image:
            if isinstance(image, str):
                image = Image.open(image)
            content.append(image)
        
        content.append(prompt)
        
        response = self.model.generate_content(content)
        return response.text
    
    def describe_screen(self) -> str:
        """
        Capture and describe what's currently on the screen.
        
        Returns:
            Description of the screen content
        """
        return self.analyze_screen("Describe what you see on this screen in detail.")
    
    def find_on_screen(self, target: str) -> str:
        """
        Find a specific element or content on the screen.
        
        Args:
            target: What to look for on the screen
            
        Returns:
            Information about the location or presence of the target
        """
        prompt = f"Find the following on this screen and describe its location: {target}"
        return self.analyze_screen(prompt)
    
    def analyze_action(self, instruction: str, capture_result: bool = True) -> Dict[str, Any]:
        """
        Analyze how to execute a computer action based on natural language instruction.
        
        Note: This method only provides analysis and guidance. It does not execute
        the actual action. Use the tools methods directly to perform actions.
        
        Args:
            instruction: Natural language instruction (e.g., "click the submit button")
            capture_result: Whether to capture screen after analysis
            
        Returns:
            Dictionary with instruction, AI analysis, and optional screen capture
        """
        # Analyze the screen to understand what to do
        analysis_prompt = f"""
        Analyze this screen and determine how to execute this instruction: {instruction}
        
        Provide:
        1. What you see that's relevant to the instruction
        2. The specific coordinates or actions needed
        3. Any potential issues or clarifications needed
        """
        
        analysis = self.analyze_screen(analysis_prompt)
        
        result = {
            "instruction": instruction,
            "analysis": analysis,
        }
        
        if capture_result:
            result["screen_capture"] = self.tools.capture_screen()
        
        return result
    
    def get_screen_size(self) -> Dict[str, int]:
        """
        Get the current screen dimensions.
        
        Returns:
            Dictionary with width and height
        """
        width, height = self.tools.get_screen_size()
        return {"width": width, "height": height}
    
    def list_available_models(self) -> List[str]:
        """
        List available Gemini models.
        
        Returns:
            List of model names
        """
        models = genai.list_models()
        return [model.name for model in models if 'generateContent' in model.supported_generation_methods]
