from database.connection import get_engine
from sqlalchemy import text

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
    
def load_new_movies(data):
    try:
        with engine.begin() as conn:
            for _, row in data.iterrows():

                query = text("""
                    INSERT INTO movies (
                        id,
                        title,
                        backdrop_path,
                        genre_ids,
                        original_language,
                        overview, 
                        popularity,
                        poster_path, 
                        release_date, 
                        vote_average,
                        vote_count
                    )
                    VALUES (
                        :id,
                        :title,
                        :backdrop_path,
                        :genre_ids,
                        :original_language,
                        :overview,
                        :popularity,
                        :poster_path,
                        :release_date,
                        :vote_average,
                        :vote_count
                    )
                    ON CONFLICT (id)
                    DO NOTHING
                """)

                conn.execute(query, row.to_dict())
        return True
    
    except Exception as e:
        print('Error: ', e)
        return False