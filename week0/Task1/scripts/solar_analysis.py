import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


# Read CSV files for each country
data_benin_malanville = pd.read_csv('week0/Task1/data/benin-malanville.csv')
data_sierraleone_bumbuna = pd.read_csv('week0/Task1/data/sierraleone-bumbuna.csv')
data_togo_dapaong_qc = pd.read_csv('week0/Task1/data/togo-dapaong_qc.csv')

# Convert 'Timestamp' column to datetime format
data_benin_malanville['Timestamp'] = pd.to_datetime(data_benin_malanville['Timestamp'])
data_sierraleone_bumbuna['Timestamp'] = pd.to_datetime(data_sierraleone_bumbuna['Timestamp'])
data_togo_dapaong_qc['Timestamp'] = pd.to_datetime(data_togo_dapaong_qc['Timestamp'])

# Set 'Timestamp' column as index
data_benin_malanville.set_index('Timestamp', inplace=True)
data_sierraleone_bumbuna.set_index('Timestamp', inplace=True)
data_togo_dapaong_qc.set_index('Timestamp', inplace=True)

# Resample data on a monthly basis and aggregate using mean
data_benin_malanville_monthly = data_benin_malanville.resample('ME').mean()
data_sierraleone_bumbuna_monthly = data_sierraleone_bumbuna.resample('ME').mean()
data_togo_dapaong_qc_monthly = data_togo_dapaong_qc.resample('ME').mean()

# Calculate summary statistics for each country
summary_stats_benin_malanville= data_benin_malanville.describe()
summary_stats_sierraleone_bumbuna= data_sierraleone_bumbuna.describe()
summary_stats_togo_dapaong_qc = data_togo_dapaong_qc.describe()


print("Summary Statistics for Benin_malanville:\n", summary_stats_benin_malanville)
print("\nSummary Statistics for Sierraleone_bumbuna:\n", summary_stats_sierraleone_bumbuna)
print("\nSummary Statistics for Togo_dapaong_qc:\n", summary_stats_togo_dapaong_qc)


# Check for missing values for each country
missing_values_benin_malanville = data_benin_malanville.isnull().sum()
missing_values_sierraleone_bumbuna = data_sierraleone_bumbuna.isnull().sum()
missing_values_togo_dapaong_qc = data_togo_dapaong_qc.isnull().sum()

print("Missing Values for Benin_malanville:\n", missing_values_benin_malanville)
print("\nMissing Values for Sierraleone_bumbuna:\n", missing_values_sierraleone_bumbuna)
print("\nMissing Values for Togo_dapaong_qc:\n", missing_values_togo_dapaong_qc)

# Check for outliers (e.g., negative values) for each country
negative_values_benin_malanville = data_benin_malanville.loc[:, data_benin_malanville.columns != 'Timestamp'].lt(0).sum()
negative_values_sierraleone_bumbuna = data_sierraleone_bumbuna.loc[:, data_sierraleone_bumbuna.columns != 'Timestamp'].lt(0).sum()
negative_values_togo_dapaong_qc = data_togo_dapaong_qc.loc[:, data_togo_dapaong_qc.columns != 'Timestamp'].lt(0).sum()

print("\nNegative Values for Benin_malanville:\n", negative_values_benin_malanville)
print("\nNegative Values for Sierraleone_bumbuna):\n", negative_values_sierraleone_bumbuna)
print("\nNegative Values for Togo_dapaong_qc:\n", negative_values_togo_dapaong_qc)


# Plot Time Series Analysis for Benin_malanville (Monthly)
plt.figure(figsize=(12, 6))
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['GHI'], label='GHI Benin_malanville')
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['DNI'], label='DNI Benin_malanville')
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['DHI'], label='DHI Benin_malanville')
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['Tamb'], label='Tamb Benin_malanville')
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Time Series Analysis (Monthly) for Benin_malanville')
plt.legend()
plt.show()

# Plot Time Series Analysis for Sierraleone_bumbuna (Monthly)
plt.figure(figsize=(12, 6))
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['GHI'], label='GHI Sierraleone_bumbuna')
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['DNI'], label='DNI Sierraleone_bumbuna')
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['DHI'], label='DHI Sierraleone_bumbuna')
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['Tamb'], label='Tamb Sierraleone_bumbuna')
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Time Series Analysis (Monthly) for Sierraleone_bumbuna')
plt.legend()
plt.show()

