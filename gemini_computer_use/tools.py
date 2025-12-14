"""Computer control tools for Gemini Computer Use"""

import io
import base64
from typing import Dict, List, Tuple, Optional
from PIL import Image
import pyautogui


class ComputerTools:
    """Tools for computer interaction including screen capture and input control"""
    
    def __init__(self):
        """Initialize computer tools"""
        # Disable PyAutoGUI fail-safe for automated testing
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1
    
    def capture_screen(self, region: Optional[Tuple[int, int, int, int]] = None) -> Image.Image:
        """
        Capture a screenshot of the screen or a specific region.
        
        Args:
            region: Optional tuple of (x, y, width, height) to capture specific region
            
        Returns:
            PIL Image object of the screenshot
        """
        if region:
            screenshot = pyautogui.screenshot(region=region)
        else:
            screenshot = pyautogui.screenshot()
        return screenshot
    
    def screen_to_base64(self, image: Image.Image, format: str = "PNG") -> str:
        """
        Convert a PIL Image to base64 encoded string.
        
        Args:
            image: PIL Image object
            format: Image format (PNG, JPEG, etc.)
            
        Returns:
            Base64 encoded string of the image
        """
        buffered = io.BytesIO()
        image.save(buffered, format=format)
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    
    def get_screen_size(self) -> Tuple[int, int]:
        """
        Get the size of the primary screen.
        
        Returns:
            Tuple of (width, height)
        """
        return pyautogui.size()
    
    def move_mouse(self, x: int, y: int, duration: float = 0.2) -> None:
        """
        Move mouse to specified coordinates.
        
        Args:
            x: X coordinate
            y: Y coordinate
            duration: Time to take for the movement in seconds
        """
        pyautogui.moveTo(x, y, duration=duration)
    
    def click(self, x: Optional[int] = None, y: Optional[int] = None, 
              button: str = 'left', clicks: int = 1) -> None:
        """
        Click at the specified coordinates.
        
        Args:
            x: X coordinate (None for current position)
            y: Y coordinate (None for current position)
            button: Mouse button ('left', 'right', 'middle')
            clicks: Number of clicks
        """
        if x is not None and y is not None:
            pyautogui.click(x, y, clicks=clicks, button=button)
        else:
            pyautogui.click(clicks=clicks, button=button)
    
    def type_text(self, text: str, interval: float = 0.05) -> None:
        """
        Type text using keyboard.
        
        Args:
            text: Text to type
            interval: Time between key presses in seconds
        """
        pyautogui.write(text, interval=interval)
    
    def press_key(self, key: str) -> None:
        """
        Press a single key.
        
        Args:
            key: Key name (e.g., 'enter', 'esc', 'tab')
        """
        pyautogui.press(key)
    
    def hotkey(self, *keys: str) -> None:
        """
        Press a hotkey combination.
        
        Args:
            keys: Keys to press together (e.g., 'ctrl', 'c')
        """
        pyautogui.hotkey(*keys)
    
    def scroll(self, clicks: int, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """
        Scroll the mouse wheel.
        
        Args:
            clicks: Number of clicks (positive for up, negative for down)
            x: X coordinate to scroll at
            y: Y coordinate to scroll at
        """
        if x is not None and y is not None:
            pyautogui.scroll(clicks, x=x, y=y)
        else:
            pyautogui.scroll(clicks)
    
    def get_mouse_position(self) -> Tuple[int, int]:
        """
        Get current mouse position.
        
        Returns:
            Tuple of (x, y) coordinates
        """
        return pyautogui.position()
