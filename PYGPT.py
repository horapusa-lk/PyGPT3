
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


class PyGPT3:
    def __init__(self, cookie_file_path, web_url):
        self.cookie_file_path = cookie_file_path
        self.web_url = web_url
        # Start virtual display
        self.display = Display(visible=False, size=(1920, 1080))  # Adjust size as needed
        self.display.start()
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        # chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (optional)

        # Create a WebDriver instance (in this case, for Chrome)
        self.driver = webdriver.Chrome()

        # Load the JSON data from the cookie.json file
        with open(self.cookie_file_path, 'r') as file:
            cookies = json.load(file)

        # Navigate to a webpage
        self.driver.get(self.web_url)

        for cookie in cookies:
            # Check if 'sameSite' is missing or invalid, and set it to 'Lax'
            if 'sameSite' not in cookie or cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                cookie['sameSite'] = 'Lax'

            self.driver.add_cookie(cookie)

        # Navigate to a webpage
        self.driver.get(self.web_url)

    def chat(self, prompt):
        textarea = self.driver.find_element(By.CLASS_NAME,
                                       'GrowingTextArea_textArea__eadlu')  # Replace 'button_id' with the actual ID of the button
        textarea.clear()
        textarea.send_keys(prompt)
        textarea.send_keys(Keys.RETURN)
        # time.sleep(10)
        old_text = None
        time.sleep(3)
        while True:
            rsp_element = self.driver.find_elements(By.CLASS_NAME, 'Markdown_markdownContainer__UyYrv')
            current_text = str(rsp_element[-1].text)
            if current_text == old_text:
                break
            else:
                old_text = str(rsp_element[-1].text)
            time.sleep(1)

        return current_text

    def quit(self):
        self.display.stop()
        self.driver.quit()
        print("Quit Success")
