import streamlit as st

# ---- Add CSS ----
st.markdown("""
    <style>
        .title {
            color: #2E86C1;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
        }

        .input-box {
            background-color: #f7f7f7;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }

        .btn {
            background-color: #2E86C1;
            color: white;
            padding: 8px 16px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- UI ----
st.markdown("<h1 class='title'>Simple Streamlit App</h1>", unsafe_allow_html=True)

name = st.text_input("Enter your name:", key="name", placeholder="Your Name")

if st.button("Submit"):
    st.success(f"Hello, {name}! 🎉")
