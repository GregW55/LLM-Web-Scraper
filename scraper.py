import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import numpy as np


def scrape_website(website: str) -> str:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    with webdriver.Chrome(service=Service("./chromedriver.exe"), options=chrome_options) as driver:
        driver.get(website)
        return driver.page_source

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content: str) -> str:
    soup = BeautifulSoup(body_content, "lxml")  # Using lxml parser for better performance

    # Remove scripts and styles in parallel
    def remove_elements(tag):
        elements = soup.find_all(tag)
        for element in elements:
            element.extract()

    with ThreadPoolExecutor() as executor:
        executor.map(remove_elements, ["script", "style"])

    # Efficient text extraction
    text_content = soup.get_text(separator="\n")
    return "\n".join(line.strip() for line in text_content.splitlines() if line.strip())


def split_dom_content(dom_content: str, max_length: int = 7000) -> list[str]:
    # Use numpy for efficient array operations
    content_array = np.array(list(dom_content))
    chunks = np.array_split(content_array, len(content_array) // max_length + 1)
    return [''.join(chunk) for chunk in chunks]

