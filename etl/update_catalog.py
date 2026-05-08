import sys
import os
sys.path.append(os.path.abspath(".."))
from etl.extract import extract_recent_movies
from etl.transform import transform_movies
from database.connection import get_engine

from sqlalchemy import text

engine = get_engine()


def update_catalog():

    print("Extrayendo películas recientes...")

    df_movies = extract_recent_movies()

    print(f"Películas extraídas: {len(df_movies)}")

    if df_movies.empty:
        print("No se encontraron películas nuevas")
        return

    print("Transformando películas...")

    df_movies = transform_movies(df_movies)

    print("Insertando nuevas películas...")

    with engine.begin() as conn:

        for _, row in df_movies.iterrows():

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

    print("Catálogo actualizado correctamente ✅")


if __name__ == "__main__":
    update_catalog()