import streamlit as st
import time


# Custom HTML styling
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #2E86C1;
        }
        .subtitle {
            font-size: 20px;
            color: #566573;
        }
        .footer {
            font-size: 12px;
            color: #A6ACAF;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📈 Company Prospects</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered stock prediction & sentiment insights</div>', unsafe_allow_html=True)
st.write("---")

ticker = st.text_input("🔍 Enter a stock ticker (e.g., AAPL, TSLA):")

placeholder = st.empty()  # reserve a slot for the message

if ticker:
    st.success(f"✅ You entered: {ticker}")

    # Create a placeholder for the loading message
    loading_message = st.empty()
    loading_message.info("📰 Pulling data and predictions now...")

    # Wait 2 seconds
    time.sleep(2)

    # Clear the loading message
    loading_message.empty()

    # (Optional) Show your actual prediction/data here
    st.write("✅ Data loaded! (This is where predictions will go.)")


# Footer
st.markdown(
    '<div class="footer">This app was created for educational and research purposes only. It is not intended to provide financial advice. All data is collected in compliance with public terms of service and used fairly for non-commercial use.</div>',
    unsafe_allow_html=True)
