import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as plt


# Title
st.title("MoonLight Energy Solutions Dashboard")

@st.cache_data

def load_data(path:str):
    data =pd.read_csv(path)
    return data

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("choose a file", type=["csv","xlsx"])

    if uploaded_file is None:
        st.info("Please select a file to upload through config")
        st.stop()

df = load_data(uploaded_file)

col1, col2, col3 = st.columns([1,1,1])

with col1.expander("solar radiation measurements Data"):
    st.write(
        df, column_config={"Timestamp": st.column_config.NumberColumn(format="%d")},
        )

    
