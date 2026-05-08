import pandas as pd
from sqlalchemy import text

def get_older_year(df):
    years = df['release_date'].dropna().apply(lambda x: x.year)
    older_year = int(years.min())
    return older_year

def get_movies_by_filter(category, 
                         min_year, 
                         engine, 
                         languages=None,
                         order_by = None,
                         page=1, 
                         page_size=12):
    
    offset = (page - 1) * page_size
    
    query = """
        SELECT *
        FROM movies
        WHERE genre_ids ILIKE :category
          AND EXTRACT(YEAR FROM release_date) >= :min_year
    """
    params = {"category": f"%{category}%", "min_year": min_year}

    if languages:
        query += " AND original_language IN :languages"
        params["languages"] = tuple(languages)
    
    if order_by:
        query += f" ORDER BY {order_by} DESC"
        
    query += " LIMIT :page_size OFFSET :offset"
    params["page_size"] = page_size
    params["offset"] = offset

    return pd.read_sql(text(query), engine, params=params)


def count_movies_by_filter(category, min_year, engine, languages=None):
    query = """
        SELECT COUNT(*)
        FROM movies
        WHERE genre_ids ILIKE :category
          AND EXTRACT(YEAR FROM release_date) >= :min_year
    """
    params = {"category": f"%{category}%", "min_year": min_year}
    
    if languages:
        query += " AND original_language IN :languages"
        params["languages"] = tuple(languages)

    return pd.read_sql(text(query), engine, params=params).iloc[0, 0]


def get_category_names(category_ids, engine):
    query = text("""
        SELECT name
        FROM categories
        WHERE id IN :category_ids
    """)
    params = {"category_ids": tuple(category_ids)}
    
    result = pd.read_sql(query, engine, params=params)
    
    return result['name'].tolist()
    
def string_to_list(cadena):
    return [int(x) for x in cadena.strip('{}').split(',') if x]

def get_language_codes(engine):
    query = text("""
             SELECT DISTINCT(original_language)
             FROM movies
             """)

    df_languages = pd.read_sql(query, engine)
    list_languages = df_languages['original_language'].tolist()
    
    return list_languages
    