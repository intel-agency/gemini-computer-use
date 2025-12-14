# Gemini Computer Use

A Python client for using Google's Gemini AI models with computer use capabilities. This library enables AI-powered screen analysis, computer vision, and automated interaction with your desktop environment.

## Features

- 🖥️ **Screen Capture & Analysis**: Capture and analyze screen content using Gemini's vision capabilities
- 🤖 **AI-Powered Computer Vision**: Understand UI elements, text, and visual content on screen
- 💬 **Conversational Interface**: Maintain chat context for multi-turn interactions
- 🎯 **Action Planning**: Get AI assistance for computer interaction tasks
- 🛠️ **Computer Control Tools**: Mouse and keyboard control integration (PyAutoGUI)
- 🔄 **Multiple Models**: Support for various Gemini models including the latest computer use models

## Installation

### From Source

```bash
git clone https://github.com/intel-agency/gemini-computer-use.git
cd gemini-computer-use
pip install -e .
```

### Using pip (after publishing)

```bash
pip install gemini-computer-use
```

### Requirements

- Python 3.8+
- Google AI API Key (get one at https://makersuite.google.com/app/apikey)

## Quick Start

### 1. Set up your API key

```bash
export GOOGLE_API_KEY='your-api-key-here'
```

Or set it in Python:

```python
import os
os.environ['GOOGLE_API_KEY'] = 'your-api-key-here'
```

### 2. Basic Usage

```python
from gemini_computer_use import GeminiComputerUseClient

# Initialize the client
client = GeminiComputerUseClient()

# Describe what's on your screen
description = client.describe_screen()
print(description)

# Find something specific
result = client.find_on_screen("browser window")
print(result)

# Ask questions about the screen
answer = client.analyze_screen("What applications are open?")
print(answer)
```

### 3. Advanced Usage - Chat Mode

```python
from gemini_computer_use import GeminiComputerUseClient

client = GeminiComputerUseClient()

# Start a chat session
client.start_chat()

# First message with screen context
response = client.send_message(
    "What do you see on this screen?",
    capture_screen=True
)
print(response)

# Follow-up questions maintain context
response = client.send_message(
    "Can you be more specific about the main window?"
)
print(response)
```

## Examples

Check out the `examples/` directory for more detailed examples:

- `simple_demo.py` - Simplest possible usage
- `basic_usage.py` - Common use cases and patterns
- `screen_automation.py` - Advanced automation workflows

Run an example:

```bash
python examples/simple_demo.py
```

## API Reference

### GeminiComputerUseClient

Main client class for interacting with Gemini models.

#### Constructor

```python
client = GeminiComputerUseClient(
    api_key=None,              # API key (or use GOOGLE_API_KEY env var)
    model_name="gemini-2.0-flash-exp",  # Model to use
    temperature=0.7,           # Sampling temperature
    top_p=0.95,               # Top-p sampling
    top_k=40,                 # Top-k sampling
    max_output_tokens=8192    # Max output length
)
```

#### Key Methods

**Screen Analysis**

- `describe_screen()` - Get a description of current screen content
- `analyze_screen(prompt)` - Analyze screen with custom prompt
- `find_on_screen(target)` - Find specific elements on screen

**Chat Interface**

- `start_chat(history=None)` - Start a new chat session
- `send_message(message, image=None, capture_screen=False)` - Send a message
- `generate_content(prompt, image=None)` - One-off generation without chat history

**Action Planning**

- `analyze_action(instruction, capture_result=True)` - Get AI guidance for actions

**Utility**

- `get_screen_size()` - Get screen dimensions
- `list_available_models()` - List available Gemini models

### ComputerTools

Low-level computer interaction tools (accessed via `client.tools`).

**Screen Capture**

- `capture_screen(region=None)` - Capture screenshot
- `screen_to_base64(image, format="PNG")` - Convert image to base64
- `get_screen_size()` - Get screen dimensions

**Mouse Control**

- `move_mouse(x, y, duration=0.2)` - Move mouse cursor
- `click(x=None, y=None, button='left', clicks=1)` - Click mouse
- `scroll(clicks, x=None, y=None)` - Scroll mouse wheel
- `get_mouse_position()` - Get current mouse position

**Keyboard Control**

- `type_text(text, interval=0.05)` - Type text
- `press_key(key)` - Press single key
- `hotkey(*keys)` - Press key combination

## Use Cases

### 1. Screen Monitoring

Monitor your screen and get alerts about specific content:

```python
client = GeminiComputerUseClient()

# Check for errors or alerts
result = client.analyze_screen(
    "Are there any error messages or alerts visible? If yes, describe them."
)
```

### 2. UI Testing

Automated visual testing of applications:

```python
# Verify a button is present
result = client.find_on_screen("Submit button")

# Check layout
result = client.analyze_screen(
    "Is the navigation menu properly aligned at the top?"
)
```

### 3. Accessibility

Help visually impaired users understand screen content:

```python
description = client.describe_screen()
# Convert description to speech or other accessible format
```

### 4. Automation Planning

Get AI suggestions for automation tasks:

```python
result = client.analyze_action(
    "How would I click the save button in the current application?"
)
```

## Model Options

The library supports various Gemini models. The default is `gemini-2.0-flash-exp` which includes computer use capabilities.

Available models (check latest with `client.list_available_models()`):
- `gemini-2.0-flash-exp` - Latest experimental model with computer use
- `gemini-1.5-pro` - Previous generation pro model
- `gemini-1.5-flash` - Fast, efficient model

## Configuration

### Environment Variables

- `GOOGLE_API_KEY` - Your Google AI API key (required)

### Model Parameters

Adjust model behavior via constructor parameters:

```python
client = GeminiComputerUseClient(
    temperature=0.9,      # Higher = more creative (0.0-1.0)
    top_p=0.95,          # Nucleus sampling parameter
    top_k=40,            # Top-k sampling parameter
    max_output_tokens=4096  # Maximum response length
)
```

## Safety & Best Practices

1. **API Key Security**: Never commit API keys to version control
2. **Rate Limiting**: Be mindful of API rate limits
3. **Screen Privacy**: Screen captures may contain sensitive information
4. **Automation Safety**: Use PyAutoGUI's fail-safe (move mouse to corner to abort)
5. **Testing**: Test automation scripts in safe environments first

## Troubleshooting

### API Key Issues

```
Error: API key must be provided...
```

Solution: Set the `GOOGLE_API_KEY` environment variable or pass it to the constructor.

### PyAutoGUI Issues

If mouse/keyboard control doesn't work:

- On Linux: May need X11 display access
- On macOS: May need accessibility permissions
- On Windows: Should work out of the box

### Model Not Found

```
Error: Model not found
```

Solution: Use `client.list_available_models()` to see available models.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built on Google's Generative AI Python SDK
- Uses PyAutoGUI for computer control
- Inspired by computer use capabilities in modern AI models

## Disclaimer

This library provides tools for computer automation. Users are responsible for ensuring their use complies with applicable terms of service, privacy policies, and laws. Always respect user privacy and system security.

## Support

- Issues: https://github.com/intel-agency/gemini-computer-use/issues
- Discussions: https://github.com/intel-agency/gemini-computer-use/discussions

## Changelog

### v0.1.0 (Initial Release)

- Initial implementation of Gemini Computer Use client
- Screen capture and analysis capabilities
- Chat interface with context management
- Computer control tools (mouse & keyboard)
- Example scripts and documentation