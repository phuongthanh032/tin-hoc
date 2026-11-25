from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Câu 10B - Phân tích Dao động Tắt dần & Cộng hưởng",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Tối ưu khoảng trắng viền của Streamlit để giao diện hiển thị toàn màn hình
st.markdown(
    """
    <style>
        .block-container {
            padding: 0.5rem 0.5rem 0rem 0.5rem;
            max-width: 100%;
        }
        header { visibility: hidden; }
    </style>
""",
    unsafe_allow_html=True,
)

html_content = Path("index.html").read_text(encoding="utf-8")
components.html(html_content, height=1380, scrolling=True)
