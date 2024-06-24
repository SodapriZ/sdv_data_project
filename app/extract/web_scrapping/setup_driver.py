from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    """Setup Chrome WebDriver with Selenium."""
    options = Options()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def get_last_page_number(driver, base_url):
    """Retrieve the last page number from the pagination."""
    driver.get(base_url)
    time.sleep(5)
    pagination_li_elements = driver.find_elements(By.CSS_SELECTOR, 'ul.pagination > li')
    
    if not pagination_li_elements:
        return 1

    last_li = pagination_li_elements[-1]
    
    if 'pagination-link' in last_li.get_attribute('class'):
        return int(last_li.find_element(By.TAG_NAME, 'a').get_attribute('data-page'))
    
    second_last_li = pagination_li_elements[-2]
    return int(second_last_li.find_element(By.TAG_NAME, 'a').get_attribute('data-page'))