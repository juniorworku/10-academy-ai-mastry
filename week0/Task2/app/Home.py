import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data


# Title
st.title("MoonLight Energy Solutions Dashboard")

# Sidebar
st.sidebar.title("Options")
option = st.sidebar.selectbox("Select Dataset", ["Benin Malanville", "Sierra Leone Bumbuna", "Togo Dapaong QC"])

# Main Content
if option == "Benin Malanville":
    st.subheader("Benin Malanville Dataset")

    # Add more visualizations and analysis here
elif option == "Sierra Leone Bumbuna":
    st.subheader("Sierra Leone Bumbuna Dataset")

    # Add more visualizations and analysis here
elif option == "Togo Dapaong QC":
    st.subheader("Togo Dapaong QC Dataset")
