import sys
import os
sys.path.append(os.path.abspath(".."))
from extract import extract_movies, extract_categories
from transform import transform_movies
from load import load_movies,load_categories

def initial_load():
    print("### Extrayendo peliculas...")
    df = extract_movies(500)
    
    print("Transformando datos")
    df = transform_movies(df)
    
    print("Cargando datos en la base de datos")
    load_movies(df)
    
    print("Peliculas cargadas exitosamente✅\n\n")

def categories_load():
    print('### Extrayendo categorias...')
    df = extract_categories()
    
    print('Subiendo categorias')
    load_categories(df)
    
    print("Categorias subidas exitosamente✅")
    
if __name__ == "__main__":
    initial_load()
    categories_load()
