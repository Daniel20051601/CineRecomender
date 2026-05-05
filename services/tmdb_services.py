import requests
import os
import time
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TMDB_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

BASE_URL = "https://api.themoviedb.org/3"


def get_movies_page(page):

    url = f"{BASE_URL}/discover/movie?page={page}"

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("results", [])

    except requests.exceptions.RequestException as e:

        print(f"Error en página {page}: {e}")

        return []


def get_all_movies(total_pages=500):

    all_movies = []

    for page in range(1, total_pages + 1):

        print(f"Extrayendo página {page}")

        movies = get_movies_page(page)

        all_movies.extend(movies)

        time.sleep(0.25)

    df = pd.DataFrame(all_movies)

    return df

def get_movies_categories():
    url = f"{BASE_URL}/genre/movie/list?language=en"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        
        response.raise_for_status()
        
        data = response.json()
        
        return pd.DataFrame(data['genres'])
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None