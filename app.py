import streamlit as st
from database.querys import get_movies
from database.connection import get_engine
from ui.filters import selectbox_categories, slide_years, multiselect_languages, segmented_control_order
from services.movies_service import get_movies_by_filter, count_movies_by_filter
from ui.modal import show_movie_information
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
        cols = st.columns(3)
        for i,(_,movie) in enumerate(df_movies.iterrows()):
            with cols[i % 3]:
                with st.container(border = True, width='stretch', height=460):
                    st.image(f"https://image.tmdb.org/t/p/w500{movie['poster_path']}")
                    st.write(
                        f"**{movie['title'][:20] + '...' if len(movie['title']) > 20 else movie['title']}**"
                    )
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.badge(str(movie['release_date'].year), color='blue')
                            
                    with col2:
                        st.badge(movie['original_language'] ,icon="🌐", color = 'violet')
                        
                    with col3:
                        st.badge(str(round(movie['vote_average'], 1)), icon="🌟", color = 'yellow')
                    
                    if st.button("Details", key=f"btn_{i}", type='tertiary'):
                            show_movie_information(movie)
                        
    
    
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

st.space('medium')
st.markdown(f"""**Created by** Ramon Emilio Lopez  
            :blue-badge[[Github](https://github.com/Daniel20051601)] :blue-badge[[LinkedIn](https://www.linkedin.com/in/ram%C3%B3n-emilio-lopez-57a833211)]""")        
st.space('xxsmall')
st.write("Powered by")
st.image("https://www.themoviedb.org/assets/2/v4/logos/v2/blue_long_2-9665a76b1ae401a510ec1e0ca40ddcb3b0cfe45f1d51b77a308fea0845885648.svg",
         width=250,
         )