from database.connection import get_engine
import pandas as pd

engine = get_engine()

def get_movies():
    try:
        df = pd.read_sql('SELECT * FROM "movies"', engine)
        return df
    except Exception as e:
        print(f"Error al cargar las peliculas: {e}")
        
def get_categories():
    try:
        df = pd.read_sql('SELECT * FROM "categories"', engine)
        return df
    except Exception as e:
        print(f"Error al cargar las categorias: {e}")

