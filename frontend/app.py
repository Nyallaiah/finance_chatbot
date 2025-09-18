import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import os
import base64

BACKEND_URL = "http://127.0.0.1:5000/ask"

st.set_page_config(page_title="Personal Finance Advisor", layout="wide")

# Function to add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        color: black !important; 
        font-family: 'Arial', sans-serif;
    }}

    h1, h2, h3, h4, h5, h6, p, label, span {{
        color: black !important;
    }}

    h1 {{
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.6);
    }}

    /* Transparent black box styling */
    .stTextInput, .stFileUploader, .stSelectbox, .stTextArea, .stNumberInput {{
        background-color: rgba(0,0,0,0.5) !important;
        padding: 10px;
        border-radius: 10px;
        color: black !important;
    }}

    .stButton button {{
        background-color: rgba(255, 215, 0, 0.8); /* Transparent gold */
        color: black !important;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }}

    .stSuccess, .stError {{
        background-color: rgba(0,0,0,0.5) !important;
        padding: 15px;
        border-radius: 12px;
        font-size: 18px;
        color: black !important;
        border: 1px solid black;
    }}

    /* Chart container */
    .stPlotlyChart, .stpyplot {{
        background-color: rgba(0,0,0,0.5);
        padding: 15px;
        border-radius: 12px;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# Call function with your uploaded image path
add_bg_from_local("background.png")

# Title
st.title("💰 Personal Finance Advisor Chatbot")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your expenses CSV", type=["csv"])

# Query input
query = st.text_input("🔍 Ask a question about your expenses")

df = None
file_path = "data/user_uploaded.csv"

# File handling
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    os.makedirs("data", exist_ok=True)
    df.to_csv(file_path, index=False)

    st.subheader("📊 Expense Distribution")
    fig, ax = plt.subplots()
    ax.set_facecolor("white")  # White chart background
    df.groupby("Category")["Amount"].sum().plot(kind="bar", ax=ax, color="blue")
    ax.set_title("Expenses by Category", color="black", fontsize=16)
    ax.set_ylabel("Amount", color="black", fontsize=14)
    ax.set_xlabel("Category", color="black", fontsize=14)
    ax.tick_params(axis="x", colors="black", labelrotation=45)
    ax.tick_params(axis="y", colors="black")
    st.pyplot(fig)

# Button and response
if st.button("💡 Get Answer") and df is not None and query:
    response = requests.post(BACKEND_URL, json={"query": query, "file_path": file_path})
    if response.status_code == 200:
        st.success(response.json().get("response"))
    else:
        st.error("Error: " + response.text)
