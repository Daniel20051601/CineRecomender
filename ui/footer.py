import streamlit as st

def page_footer():
    st.space('medium')
    
    st.markdown(f"""**Created by** Ramon Emilio Lopez  
            :blue-badge[[Github](https://github.com/Daniel20051601)] :blue-badge[[LinkedIn](https://www.linkedin.com/in/ram%C3%B3n-emilio-lopez-57a833211)]""")        
    
    st.space('xxsmall')
    
    st.write("Powered by")
    st.image("https://www.themoviedb.org/assets/2/v4/logos/v2/blue_long_2-9665a76b1ae401a510ec1e0ca40ddcb3b0cfe45f1d51b77a308fea0845885648.svg",
         width=250,
         ) 