import logging
from extract.web_scrapping.setup_driver import setup_driver, get_last_page_number
from extract.web_scrapping.fetch_page import scrape_page
from extract.web_scrapping.save_to_json import save_to_json

# URL of the page to scrape
BASE_URL = 'https://www.maxicoffee.com/tous-cafes-grain-c-58_1361.html?sort_products=name_asc'

def extract():
    driver = setup_driver()
    try:
        last_page_number = get_last_page_number(driver, BASE_URL)
        logging.info(f"Total number of pages: {last_page_number}")

        all_scraped_data = []

        for page_number in range(1, last_page_number + 2):
            current_url = f"{BASE_URL}&page={page_number}"
            logging.info(f"Scraping page {page_number}: {current_url}")
            scraped_data = scrape_page(driver, current_url)
            all_scraped_data.extend(scraped_data)
        
        save_to_json(all_scraped_data, './data/1_bronze/scraped_data.json')

    finally:
        driver.quit()

def main():
    logging.basicConfig(level=logging.INFO)
    extract()
    

if __name__ == "__main__":
    main()