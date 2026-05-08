import streamlit as st
 
def page_bottoms(total_pages):
    col_prev, col_center, col_next = st.columns([1, 5, 1])
    with col_prev:
        if st.button("Anterior") and st.session_state.page > 1:
            st.session_state.page -= 1
            st.rerun()
    
    with col_center:
        st.markdown(f"Página {st.session_state.page} de {total_pages}", text_alignment='center')
    
    with col_next:
        if st.button("Siguiente", disabled=st.session_state.page >= total_pages):
            st.session_state.page += 1
            st.rerun()