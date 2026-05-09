import streamlit as st
from services.tmdb_services import get_movie_details, get_movie_credits
from services.movies_service import string_to_list, get_category_names, get_director, get_cast
from database.connection import get_engine

engine = get_engine()

@st.cache_data(ttl=3600, show_spinner=False)
def get_movie_details_cached(movie_id):
    return get_movie_details(movie_id)

@st.cache_data(ttl=3600, show_spinner=False)
def get_movie_credits_cached(movie_id):
    return get_movie_credits(movie_id)

@st.dialog("Movie Information")
def show_movie_information(movie):
    
    with st.spinner("Cargando detalles..."):
        movie_details = get_movie_details_cached(movie['id'])
        credits = get_movie_credits_cached(movie['id'])
    
    director = get_director(credits)
    
    col1, col2 = st.columns([3,1])
    with col1:
        st.image(f"https://image.tmdb.org/t/p/w500{movie['backdrop_path']}")
        
        if movie_details['status'] != 'Released':
            st.badge(f"{movie_details['status']}", color='red')
            
    with col2:
        st.markdown(f"""
                    :blue-badge[🌟 {str(round(movie['vote_average'], 1))}]
                    :blue-badge[📆 {str(movie['release_date'].year)}]
                    :blue-badge[⏰{movie_details['runtime']} min]
                    :blue-badge[🌐{movie['original_language']}]
                    """)
            
    st.subheader(movie['title'])
    st.markdown(f"**Overview:** {movie['overview'][:200] + '...' if len(movie['overview']) > 200 else movie['overview'] }")

    st.markdown(f"🎬**Director:** {director}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Cast**")
        get_cast(credits)
        
    with col2:
        st.markdown("**Categories**")
        id_list = string_to_list(movie['genre_ids'])
        name_categories = get_category_names(id_list, engine)
        badges = "  ".join([f":blue-badge[{name}]" for name in name_categories])
        st.markdown(badges)
        
    if movie_details['budget'] != 0 and movie_details['revenue'] != 0:
        st.markdown(f":green-badge[**Budget:**] {movie_details['budget']:,} ") 
        st.markdown(f":green-badge[**Revenue:**] {movie_details['revenue']:,} ")
    


    