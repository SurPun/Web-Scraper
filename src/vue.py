import os # Operating System
import requests # Library for making HTTP requests in Python
from selenium import webdriver # Imports the WebDriver class for controlling web browsers.
from selenium.webdriver.common.by import By # Provides ways to locate elements within a page.
from selenium.webdriver.chrome.service import Service # Allows you to start the Chrome browser in a Selenium script.
from selenium.webdriver.support.ui import WebDriverWait # Provides the ability to wait for a certain condition to occur before proceeding.
from selenium.webdriver.support import expected_conditions as EC # Collection of predefined conditions to use with WebDriverWait.
from selenium.common.exceptions import NoSuchElementException # Exception thrown when an element is not found.

# Image Downloader

def download_image(image_url, file_name):
    # Check if the directory exists where the image will be saved
    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it does not exist
    
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)