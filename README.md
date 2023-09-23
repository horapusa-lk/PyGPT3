# PyGPT3

### Collect cookies


1. Open [poe.com/ChatGPT](https://poe.com/ChatGPT)
2. Register the the web site for free.
3. Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/) 
4. Go to [poe.com/ChatGPT](https://poe.com/ChatGPT)
5. Open the extension
6. Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
7. Paste your cookies into a file `cookies.json`.
8. Go to [poe.com/GPT-3.5-Turbo-Instruct](https://poe.com/GPT-3.5-Turbo-Instruct)
9. Send a message and wait for the response.
10. Copy the page url . use it as `chat_url`

### Install Requirements
```
pip3 install -r requirements.txt
```

Regular Example:
```python
from PyGPT import PyGPT3
def chatgpt(msg_prompt: str):
    gpt3 = PyGPT3("cookie_file_path", 'chat_url')
    return str(gpt3.chat(msg_prompt))
chatgpt("hello world")
```
