import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
togo_data = pd.read_csv('week0/Task1/data/benin-malanville.csv')
sierraleone_data = pd.read_csv('week0/Task1/data/sierraleone-bumbuna.csv')
benin_data = pd.read_csv('week0/Task1/data/togo-dapaong_qc.csv')


df_togo = pd.read_csv('togo-dapaong_qc.csv')
df_sierraleone = pd.read_csv('sierraleone-bumbuna.csv')
df_benin = pd.read_csv('benin-malanville.csv')

print('Togo Data:')
print(df_togo.head())
print('\
Sierra Leone Data:')
print(df_sierraleone.head())
print('\
Benin Data:')
print(df_benin.head())

# Descriptive statistics for each dataset
print('Descriptive Statistics for Togo Data:')
print(df_togo.describe())
print('\
Descriptive Statistics for Sierra Leone Data:')
print(df_sierraleone.describe())
print('\
Descriptive Statistics for Benin Data:')
print(df_benin.describe())

# Checking for missing values in each dataset
print('\
Missing Values in Togo Data:')
print(df_togo.isnull().sum())
print('\
Missing Values in Sierra Leone Data:')
print(df_sierraleone.isnull().sum())
print('\
Missing Values in Benin Data:')
print(df_benin.isnull().sum())

# Converting 'Timestamp' column to datetime format for each dataset
from tqdm import tqdm
tqdm.pandas()

df_togo['Timestamp'] = df_togo['Timestamp'].progress_apply(pd.to_datetime)
df_sierraleone['Timestamp'] = df_sierraleone['Timestamp'].progress_apply(pd.to_datetime)
df_benin['Timestamp'] = df_benin['Timestamp'].progress_apply(pd.to_datetime)

print('Timestamp conversion done for all datasets.')

# Resampling data on a monthly basis and aggregating using mean for each dataset
monthly_togo = df_togo.resample('M', on='Timestamp').mean()
monthly_sierraleone = df_sierraleone.resample('M', on='Timestamp').mean()
monthly_benin = df_benin.resample('M', on='Timestamp').mean()

print('Monthly resampling and aggregation done for all datasets.')

# Data quality check for each dataset by checking for any anomalies or inconsistencies
# Checking for extreme values and inconsistencies in the monthly resampled data
def check_data_quality(df):
    anomalies = {}
    for column in df.columns:
        # Check for extreme values that are beyond reasonable expectations
        q_low = df[column].quantile(0.01)
        q_high = df[column].quantile(0.99)
        anomalies[column] = df[(df[column] < q_low) | (df[column] > q_high)].shape[0]
    return anomalies

quality_togo = check_data_quality(monthly_togo)
quality_sierraleone = check_data_quality(monthly_sierraleone)
quality_benin = check_data_quality(monthly_benin)

print('Data Quality Check for Togo:\
', quality_togo)
print('Data Quality Check for Sierra Leone:\
', quality_sierraleone)
print('Data Quality Check for Benin:\
', quality_benin)

import matplotlib.pyplot as plt

# Plotting time series for GHI, DNI, DHI, and Tamb for each country
def plot_time_series(df, country_name):
    plt.figure(figsize=(14, 10))
    plt.plot(df.index, df['GHI'], label='GHI')
    plt.plot(df.index, df['DNI'], label='DNI')
    plt.plot(df.index, df['DHI'], label='DHI')
    plt.plot(df.index, df['Tamb'], label='Ambient Temperature')
    plt.title('Time Series of GHI, DNI, DHI, and Tamb in ' + country_name)
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_time_series(monthly_togo, 'Togo')
plot_time_series(monthly_sierraleone, 'Sierra Leone')
plot_time_series(monthly_benin, 'Benin')


import seaborn as sns

# Function to plot correlation matrix for selected variables
def plot_correlation(df, variables, country_name):
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[variables].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    plt.title('Correlation Matrix for ' + country_name)
    plt.show()

# Variables of interest
variables = ['GHI', 'DHI', 'DNI', 'TModA', 'TModB']

# Plotting correlation matrices for each country
plot_correlation(monthly_togo, variables, 'Togo')
plot_correlation(monthly_sierraleone, variables, 'Sierra Leone')
plot_correlation(monthly_benin, variables, 'Benin')





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

import matplotlib.pyplot as plt

# Plotting time series for GHI, DNI, DHI, and Tamb for each country
def plot_time_series(df, country_name):
    plt.figure(figsize=(14, 10))
    plt.plot(df.index, df['GHI'], label='GHI')
    plt.plot(df.index, df['DNI'], label='DNI')
    plt.plot(df.index, df['DHI'], label='DHI')
    plt.plot(df.index, df['Tamb'], label='Ambient Temperature')
    plt.title('Time Series of GHI, DNI, DHI, and Tamb in ' + country_name)
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_time_series(monthly_togo, 'Togo')
plot_time_series(monthly_sierraleone, 'Sierra Leone')
plot_time_series(monthly_benin, 'Benin')

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