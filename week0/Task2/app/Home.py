import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load Data


# Title
st.title("MoonLight Energy Solutions Dashboard")

@st.cache

def load_data():
    data =pd.read_csv('Benin.csv')
    return data

data = load_data()

# Title and introduction
st.title('Solar Installation Potential Dashboard')
st.write('Explore regions with high potential for solar installation and monitor operational efficiency.')

# Solar Radiation Analysis
st.header('Solar Radiation Analysis')
selected_month = st.selectbox('Select Month', data['month'].unique())
month_data = data[data['month'] == selected_month]
st.line_chart(month_data[['GHI', 'DNI', 'DHI']])
