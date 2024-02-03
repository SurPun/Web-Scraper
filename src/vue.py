import os # Operating System
import requests # Library for making HTTP requests in Python
from selenium import webdriver # Imports the WebDriver class for controlling web browsers.
from selenium.webdriver.common.by import By # Provides ways to locate elements within a page.
from selenium.webdriver.chrome.service import Service # Allows you to start the Chrome browser in a Selenium script.
from selenium.webdriver.support.ui import WebDriverWait # Provides the ability to wait for a certain condition to occur before proceeding.
from selenium.webdriver.support import expected_conditions as EC # Collection of predefined conditions to use with WebDriverWait.
from selenium.common.exceptions import NoSuchElementException # Exception thrown when an element is not found.