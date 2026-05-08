from services.tmdb_services import get_all_movies, get_movies_categories, get_movies_page
import pandas as pd

def extract_movies(pages):
    df_movies = get_all_movies(pages)
    return df_movies

def extract_categories():
    df_categories = get_movies_categories()
    return df_categories

def extract_recent_movies():

    all_movies = []

    for page in range(1, 6):

        movies = get_movies_page(page)

        all_movies.extend(movies)

    return pd.DataFrame(all_movies)