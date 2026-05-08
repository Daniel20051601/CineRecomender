import streamlit as st
from database.querys import get_movies
from database.connection import get_engine
from ui.filters import selectbox_categories, slide_years, multiselect_languages, segmented_control_order
from services.movies_service import get_movies_by_filter, count_movies_by_filter
from ui.movie_container import movie_container
from ui.footer import page_footer
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
    
    col_prev, col_center, col_next = st.columns([1, 5, 1])
    with col_prev:
        if st.button("Anterior") and st.session_state.page > 1:
            st.session_state.page -= 1
            st.rerun()
    
    with col_center:
        st.markdown(f"<div style='text-align:center; font-size:18px;'>Página {st.session_state.page} de {total_pages}</div>", unsafe_allow_html=True)
    
    with col_next:
        if st.button("Siguiente", disabled=st.session_state.page >= total_pages):
            st.session_state.page += 1
            st.rerun()
    
    page_footer()