# Plot Time Series Analysis for Togo_dapaong_qc(Monthly)
plt.figure(figsize=(12, 6))
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['GHI'], label='GHI Togo_dapaong_qc')
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['DNI'], label='DNI Togo_dapaong_qc')
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['DHI'], label='DHI Togo_dapaong_qc')
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['Tamb'], label='Tamb Togo_dapaong_qc')
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Time Series Analysis (Monthly) for Togo_dapaong_qc')
plt.legend()
plt.show()


# Calculate correlation matrix for each country
correlation_matrix_benin_malanville = data_benin_malanville.corr()
correlation_matrix_sierraleone_bumbuna = data_sierraleone_bumbuna.corr()
correlation_matrix_togo_dapaong_qc = data_togo_dapaong_qc.corr()

print("Correlation Matrix for Benin_malanville:\n", correlation_matrix_benin_malanville)
print("\nCorrelation Matrix for Sierraleone_bumbuna:\n", correlation_matrix_sierraleone_bumbuna)
print("\nCorrelation Matrix for Togo_dapaong_qc:\n", correlation_matrix_togo_dapaong_qc)


# Wind Analysis for Benin_malanville
plt.figure(figsize=(10, 6))
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['WS'], label='WS Benin_malanville')
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['WSgust'], label='WSgust Benin_malanville')
plt.xlabel('Month')
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Analysis (Monthly) for Benin_malanville')
plt.legend()
plt.show()

# Wind Analysis Sierraleone_bumbuna
plt.figure(figsize=(10, 6))
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['WS'], label='WS Sierraleone_bumbuna')
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['WSgust'], label='WSgust Sierraleone_bumbuna')
plt.xlabel('Month')
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Analysis (Monthly) for Sierraleone_bumbuna')
plt.legend()
plt.show()

# Wind Analysis for Togo_dapaong_qc
plt.figure(figsize=(10, 6))
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['WS'], label='WS Togo_dapaong_qc')
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['WSgust'], label='WSgust Togo_dapaong_qc')
plt.xlabel('Month')
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Analysis (Monthly) for Togo_dapaong_qc')
plt.legend()
plt.show()

# Temperature Analysis for Benin_malanville
plt.figure(figsize=(10, 6))
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['TModA'], label='TModA Benin_malanville')
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['TModB'], label='TModB Benin_malanville')
plt.plot(data_benin_malanville_monthly.index, data_benin_malanville_monthly['Tamb'], label='Tamb Benin_malanville')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Analysis (Monthly) for Benin_malanville')
plt.legend()
plt.show()

# Temperature Analysis for Sierraleone_bumbuna
plt.figure(figsize=(10, 6))
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['TModA'], label='TModA Sierraleone_bumbuna')
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['TModB'], label='TModB Sierraleone_bumbuna')
plt.plot(data_sierraleone_bumbuna_monthly.index, data_sierraleone_bumbuna_monthly['Tamb'], label='Tamb Sierraleone_bumbuna')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Analysis (Monthly) for Sierraleone_bumbuna')
plt.legend()
plt.show()

# Temperature Analysis for Togo_dapaong_qc
plt.figure(figsize=(10, 6))
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['TModA'], label='TModA Togo_dapaong_qc')
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['TModB'], label='TModB Togo_dapaong_qc')
plt.plot(data_togo_dapaong_qc_monthly.index, data_togo_dapaong_qc_monthly['Tamb'], label='Tamb Togo_dapaong_qc')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Analysis (Monthly) for Togo_dapaong_qc')
plt.legend()
plt.show()

# Histograms for Benin_malanville
plt.figure(figsize=(10, 6))
sns.histplot(data=data_benin_malanville, x='GHI', bins=20, kde=True, color='blue')
plt.xlabel('GHI')
plt.ylabel('Frequency')
plt.title('Histogram of GHI for Benin_malanville')
plt.show()

# Histograms for Sierraleone_bumbuna
plt.figure(figsize=(10, 6))
sns.histplot(data=data_sierraleone_bumbuna, x='GHI', bins=20, kde=True, color='blue')
plt.xlabel('GHI')
plt.ylabel('Frequency')
plt.title('Histogram of GHI for Sierraleone_bumbuna')
plt.show()

# Histograms for Togo_dapaong_qc
plt.figure(figsize=(10, 6))
sns.histplot(data=data_togo_dapaong_qc, x='GHI', bins=20, kde=True, color='blue')
plt.xlabel('GHI')
plt.ylabel('Frequency')
plt.title('Histogram of GHI for Togo_dapaong_qc')
plt.show()

# Create box plots for each country

