import logging

from extract.web_scrapping.setup_driver import setup_driver, get_last_page_number
from extract.web_scrapping.fetch_page import scrape_page
from extract.web_scrapping.save_to_json import save_to_json

from transform.clean_data import clean_data
from transform.extract_column import extract_columns
from transform.load_data import load_data
from transform.save_dataframe_to_json import save_dataframe_to_json
from transform.setup_spark import initialize_spark

from load.write_data import write_data_to_mongo

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

def transform():
    # Initialize Spark session
    spark = initialize_spark("CoffeeDataTransformation")
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Define the path to the JSON file
    file_path = "./data/1_bronze/scraped_data.json"
    
    try:
        # Load JSON data into DataFrame
        df = load_data(spark, file_path)
        
        # Extract and transform columns
        df = extract_columns(df)
        
        # Clean and preprocess data
        df_cleaned = clean_data(df)
        
        # Show the transformed data (optional)
        logging.info("Transformed data:")
        df_cleaned.show(truncate=False)
        
        return df_cleaned
        
    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        raise

def load(df):
    # Write data to MongoDB
    write_data_to_mongo(df)

def main():
    logging.basicConfig(level=logging.INFO)
    # extract()
    df = transform()
    load(df)
    

if __name__ == "__main__":
    main()