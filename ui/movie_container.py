import streamlit as st
from ui.modal import show_movie_information

def movie_container(df_movies):
    
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