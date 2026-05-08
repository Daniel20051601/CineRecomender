import streamlit as st
from database.querys import get_categories
from services.movies_service import get_older_year, get_language_codes
from utils.languages import country_code_to_name

def selectbox_categories():

    df_categories = get_categories()

    options = df_categories.to_dict('records')

    selected = st.selectbox(
        "Select a category",
        options,
        format_func= lambda x: x['name'],
        index=None,
        placeholder="Choose an option",
        key="cat", 
        on_change=reset_page
    )

    return selected

def slide_years(df_movies):
    min_year = get_older_year(df_movies)
    slide = st.slider("Select a year range", min_year, 2026, min_year, key="year", on_change=reset_page)
    return slide

def multiselect_languages(engine):
    code_list = get_language_codes(engine)
    languages = country_code_to_name(code_list)
    
    options = {lang["name"]: lang["code"] for lang in languages}
    selected_names = st.multiselect("Select the languages", list(options.keys()), key="langs", on_change=reset_page)
    
    selected_codes = [options[name] for name in selected_names]
    
    return selected_codes

def segmented_control_order():
    filters = {"popularity": "Popularity",
               "vote_average": "Rating",
               "release_date": "Release date" 
               }
    control = st.segmented_control("Order by", list(filters.keys()), format_func= lambda x: filters.get(x, x), key = 'order_by' ,on_change= reset_page )
    
    return control
    
def reset_page():
    st.session_state.page = 1