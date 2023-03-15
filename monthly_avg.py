import pandas as pd

# Read the CSV file
data = pd.read_csv("Daily_AVG_humidity.csv")

# Calculate the average for each row
data['AVG_Monthly_Humidity'] = round(data.iloc[:, 2:33].mean(axis=1), 0)

# Save the updated dataframe to a new CSV file
data.to_csv("Daily_AVG_humidity.csv", index=False)
