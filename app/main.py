import requests
from bs4 import BeautifulSoup
import json
import os
import logging
from unidecode import unidecode


from extract.web_scrapping.extract_with_bs4 import fetch_page_content, parse_recipe_page, save_recipe_to_json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of recipes with title, URL, and refresh date
recipes_list = [
    {"title": "Recette de Crêpes", "url": "https://cuisine.journaldesfemmes.fr/recette/333415-recette-de-crepes-la-meilleure-recette-rapide", "refresh_date": "2024-06-24"},
    {"title": "Recette de Crêpes", "url": "https://cuisine.journaldesfemmes.fr/recette/333415-recette-de-crepes-la-meilleure-recette-rapide", "refresh_date": "2024-06-24"},
]

def extract(url, filepath):
    html_content = fetch_page_content(url)
    recipe_data = parse_recipe_page(html_content)
    save_recipe_to_json(recipe_data, filepath)

    # Print the scraped data (optional)
    print("Titre de la recette:", recipe_data['recipe_title'])
    print("\nIngrédients:")
    for ing in recipe_data['ingredients']:
        if isinstance(ing, dict):
            print(f"- {ing['quantity']} {ing['name']}")
        else:
            print(f"- {ing}")

    print("\nÉtapes de préparation:")
    for i, etape in enumerate(recipe_data['steps'], start=1):
        print(f"{i}. {etape}")

def main (recipes_list):
    for recipe in recipes_list:
        url = recipe['url']
        bronze_path = f'./data/1_bronze/{unidecode(recipe.get("title").lower().replace(' ','_'))}.json'
        extract(url, bronze_path)

if __name__ == "__main__":
    main(recipes_list)