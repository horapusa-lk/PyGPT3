# PyGPT3

Welcome to PyGPT3, a Python package that allows you to interact with OpenAI's GPT-3.5 Turbo through a simple interface. This README file provides instructions on how to collect necessary cookies and install the package for seamless integration.

## Collect Cookies

Follow these steps to collect the required cookies for interacting with GPT-3.5 Turbo:

1. Open [poe.com/ChatGPT](https://poe.com/ChatGPT).
2. Register on the website for free.
3. Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/).
4. Go to [poe.com/ChatGPT](https://poe.com/ChatGPT).
5. Open the cookie extension.
6. Click "Export" on the bottom right, then "Export as JSON" (This will save your cookies to the clipboard).
7. Paste your cookies into a file named `cookies.json`.
8. Go to [poe.com/GPT-3.5-Turbo-Instruct](https://poe.com/GPT-3.5-Turbo-Instruct).
9. Send a message and wait for the response.
10. Copy the page URL and use it as `chat_url`.

## Installation

To set up PyGPT3, follow these installation steps:

```bash
git clone https://github.com/horapusa-lk/PyGPT3
cd PyGPT3
pip3 install -r requirements.txt
```

## Regular Usage Example

To use PyGPT3 and interact with GPT-3.5 Turbo, follow these steps:

1. Import the `PyGPT3` class from the PyGPT module.
2. Initialize an instance of `PyGPT3` with the appropriate cookie file path and chat URL.
3. Use the `chat()` method to send a message prompt to GPT-3.5 Turbo and receive a response.

```python
from PyGPT import PyGPT3

def chatgpt(msg_prompt: str):
    # Initialize PyGPT3 with the cookie file path and chat URL
    gpt3 = PyGPT3("cookie_file_path", 'chat_url')
    
    # Send a message prompt and get the response
    return str(gpt3.chat(msg_prompt))

# Example usage
response = chatgpt("Hello, world!")
print(response)
