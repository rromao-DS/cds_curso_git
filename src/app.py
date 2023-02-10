import streamlit as st
from scr.extraction import load_data

st.set_page_config(layout='wide')

def main():
    df_raw = load_data()
    
    st.dataframe(df_raw)
    
if __name__ == '__main__':
    main()