import requests
from bs4 import BeautifulSoup
import json
import os
import logging

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Successfully fetched the content from {url}")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching the URL {url}: {e}")
        raise

def parse_recipe_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract recipe title
    title_tag = soup.find('h1', class_='app_recipe_title_page')
    title = title_tag.get_text(strip=True) if title_tag else 'Titre non trouvé'
    
    # Extract ingredients
    ingredients = []
    ingredients_list = soup.select('ul.app_recipe_list--2 li')
    for item in ingredients_list:
        ingredient_name = item.find('span', class_='jHiddenHref')
        ingredient_quantity = item.find('span', class_='jIngredientQuantity')
        if ingredient_name and ingredient_quantity:
            ingredients.append({
                "name": ingredient_name.get_text(strip=True),
                "quantity": ingredient_quantity.get_text(strip=True)
            })
    if not ingredients:
        logging.warning("No ingredients found")
        ingredients.append('Ingrédients non trouvés')

    # Extract preparation steps
    steps = []
    steps_list = soup.select('section.app_recipe_section--steps ol li')
    for item in steps_list:
        steps.append(item.get_text(strip=True))
    if not steps:
        logging.warning("No preparation steps found")
        steps.append('Étapes de préparation non trouvées')

    return {
        "recipe_title": title,
        "ingredients": ingredients,
        "steps": steps
    }

def save_recipe_to_json(recipe_data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe_data, f, ensure_ascii=False, indent=4)
        logging.info(f"Recipe data saved to {filepath}")
    except IOError as e:
        logging.error(f"Error saving recipe data to {filepath}: {e}")
        raise