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


# proxy settings
vue_domain = "https://www.myvue.com/"
NO_PROXY_DOMAINS = "localhost, vue_domain"
os.environ["no_proxy"] = NO_PROXY_DOMAINS


def _get_chromedriver_path():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root_path = os.path.abspath(os.path.join(current_dir, os.pardir))
    chromedriver_path = os.path.join(
        project_root_path,
        "chromedriver",
        "chromedriver.exe"
    )
    return chromedriver_path


def setup_webdriver():
    service = Service(executable_path=_get_chromedriver_path())
    return webdriver.Chrome(service=service)


# Navigate To Url
def navigate_to_page(driver, url):
    driver.get(url)


# Accept Cookies
def accept_cookies(driver):
    try:
        agree_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        agree_button.click()
    except NoSuchElementException:
        print("Cookie acceptance element not found on page.")


# Execute
if __name__ == "__main__":

    driver = setup_webdriver()

    navigate_to_page(driver, "https://www.myvue.com/")
    accept_cookies(driver)

