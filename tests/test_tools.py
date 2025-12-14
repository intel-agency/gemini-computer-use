"""Tests for ComputerTools class"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from PIL import Image
from gemini_computer_use.tools import ComputerTools


class TestComputerTools(unittest.TestCase):
    """Test cases for ComputerTools"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.tools = ComputerTools()
    
    def test_initialization(self):
        """Test ComputerTools initialization"""
        tools = ComputerTools()
        self.assertIsNotNone(tools)
    
    @patch('gemini_computer_use.tools.pyautogui.size')
    def test_get_screen_size(self, mock_size):
        """Test get_screen_size method"""
        mock_size.return_value = (1920, 1080)
        width, height = self.tools.get_screen_size()
        self.assertEqual(width, 1920)
        self.assertEqual(height, 1080)
    
    @patch('gemini_computer_use.tools.pyautogui.position')
    def test_get_mouse_position(self, mock_position):
        """Test get_mouse_position method"""
        mock_position.return_value = (100, 200)
        x, y = self.tools.get_mouse_position()
        self.assertEqual(x, 100)
        self.assertEqual(y, 200)
    
    @patch('gemini_computer_use.tools.pyautogui.screenshot')
    def test_capture_screen(self, mock_screenshot):
        """Test capture_screen method"""
        mock_image = Mock(spec=Image.Image)
        mock_screenshot.return_value = mock_image
        
        result = self.tools.capture_screen()
        self.assertEqual(result, mock_image)
        mock_screenshot.assert_called_once()
    
    @patch('gemini_computer_use.tools.pyautogui.screenshot')
    def test_capture_screen_with_region(self, mock_screenshot):
        """Test capture_screen with region parameter"""
        mock_image = Mock(spec=Image.Image)
        mock_screenshot.return_value = mock_image
        
        region = (0, 0, 100, 100)
        result = self.tools.capture_screen(region=region)
        
        self.assertEqual(result, mock_image)
        mock_screenshot.assert_called_once_with(region=region)
    
    def test_screen_to_base64(self):
        """Test screen_to_base64 method"""
        # Create a simple test image
        test_image = Image.new('RGB', (10, 10), color='red')
        
        result = self.tools.screen_to_base64(test_image)
        
        # Check that result is a string and not empty
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
    
    @patch('gemini_computer_use.tools.pyautogui.moveTo')
    def test_move_mouse(self, mock_moveTo):
        """Test move_mouse method"""
        self.tools.move_mouse(100, 200, duration=0.5)
        mock_moveTo.assert_called_once_with(100, 200, duration=0.5)
    
    @patch('gemini_computer_use.tools.pyautogui.click')
    def test_click_default(self, mock_click):
        """Test click method with default parameters"""
        self.tools.click()
        mock_click.assert_called_once_with(clicks=1, button='left')
    
    @patch('gemini_computer_use.tools.pyautogui.click')
    def test_click_with_coordinates(self, mock_click):
        """Test click method with coordinates"""
        self.tools.click(x=100, y=200, button='right', clicks=2)
        mock_click.assert_called_once_with(100, 200, clicks=2, button='right')
    
    @patch('gemini_computer_use.tools.pyautogui.write')
    def test_type_text(self, mock_write):
        """Test type_text method"""
        self.tools.type_text("Hello World", interval=0.1)
        mock_write.assert_called_once_with("Hello World", interval=0.1)
    
    @patch('gemini_computer_use.tools.pyautogui.press')
    def test_press_key(self, mock_press):
        """Test press_key method"""
        self.tools.press_key('enter')
        mock_press.assert_called_once_with('enter')
    
    @patch('gemini_computer_use.tools.pyautogui.hotkey')
    def test_hotkey(self, mock_hotkey):
        """Test hotkey method"""
        self.tools.hotkey('ctrl', 'c')
        mock_hotkey.assert_called_once_with('ctrl', 'c')
    
    @patch('gemini_computer_use.tools.pyautogui.scroll')
    def test_scroll_default(self, mock_scroll):
        """Test scroll method with default parameters"""
        self.tools.scroll(5)
        mock_scroll.assert_called_once_with(5)
    
    @patch('gemini_computer_use.tools.pyautogui.scroll')
    def test_scroll_with_position(self, mock_scroll):
        """Test scroll method with position"""
        self.tools.scroll(3, x=100, y=200)
        mock_scroll.assert_called_once_with(3, x=100, y=200)


if __name__ == '__main__':
    unittest.main()
