import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data


# Title
st.title("MoonLight Energy Solutions Dashboard")

def load_data(path:str):
    data = pd.read_csv(path)
    return data

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is None:
    st.info("Please select a file to upload through config")
    st.stop()

df = load_data(uploaded_file)
st.dataframe(df)