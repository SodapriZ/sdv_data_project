import json
import os
import logging

def save_to_json(data, filename):
    """Save scraped data to a JSON file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"Scraped data saved to {filename}")
    except IOError as e:
        logging.error(f"Error saving scraped data to {filename}: {e}")
        raise