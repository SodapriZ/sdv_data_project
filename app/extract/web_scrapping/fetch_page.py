from selenium.webdriver.common.by import By
import time
import logging

def scrape_page(driver, url):
    """Scrape data from a single page."""
    driver.get(url)
    time.sleep(5)  # Give time for the page to fully load
    
    product_containers = driver.find_elements(By.CLASS_NAME, 'produit')
    scraped_data = []

    for product in product_containers:
        title = product.find_element(By.CLASS_NAME, 'produit-titre').text.strip()

        # Extract reviews
        try:
            rating_elem = product.find_element(By.CLASS_NAME, 'rating')
            stars = rating_elem.find_elements(By.TAG_NAME, 'img')
            rating = len(stars)
            total_reviews = product.find_element(By.CLASS_NAME, 'produit-avis').text.strip().split()[0]
            reviews = f"Rating: {rating} stars ({total_reviews} reviews)"
        except Exception:
            reviews = 'No reviews or rating'

        # Extract price
        try:
            price = product.find_element(By.CLASS_NAME, 'prix').text.strip()
        except Exception:
            price = 'N/A'

        # Extract commerce details
        commerce_details = []
        element_commerce_divs = product.find_elements(By.CLASS_NAME, 'element-commerce')
        for div in element_commerce_divs:
            img_tag = div.find_element(By.TAG_NAME, 'img')
            if img_tag:
                alt_text = img_tag.get_attribute('alt')
                commerce_details.append(alt_text)
        
        commerce_details_str = ', '.join(commerce_details)
        
        if commerce_details and price:
            scraped_data.append({
                'Title': title,
                'Reviews': reviews,
                'Price': price,
                'Commerce Details': commerce_details_str
            })
        else:
            pass

    return scraped_data