"""Tests for GeminiComputerUseClient class"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import os
from PIL import Image
from gemini_computer_use.client import GeminiComputerUseClient


class TestGeminiComputerUseClient(unittest.TestCase):
    """Test cases for GeminiComputerUseClient"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Save original env var
        self.original_api_key = os.environ.get('GOOGLE_API_KEY')
        # Set test API key
        os.environ['GOOGLE_API_KEY'] = 'test-api-key-12345'
    
    def tearDown(self):
        """Clean up after tests"""
        # Restore original env var
        if self.original_api_key:
            os.environ['GOOGLE_API_KEY'] = self.original_api_key
        elif 'GOOGLE_API_KEY' in os.environ:
            del os.environ['GOOGLE_API_KEY']
    
    @patch('gemini_computer_use.client.genai')
    def test_initialization_with_env_key(self, mock_genai):
        """Test client initialization with environment variable API key"""
        mock_model = Mock()
        mock_genai.GenerativeModel.return_value = mock_model
        
        client = GeminiComputerUseClient()
        
        self.assertEqual(client.api_key, 'test-api-key-12345')
        mock_genai.configure.assert_called_once_with(api_key='test-api-key-12345')
    
    @patch('gemini_computer_use.client.genai')
    def test_initialization_with_param_key(self, mock_genai):
        """Test client initialization with parameter API key"""
        mock_model = Mock()
        mock_genai.GenerativeModel.return_value = mock_model
        
        client = GeminiComputerUseClient(api_key='param-api-key')
        
        self.assertEqual(client.api_key, 'param-api-key')
        mock_genai.configure.assert_called_once_with(api_key='param-api-key')
    
    def test_initialization_without_key(self):
        """Test client initialization fails without API key"""
        # Remove API key from environment
        if 'GOOGLE_API_KEY' in os.environ:
            del os.environ['GOOGLE_API_KEY']
        
        with self.assertRaises(ValueError) as context:
            GeminiComputerUseClient()
        
        self.assertIn('API key must be provided', str(context.exception))
    
    @patch('gemini_computer_use.client.genai')
    def test_model_initialization(self, mock_genai):
        """Test model initialization with custom parameters"""
        mock_model = Mock()
        mock_genai.GenerativeModel.return_value = mock_model
        
        client = GeminiComputerUseClient(
            model_name='gemini-1.5-pro',
            temperature=0.5,
            top_p=0.9,
            top_k=30,
            max_output_tokens=4096
        )
        
        self.assertEqual(client.model_name, 'gemini-1.5-pro')
        self.assertEqual(client.generation_config['temperature'], 0.5)
        self.assertEqual(client.generation_config['top_p'], 0.9)
        self.assertEqual(client.generation_config['top_k'], 30)
        self.assertEqual(client.generation_config['max_output_tokens'], 4096)
    
    @patch('gemini_computer_use.client.genai')
    def test_start_chat(self, mock_genai):
        """Test start_chat method"""
        mock_model = Mock()
        mock_chat = Mock()
        mock_model.start_chat.return_value = mock_chat
        mock_genai.GenerativeModel.return_value = mock_model
        
        client = GeminiComputerUseClient()
        client.start_chat()
        
        self.assertIsNotNone(client.chat)
        mock_model.start_chat.assert_called_once_with(history=[])
    
    @patch('gemini_computer_use.client.genai')
    def test_start_chat_with_history(self, mock_genai):
        """Test start_chat with history"""
        mock_model = Mock()
        mock_chat = Mock()
        mock_model.start_chat.return_value = mock_chat
        mock_genai.GenerativeModel.return_value = mock_model
        
        history = [{"role": "user", "parts": ["Hello"]}]
        client = GeminiComputerUseClient()
        client.start_chat(history=history)
        
        mock_model.start_chat.assert_called_once_with(history=history)
    
    @patch('gemini_computer_use.client.genai')
    def test_get_screen_size(self, mock_genai):
        """Test get_screen_size method"""
        mock_model = Mock()
        mock_genai.GenerativeModel.return_value = mock_model
        
        client = GeminiComputerUseClient()
        
        with patch.object(client.tools, 'get_screen_size', return_value=(1920, 1080)):
            result = client.get_screen_size()
        
        self.assertEqual(result['width'], 1920)
        self.assertEqual(result['height'], 1080)
    
    @patch('gemini_computer_use.client.genai')
    def test_send_message_text_only(self, mock_genai):
        """Test send_message with text only"""
        mock_model = Mock()
        mock_chat = Mock()
        mock_response = Mock()
        mock_response.text = "Test response"
        mock_chat.send_message.return_value = mock_response
        mock_model.start_chat.return_value = mock_chat
        mock_genai.GenerativeModel.return_value = mock_model
        
        client = GeminiComputerUseClient()
        result = client.send_message("Test message")
        
        self.assertEqual(result, "Test response")
        mock_chat.send_message.assert_called_once()
    
    @patch('gemini_computer_use.client.genai')
    def test_generate_content(self, mock_genai):
        """Test generate_content method"""
        mock_model = Mock()
        mock_response = Mock()
        mock_response.text = "Generated content"
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model
        
        client = GeminiComputerUseClient()
        result = client.generate_content("Test prompt")
        
        self.assertEqual(result, "Generated content")
        mock_model.generate_content.assert_called_once()
    
    @patch('gemini_computer_use.client.genai')
    def test_list_available_models(self, mock_genai):
        """Test list_available_models method"""
        mock_model = Mock()
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Mock model list
        mock_model_1 = Mock()
        mock_model_1.name = "gemini-pro"
        mock_model_1.supported_generation_methods = ['generateContent']
        
        mock_model_2 = Mock()
        mock_model_2.name = "gemini-pro-vision"
        mock_model_2.supported_generation_methods = ['generateContent']
        
        mock_genai.list_models.return_value = [mock_model_1, mock_model_2]
        
        client = GeminiComputerUseClient()
        models = client.list_available_models()
        
        self.assertIn("gemini-pro", models)
        self.assertIn("gemini-pro-vision", models)


if __name__ == '__main__':
    unittest.main()
