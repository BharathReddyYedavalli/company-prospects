import streamlit as st
from streamlit_javascript import st_javascript

st.set_page_config(page_title="Company Prospects", layout="centered")

st.markdown("""
    <style>
        .big-title {
            font-size: 36px;
            font-weight: 800;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        }
        .section {
            background: #f7f7f7;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0px 0px 8px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">📈 Company Prospects</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.subheader("🧠 What This App Does")
    st.write("Predicts stock trends, gathers recent company news, and offers insights on whether to invest.")

    st.subheader("🌐 Browser Info (via JavaScript)")
    browser_info = st_javascript("navigator.userAgent")
    st.write("Your browser is:", browser_info)

    st.subheader("🚀 Coming Soon")
    st.info("Predictions and news features will appear here after you connect your backend or data feed!")

    st.markdown('</div>', unsafe_allow_html=True)
