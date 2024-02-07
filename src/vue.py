import os # Operating System
import requests # Library for making HTTP requests in Python
from selenium import webdriver # Imports the WebDriver class for controlling web browsers.
from selenium.webdriver.common.by import By # Provides ways to locate elements within a page.
from selenium.webdriver.chrome.service import Service # Allows you to start the Chrome browser in a Selenium script.
from selenium.webdriver.support.ui import WebDriverWait # Provides the ability to wait for a certain condition to occur before proceeding.
from selenium.webdriver.support import expected_conditions as EC # Collection of predefined conditions to use with WebDriverWait.
from selenium.common.exceptions import NoSuchElementException # Exception thrown when an element is not found.

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


# Extract Data
def extract_data(driver):
    vue_datas = []
    vue_elements = driver.find_elements(By.CSS_SELECTOR, ".card")

    for element in vue_elements:
        movie_name = "Unknown"

        try:
            title_element = element.find_element(By.CSS_SELECTOR, "h3.card-title")
            movie_name = title_element.text.strip()

            link_element = element.find_element(By.CSS_SELECTOR, "a")
            movie_link = link_element.get_attribute('href')

            image_element = element.find_element(By.CSS_SELECTOR, "img")
            image_url = image_element.get_attribute('src') or image_element.get_attribute('data-src')

            image_file_name = f"movie_names/{movie_name.replace(' ', '_')}.jpg"

            download_image(image_url, image_file_name)

            vue_data = {
            'title': movie_name,
            'link': movie_link,
            'image_file_name': image_file_name
            }
            vue_datas.append(vue_data)

        except NoSuchElementException:
            print(f"Error: Movie title element not found within the card.")
        except Exception as e:
            print(f"Error extracting vue data for {movie_name}: {e}")

    return vue_datas

def scrape_movie_details(driver, movie_data):
    driver.get(movie_data["link"])
    try:
        description_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p"))
        )
        movie_data['description'] = description_element.text.strip()
    except NoSuchElementException:
        movie_data['description'] = "No description found."


# Execute
if __name__ == "__main__":

    driver = setup_webdriver()

    navigate_to_page(driver, "https://www.myvue.com/")
    accept_cookies(driver)

    data = extract_data(driver)

    for movie in data:
        scrape_movie_details(driver, movie)

    print(data)

    input("Press Enter to close the browser...")
    driver.quit()