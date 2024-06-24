from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# URL of the page to scrape
base_url = 'https://www.maxicoffee.com/tous-cafes-grain-c-58_1361.html?sort_products=name_asc'

# Setup Chrome WebDriver with Selenium
options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode (without opening browser window)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open URL in Chrome
driver.get(base_url)
time.sleep(5)  # Give time for the page to fully load (adjust as needed)

# Get all pagination <li> elements
pagination_li_elements = driver.find_elements(By.CSS_SELECTOR, 'ul.pagination > li')

# Get the last <li> element
last_li = pagination_li_elements[-1]

# Check if the last <li> element contains a direct page link or is a '...' for further pages
if 'pagination-link' in last_li.get_attribute('class'):
    last_page_number = last_li.find_element(By.TAG_NAME, 'a').get_attribute('data-page')
else:
    # If it's '...', get the second to last <li> which should have the last actual page link
    second_last_li = pagination_li_elements[-2]
    last_page_number = second_last_li.find_element(By.TAG_NAME, 'a').get_attribute('data-page')

print(f"Total number of pages: {last_page_number}")

# Function to scrape data from a single page
def scrape_page(url):
    driver.get(url)
    time.sleep(5)  # Give time for the page to fully load (adjust as needed)

    # Find all product containers
    product_containers = driver.find_elements(By.CLASS_NAME, 'produit')

    # Loop through each product container
    for product in product_containers:
        # Extract title
        title_elem = product.find_element(By.CLASS_NAME, 'produit-titre')
        title = title_elem.text.strip() if title_elem else 'N/A'

        # Extract reviews
        try:
            rating_elem = product.find_element(By.CLASS_NAME, 'rating')
            stars = rating_elem.find_elements(By.TAG_NAME, 'img')
            rating = len(stars)  # Counting the number of filled stars
            total_reviews_elem = product.find_element(By.CLASS_NAME, 'produit-avis')
            total_reviews = total_reviews_elem.text.strip().split()[0]
            reviews = f"Rating: {rating} stars ({total_reviews} reviews)"
        except:
            reviews = 'No reviews or rating'

        # Extract price
        try:
            price_elem = product.find_element(By.CLASS_NAME, 'prix')
            price = price_elem.text.strip() if price_elem else 'N/A'
        except:
            price = 'N/A'

        # Extract commerce details
        commerce_details = []
        element_commerce_divs = product.find_elements(By.CLASS_NAME, 'element-commerce')
        for div in element_commerce_divs:
            img_tag = div.find_element(By.TAG_NAME, 'img')
            if img_tag:
                alt_text = img_tag.get_attribute('alt')
                commerce_details.append(alt_text)

        # Print the results (or you can store them in a list/dictionary)
        print(f"Title: {title}")
        print(f"Reviews: {reviews}")
        print(f"Price: {price}")
        print(f"Commerce Details: {commerce_details}")
        print("-------------------------------------------------------")

# Loop through all pages
for page_number in range(1, int(last_page_number) + 1):
    if page_number == 1:
        current_url = base_url
    else:
        current_url = f"{base_url}&page={page_number}"

    print(f"Scraping page {page_number}: {current_url}")
    scrape_page(current_url)

# Close the WebDriver
driver.quit()