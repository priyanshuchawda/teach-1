import pandas as pd

# Create a DataFrame (or read from a CSV using pd.read_csv('file.csv'))
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "Salary": [50000, 54000, 58000, None]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Clean the data: Fill missing salary with the average
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Calculate statistics
print("\nStatistics:")
print(df.describe())  # Summarize numerical columns

# Filter: Get all rows where Age > 25
print("\nFiltered Rows (Age > 25):")
print(df[df['Age'] > 25])
