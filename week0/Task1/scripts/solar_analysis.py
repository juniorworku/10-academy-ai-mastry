import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV files for each country
data_country1 = pd.read_csv('/content/drive/MyDrive/path_to_file_country1.csv')
data_country2 = pd.read_csv('/content/drive/MyDrive/path_to_file_country2.csv')
data_country3 = pd.read_csv('/content/drive/MyDrive/path_to_file_country3.csv')

# Convert 'Timestamp' column to datetime format
data_country1['Timestamp'] = pd.to_datetime(data_country1['Timestamp'])
data_country2['Timestamp'] = pd.to_datetime(data_country2['Timestamp'])
data_country3['Timestamp'] = pd.to_datetime(data_country3['Timestamp'])

# Set 'Timestamp' column as index
data_country1.set_index('Timestamp', inplace=True)
data_country2.set_index('Timestamp', inplace=True)
data_country3.set_index('Timestamp', inplace=True)

# Resample data on a monthly basis and aggregate using mean
data_country1_monthly = data_country1.resample('M').mean()
data_country2_monthly = data_country2.resample('M').mean()
data_country3_monthly = data_country3.resample('M').mean()

# Summary Statistics
summary_stats_country1 = data_country1.describe()
summary_stats_country2 = data_country2.describe()
summary_stats_country3 = data_country3.describe()

# Data Quality Check
missing_values_country1 = data_country1.isnull().sum()
missing_values_country2 = data_country2.isnull().sum()
missing_values_country3 = data_country3.isnull().sum()

negative_values_country1 = (data_country1 < 0).sum()
negative_values_country2 = (data_country2 < 0).sum()
negative_values_country3 = (data_country3 < 0).sum()

# Time Series Analysis (Monthly)
plt.figure(figsize=(12, 6))
plt.plot(data_country1_monthly.index, data_country1_monthly['GHI'], label='GHI Country 1')
plt.plot(data_country1_monthly.index, data_country1_monthly['DNI'], label='DNI Country 1')
plt.plot(data_country1_monthly.index, data_country1_monthly['DHI'], label='DHI Country 1')
plt.plot(data_country1_monthly.index, data_country1_monthly['Tamb'], label='Tamb Country 1')
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Time Series Analysis (Monthly) for Country 1')
plt.legend()
plt.show()

# Repeat the same for Country 2 and Country 3

# Correlation Analysis
correlation_matrix_country1 = data_country1.corr()
correlation_matrix_country2 = data_country2.corr()
correlation_matrix_country3 = data_country3.corr()

# Wind Analysis (Monthly)
plt.figure(figsize=(10, 6))
plt.plot(data_country1_monthly.index, data_country1_monthly['WS'], label='WS Country 1')
plt.plot(data_country1_monthly.index, data_country1_monthly['WSgust'], label='WSgust Country 1')
plt.xlabel('Month')
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Analysis (Monthly) for Country 1')
plt.legend()
plt.show()

# Repeat the same for Country 2 and Country 3

# Temperature Analysis (Monthly)
plt.figure(figsize=(10, 6))
plt.plot(data_country1_monthly.index, data_country1_monthly['TModA'], label='TModA Country 1')
plt.plot(data_country1_monthly.index, data_country1_monthly['TModB'], label='TModB Country 1')
plt.plot(data_country1_monthly.index, data_country1_monthly['Tamb'], label='Tamb Country 1')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Analysis (Monthly) for Country 1')
plt.legend()
plt.show()

# Repeat the same for Country 2 and Country 3

# Histograms
plt.figure(figsize=(10, 6))
sns.histplot(data=data_country1, x='GHI', bins=20, kde=True, color='blue')
plt.xlabel('GHI')
plt.ylabel('Frequency')
plt.title('Histogram of GHI for Country 1')
plt.show()

# Repeat the same for Country 2 and Country 3

# Box Plots
plt.figure(figsize=(10, 6))
sns.boxplot(data=data_country1[['GHI', 'DNI', 'DHI', 'Tamb']])
plt.title('Box Plot of Solar Radiation and Ambient Temperature for Country 1')
plt.show()

# Repeat the same for Country 2 and Country 3

# Scatter Plots
plt.figure(figsize=(10, 6))
plt.scatter(data_country1['GHI'], data_country1['Tamb'], alpha=0.5)
plt.xlabel('GHI')
plt.ylabel('Tamb')
plt.title('Scatter Plot: GHI vs. Tamb for Country 1')
plt.show()

# Repeat the same for Country 2 and Country 3 if needed

# Data Cleaning
print("Before data cleaning:")
print("Number of rows before cleaning (Country 1):", len(data_country1))
print("Number of missing values (Country 1):\n", missing_values_country1)
print("Number of negative GHI values (Country 1):", negative_values_country1['GHI'])

# Handle missing values
data_country1_cleaned = data_country1.dropna()

# Handle anomalies (e.g., negative values)
data_country1_cleaned = data_country1_cleaned[data_country1_cleaned['GHI'] >= 0]

print("\nAfter data cleaning:")
print("Number of rows after cleaning (Country 1):", len(data_country1_cleaned))