# Box plots for Benin_malanville
plt.figure(figsize=(10, 6))
sns.boxplot(data=data_benin_malanville[['GHI', 'DNI', 'DHI', 'Tamb']])
plt.title('Box Plot of Solar Radiation and Ambient Temperature for Benin_malanville')
plt.show()

# Box plots for Sierraleone_bumbuna
plt.figure(figsize=(10, 6))
sns.boxplot(data=data_sierraleone_bumbuna[['GHI', 'DNI', 'DHI', 'Tamb']])
plt.title('Box Plot of Solar Radiation and Ambient Temperature for Sierraleone_bumbuna')
plt.show()

# Box plots for Togo_dapaong_qc
plt.figure(figsize=(10, 6))
sns.boxplot(data=data_togo_dapaong_qc[['GHI', 'DNI', 'DHI', 'Tamb']])
plt.title('Box Plot of Solar Radiation and Ambient Temperature for Togo_dapaong_qc')
plt.show()

# Scatter Plots for Benin_malanville
plt.figure(figsize=(10, 6))
plt.scatter(data_benin_malanville['GHI'], data_benin_malanville['Tamb'], alpha=0.5)
plt.xlabel('GHI')
plt.ylabel('Tamb')
plt.title('Scatter Plot: GHI vs. Tamb for Benin_malanville')
plt.show()

# Scatter Plots for Sierraleone_bumbuna
plt.figure(figsize=(10, 6))
plt.scatter(data_sierraleone_bumbuna['GHI'], data_sierraleone_bumbuna['Tamb'], alpha=0.5)
plt.xlabel('GHI')
plt.ylabel('Tamb')
plt.title('Scatter Plot: GHI vs. Tamb for Sierraleone_bumbuna')
plt.show()

# Scatter Plots for Togo_dapaong_qc
plt.figure(figsize=(10, 6))
plt.scatter(data_togo_dapaong_qc['GHI'], data_togo_dapaong_qc['Tamb'], alpha=0.5)
plt.xlabel('GHI')
plt.ylabel('Tamb')
plt.title('Scatter Plot: GHI vs. Tamb for Togo_dapaong_qc')
plt.show()

# Data Cleaning Benin_malanville

print("Before data cleaning:")
print("Number of rows before cleaning:", len(data_benin_malanville))
print("Number of missing values:\n", data_benin_malanville.isnull().sum())
print("Number of negative GHI values:", (data_benin_malanville['GHI'] < 0).sum())

# Handle missing values country1
data_benin_malanville_cleaned = data_benin_malanville.dropna()

# Handle anomalies (e.g., negative values) country1
data_benin_malanville_cleaned = data_benin_malanville_cleaned[data_benin_malanville_cleaned['GHI'] >= 0]

print("\nAfter data cleaning:")
print("Number of rows after cleaning:", len(data_benin_malanville_cleaned))



# Data Cleaning Sierraleone_bumbuna

print("Before data cleaning:")
print("Number of rows before cleaning:", len(data_sierraleone_bumbuna))
print("Number of missing values:\n", data_sierraleone_bumbuna.isnull().sum())
print("Number of negative GHI values:", (data_sierraleone_bumbuna['GHI'] < 0).sum())

# Handle missing values
data_sierraleone_bumbuna_cleaned = data_sierraleone_bumbuna.dropna()

# Handle anomalies (e.g., negative values) Sierraleone_bumbuna
data_sierraleone_bumbuna_cleaned = data_sierraleone_bumbuna_cleaned[data_sierraleone_bumbuna_cleaned['GHI'] >= 0]

print("\nAfter data cleaning:")
print("Number of rows after cleaning:", len(data_sierraleone_bumbuna_cleaned))

# Data Cleaning Togo_dapaong_qc

print("Before data cleaning:")
print("Number of rows before cleaning:", len(data_togo_dapaong_qc))
print("Number of missing values:\n", data_togo_dapaong_qc.isnull().sum())
print("Number of negative GHI values:", (data_togo_dapaong_qc['GHI'] < 0).sum())

# Handle missing values
data_togo_dapaong_qc_cleaned = data_togo_dapaong_qc.dropna()

# Handle anomalies (e.g., negative values) country1
data_togo_dapaong_qc_cleaned = data_togo_dapaong_qc_cleaned[data_togo_dapaong_qc_cleaned['GHI'] >= 0]

print("\nAfter data cleaning:")
print("Number of rows after cleaning:", len(data_togo_dapaong_qc_cleaned))


