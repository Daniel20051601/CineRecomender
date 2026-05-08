from database.connection import get_engine

engine = get_engine()

def load_movies(df):
    df.to_sql(
        "movies",
        engine,
        if_exists="append",
        index=False
    )
    
    print("Peliculas guardadas exitosamente")
    
def load_categories(df):
    df.to_sql(
        "categories",
        engine,
        if_exists="replace",
        index=False
    )