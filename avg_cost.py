import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'export-AverageDailyTransactionFee.csv'
df = pd.read_csv(file_path)

# Convert the Date(UTC) column to datetime format
df['Date(UTC)'] = pd.to_datetime(df['Date(UTC)'])

# Define the date range
start_date = '2023-12-01'
end_date = '2024-12-01'

# Filter the data for the specified date range
mask = (df['Date(UTC)'] >= start_date) & (df['Date(UTC)'] <= end_date)
filtered_df = df.loc[mask]

# Calculate the average and median of the Average Txn Fee (USD)
average_fee = filtered_df['Average Txn Fee (USD)'].mean()
median_fee = filtered_df['Average Txn Fee (USD)'].median()

print(f"Average Transaction Fee (USD): {average_fee}")
print(f"Median Transaction Fee (USD): {median_fee}")

plt.figure(figsize=(10, 6))
plt.hist(filtered_df['Average Txn Fee (USD)'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Average Txn Fee (USD)')
plt.ylabel('Frequency')
plt.title('Distribution of Average Ethereum Transaction Fees')
plt.show()

plt.figure(figsize=(8, 6))
plt.boxplot(filtered_df['Average Txn Fee (USD)'], vert=False)
plt.xlabel('Average Txn Fee (USD)')
plt.title('Box Plot of Average Ethereum Transaction Fees')
plt.show()

filtered_df['Moving_Average'] = filtered_df['Average Txn Fee (USD)'].rolling(window=30).mean()

plt.figure(figsize=(12, 6))
plt.plot(filtered_df['Date(UTC)'], filtered_df['Average Txn Fee (USD)'], label='Average Txn Fee (USD)')
plt.plot(filtered_df['Date(UTC)'], filtered_df['Moving_Average'], color='red', label='30-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Average Txn Fee (USD)')
plt.title('Average Ethereum Transaction Fee with 30-Day Moving Average')
plt.legend()
plt.show()


