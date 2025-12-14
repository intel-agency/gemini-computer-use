from setuptools import setup, find_packages

setup(
    name="gemini-computer-use",
    version="0.1.0",
    description="Google GenAI client for computer use with Gemini models",
    author="Intel Agency",
    packages=find_packages(),
    install_requires=[
        "google-generativeai>=0.8.0",
        "pillow>=10.3.0",
        "pyautogui>=0.9.54",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
