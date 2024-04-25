#Setup and Data Loading
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    data_benin = pd.read_csv('/home/ted/Desktop/10 Academy Artificial Intelligence Mastery/week0/Task2/data/Benin_Malanville_monthly.csv', parse_dates=['Timestamp'], index_col='Timestamp')
    data_sierra = pd.read_csv('/home/ted/Desktop/10 Academy Artificial Intelligence Mastery/week0/Task2/data/Sierra_Leone_Bumbuna_monthly.csv', parse_dates=['Timestamp'], index_col='Timestamp')
    data_togo = pd.read_csv('/home/ted/Desktop/10 Academy Artificial Intelligence Mastery/week0/Task2/data/Togo_Dapaong_Qc_monthly.csv', parse_dates=['Timestamp'], index_col='Timestamp')
    return data_benin, data_sierra, data_togo

data_benin, data_sierra, data_togo = load_data()

#Dashboard Layout
st.sidebar.title("Solar Data Analysis")
analysis_type = st.sidebar.selectbox("Choose Analysis Type", ["Solar Radiation", "Temperature", "Wind","Correlation"])

#Solar Radiation Analysis
if analysis_type == "Solar Radiation":
    st.title("Solar Radiation Analysis")
    fig, ax = plt.subplots()
    monthly_avg = data_benin['GHI'].resample('M').mean()
    ax.plot(monthly_avg.index, monthly_avg.values)
    ax.set_title('Monthly Average GHI - Benin')
    ax.set_xlabel('Month')
    ax.set_ylabel('GHI')
    st.pyplot(fig)

if analysis_type == "Solar Radiation":
    st.title("Solar Radiation Analysis")
    fig, ax = plt.subplots()
    monthly_avg = data_sierra['GHI'].resample('M').mean()
    ax.plot(monthly_avg.index, monthly_avg.values)
    ax.set_title('Monthly Average GHI - Sierra')
    ax.set_xlabel('Month')
    ax.set_ylabel('GHI')
    st.pyplot(fig)
if analysis_type == "Solar Radiation":
    st.title("Solar Radiation Analysis")
    fig, ax = plt.subplots()
    monthly_avg = data_togo['GHI'].resample('M').mean()
    ax.plot(monthly_avg.index, monthly_avg.values)
    ax.set_title('Monthly Average GHI - Togo')
    ax.set_xlabel('Month')
    ax.set_ylabel('GHI')
    st.pyplot(fig)



#Temperature Analysis
if analysis_type == "Temperature":
    st.title("Temperature Analysis")
    fig, ax = plt.subplots()
    temp_avg = data_benin['Tamb'].resample('M').mean()
    ax.plot(temp_avg.index, temp_avg.values)
    ax.set_title('Monthly Average Temperature - Benin')
    ax.set_xlabel('Month')
    ax.set_ylabel('Temperature (°C)')
    st.pyplot(fig)

if analysis_type == "Temperature":
    st.title("Temperature Analysis")
    fig, ax = plt.subplots()
    temp_avg = data_sierra['Tamb'].resample('M').mean()
    ax.plot(temp_avg.index, temp_avg.values)
    ax.set_title('Monthly Average Temperature - Sierra Leone')
    ax.set_xlabel('Month')
    ax.set_ylabel('Temperature (°C)')
    st.pyplot(fig)

if analysis_type == "Temperature":
    st.title("Temperature Analysis")
    fig, ax = plt.subplots()
    temp_avg = data_togo['Tamb'].resample('M').mean()
    ax.plot(temp_avg.index, temp_avg.values)
    ax.set_title('Monthly Average Temperature - Togo')
    ax.set_xlabel('Month')
    ax.set_ylabel('Temperature (°C)')
    st.pyplot(fig)

#Wind Analysis
if analysis_type == "Wind":
    st.title("Wind Speed Analysis")
    fig, ax = plt.subplots()
    wind_avg = data_benin['WS'].resample('M').mean()
    ax.plot(wind_avg.index, wind_avg.values)
    ax.set_title('Monthly Average Wind Speed - Benin')
    ax.set_xlabel('Month')
    ax.set_ylabel('Wind Speed (m/s)')
    st.pyplot(fig)

if analysis_type == "Wind":
    st.title("Wind Speed Analysis")
    fig, ax = plt.subplots()
    wind_avg = data_sierra['WS'].resample('M').mean()
    ax.plot(wind_avg.index, wind_avg.values)
    ax.set_title('Monthly Average Wind Speed - Sierra')
    ax.set_xlabel('Month')
    ax.set_ylabel('Wind Speed (m/s)')
    st.pyplot(fig)

if analysis_type == "Wind":
    st.title("Wind Speed Analysis")
    fig, ax = plt.subplots()
    wind_avg = data_togo['WS'].resample('M').mean()
    ax.plot(wind_avg.index, wind_avg.values)
    ax.set_title('Monthly Average Wind Speed - Togo')
    ax.set_xlabel('Month')
    ax.set_ylabel('Wind Speed (m/s)')
    st.pyplot(fig)


#Correlation Analysis
if analysis_type == "Correlation":
    st.title("Correlation Analysis between GHI and Temperature in Benin")
    fig, ax = plt.subplots()
    sns.heatmap(data_benin[['GHI', 'Tamb']].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

if analysis_type == "Correlation":
    st.title("Correlation Analysis between GHI and Temperature in Sierra")
    fig, ax = plt.subplots()
    sns.heatmap(data_sierra[['GHI', 'Tamb']].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

if analysis_type == "Correlation":
    st.title("Correlation Analysis between GHI and Temperature in Togo")
    fig, ax = plt.subplots()
    sns.heatmap(data_togo[['GHI', 'Tamb']].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)