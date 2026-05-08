import streamlit as st
from database.querys import get_movies
from database.connection import get_engine
from ui.filters import selectbox_categories, slide_years, multiselect_languages, segmented_control_order
from services.movies_service import get_movies_by_filter, count_movies_by_filter
from ui.movie_container import movie_container
from ui.footer import page_footer
from ui.page_bottoms import page_bottoms
import math

df_movies = get_movies()
engine = get_engine()

st.header(" :mag: **Discover your next movie**", text_alignment='center')

categoria_seleccionada = selectbox_categories()
release_years = slide_years(df_movies)
selected_languages = multiselect_languages(engine)
order_by = segmented_control_order()

PAGE_SIZE = 12

if "page" not in st.session_state:
        st.session_state.page = 1
        
if categoria_seleccionada:
          
    id_selected_category = str(categoria_seleccionada['id'])
    
    df_movies = get_movies_by_filter(
        id_selected_category, release_years, engine, selected_languages, order_by,
        page=st.session_state.page, page_size= PAGE_SIZE
    )
    
    total = count_movies_by_filter(id_selected_category, release_years, engine, selected_languages)
    total_pages = math.ceil(total / PAGE_SIZE)  
        
    if not df_movies.empty:
        movie_container(df_movies)
    
    page_bottoms(total_pages)
    
    page_footer()

