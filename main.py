import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Aetheria",
    page_icon="assets/page_icon.png",
)

welcome_page = st.Page(
    page="screens/home.py",
    title="Beranda",
    icon=":material/home:",
    default=True,
)

chatbot_page = st.Page(
    page="screens/chatbot.py",
    title="Chatbot",
    icon=":material/robot:",
)

resume_page = st.Page(
    page="screens/resume.py",
    title="Buat CV",
    icon=":material/edit_square:",
)

developer_page = st.Page(
    page="screens/developer.py",
    title="Developer",
    icon=":material/developer_mode:",
)

pg = st.navigation(pages=[welcome_page, chatbot_page, resume_page, developer_page])
pg.run()