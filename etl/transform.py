import pandas as pd

def transform_movies(df):
    
    columns = ['id',
               'title',
               'backdrop_path',
               'genre_ids',
               'original_language',
               'overview', 
               'popularity',
               'poster_path', 
               'release_date', 
               'vote_average',
               'vote_count']
    
    df = df[columns].copy()
    
    df['title'] = df['title'].str.strip()
    
    df['release_date'] = pd.to_datetime(df['release_date']).dt.date
    
    df = df.drop_duplicates(subset=['id'])
    
    return df

