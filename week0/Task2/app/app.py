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

# Dashboard Layout
st.sidebar.title("Solar Data Analysis")
analysis_type = st.sidebar.selectbox("Choose Analysis Type", ["Solar Radiation", "Temperature", "Wind", "Correlation"])

# Solar Radiation Analysis
if analysis_type == "Solar Radiation":
    st.title("Solar Radiation Analysis")
    st.subheader("Monthly Average GHI")

    st.write("Benin")
    monthly_avg_benin = data_benin['GHI'].resample('M').mean()
    st.line_chart(monthly_avg_benin)

    st.write("Sierra Leone")
    monthly_avg_sierra = data_sierra['GHI'].resample('M').mean()
    st.line_chart(monthly_avg_sierra)

    st.write("Togo")
    monthly_avg_togo = data_togo['GHI'].resample('M').mean()
    st.line_chart(monthly_avg_togo)

    # Bar chart showing total GHI for each country
    st.subheader("Total GHI for Each Country")
    total_ghi = pd.DataFrame({
        'Country': ['Benin', 'Sierra Leone', 'Togo'],
        'Total GHI': [data_benin['GHI'].sum(), data_sierra['GHI'].sum(), data_togo['GHI'].sum()]
    })
    st.bar_chart(total_ghi.set_index('Country'))

     # Box plots for Solar Radiation
    st.subheader("Box Plot of Solar Radiation for Each Location")
    st.write("Box plots show the distribution of solar radiation values.")
    
    # Box plots for Benin (Malanville)
    st.write("**Benin (Malanville)**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=data_benin[['GHI', 'DNI', 'DHI', 'Tamb']], ax=ax)
    ax.set_title('Box Plot of Solar Radiation and Ambient Temperature for Benin (Malanville)')
    st.pyplot(fig)

    # Box plots for Sierra Leone (Bumbuna)
    st.write("**Sierra Leone (Bumbuna)**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=data_sierra[['GHI', 'DNI', 'DHI', 'Tamb']], ax=ax)
    ax.set_title('Box Plot of Solar Radiation and Ambient Temperature for Sierra Leone (Bumbuna)')
    st.pyplot(fig)

    # Box plots for Togo (Dapaong)
    st.write("**Togo (Dapaong)**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=data_togo[['GHI', 'DNI', 'DHI', 'Tamb']], ax=ax)
    ax.set_title('Box Plot of Solar Radiation and Ambient Temperature for Togo (Dapaong)')
    st.pyplot(fig)


# Temperature Analysis
elif analysis_type == "Temperature":
    st.title("Temperature Analysis")
    st.subheader("Monthly Average Temperature")

    st.write("Benin")
    temp_avg_benin = data_benin['Tamb'].resample('M').mean()
    st.line_chart(temp_avg_benin)

    st.write("Sierra Leone")
    temp_avg_sierra = data_sierra['Tamb'].resample('M').mean()
    st.line_chart(temp_avg_sierra)

    st.write("Togo")
    temp_avg_togo = data_togo['Tamb'].resample('M').mean()
    st.line_chart(temp_avg_togo)

    # Scatter plots for Temperature
    st.subheader("Scatter Plot of GHI vs. Temperature for Each Location")
    st.write("Scatter plots show the relationship between GHI and temperature.")
    
    # Scatter plots for Benin (Malanville)
    st.write("**Benin (Malanville)**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data_benin, x='GHI', y='Tamb', ax=ax)
    ax.set_xlabel('GHI')
    ax.set_ylabel('Tamb')
    ax.set_title('Scatter Plot: GHI vs. Tamb for Benin (Malanville)')
    st.pyplot(fig)

    # Scatter plots for Sierra Leone (Bumbuna)
    st.write("**Sierra Leone (Bumbuna)**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data_sierra, x='GHI', y='Tamb', ax=ax)
    ax.set_xlabel('GHI')
    ax.set_ylabel('Tamb')
    ax.set_title('Scatter Plot: GHI vs. Tamb for Sierra Leone (Bumbuna)')
    st.pyplot(fig)

    # Scatter plots for Togo (Dapaong)
    st.write("**Togo (Dapaong)**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data_togo, x='GHI', y='Tamb', ax=ax)
    ax.set_xlabel('GHI')
    ax.set_ylabel('Tamb')
    ax.set_title('Scatter Plot: GHI vs. Tamb for Togo (Dapaong)')
    st.pyplot(fig)

    

# Wind Analysis
elif analysis_type == "Wind":
    st.title("Wind Speed Analysis")
    st.subheader("Monthly Average Wind Speed")

    st.write("Benin")
    wind_avg_benin = data_benin['WS'].resample('M').mean()
    st.line_chart(wind_avg_benin)

    st.write("Sierra Leone")
    wind_avg_sierra = data_sierra['WS'].resample('M').mean()
    st.line_chart(wind_avg_sierra)

    st.write("Togo")
    wind_avg_togo = data_togo['WS'].resample('M').mean()
    st.line_chart(wind_avg_togo)

# Correlation Analysis
else:
    st.title("Correlation Analysis")
    st.subheader("Correlation between GHI and Temperature")

    st.write("Benin")
    st.write(data_benin[['GHI', 'Tamb']].corr())

    st.write("Sierra Leone")
    st.write(data_sierra[['GHI', 'Tamb']].corr())

    st.write("Togo")
    st.write(data_togo[['GHI', 'Tamb']].corr())

