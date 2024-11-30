import streamlit as st

def add_header():
    
    st.header("Matrix Mall",divider="gray")



if __name__ == "__main__":

    add_header()

    st.page_link('pages\\single_matrix.py', label='Continue with single matrix')







