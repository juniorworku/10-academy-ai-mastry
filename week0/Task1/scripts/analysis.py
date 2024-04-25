import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
togo_data = pd.read_csv('togo-dapaong_qc.csv')
sierraleone_data = pd.read_csv('sierraleone-bumbuna.csv')
benin_data = pd.read_csv('benin-malanville.csv')

# Function to clean data
def clean_data(df):
    if df['Comments'].isnull().all():
        df.drop('Comments', axis=1, inplace=True)
    # Fill missing values with the mean of each column
    df.fillna(df.mean(numeric_only=True), inplace=True)
    return df

# Clean the datasets
togo_data = clean_data(togo_data)
sierraleone_data = clean_data(sierraleone_data)
benin_data = clean_data(benin_data)

# Function to plot box plots for solar radiation and temperature data
def plot_boxplots(df, country_name):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'Tamb']])
    plt.title('Box Plot of Solar Radiation and Temperature in ' + country_name)
    plt.ylabel('Value')
    plt.show()

# Function to plot scatter plots for GHI vs Tamb and WS vs WSgust
def plot_scatterplots(df, country_name):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(df['GHI'], df['Tamb'])
    plt.title('GHI vs Tamb in ' + country_name)
    plt.xlabel('GHI')
    plt.ylabel('Tamb')
    
    plt.subplot(1, 2, 2)
    plt.scatter(df['WS'], df['WSgust'])
    plt.title('WS vs WSgust in ' + country_name)
    plt.xlabel('WS')
    plt.ylabel('WSgust')
    plt.show()

# Plotting box plots and scatter plots for each country
plot_boxplots(togo_data, 'Togo')
plot_boxplots(sierraleone_data, 'Sierra Leone')
plot_boxplots(benin_data, 'Benin')

plot_scatterplots(togo_data, 'Togo')
plot_scatterplots(sierraleone_data, 'Sierra Leone')
plot_scatterplots(benin_data, 'Benin')