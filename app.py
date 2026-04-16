import streamlit as st
import pathlib

st.set_page_config(
    page_title="Dashboard Focus — Banco Central do Brasil",
    page_icon="🏦",
    layout="wide",
)

# Remove Streamlit default chrome so the dashboard fills the entire screen
st.markdown("""
    <style>
        #MainMenu, header, footer { visibility: hidden; }
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

html_content = pathlib.Path("dashboard.html").read_text(encoding="utf-8")

st.components.v1.html(html_content, height=1000, scrolling=True)
