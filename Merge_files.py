# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:34:48 2023

@author: Tinni
"""

import pandas as pd

# Read in each CSV file and extract only the columns we want
df1 = pd.read_csv('Daily_Min_Temp.csv', usecols=['Station', 'Year', 'Month', 'AVG_Monthly_Min_Temp'])
df2 = pd.read_csv('Daily_Max_Temp.csv', usecols=['Station', 'Year', 'Month', 'AVG_Monthly_Max_Temp'])
df3 = pd.read_csv('Daily_Rainfall.csv', usecols=['Station', 'Year', 'Month', 'AVG_Monthly_Rainfall'])
df4 = pd.read_csv('Daily_Sunshine.csv', usecols=['Station', 'Year', 'Month', 'AVG_Monthly_Sunshine'])
df5 = pd.read_csv('Daily_AVG_humidity.csv', usecols=['Station', 'Year', 'Month', 'AVG_Monthly_Humidity'])

# Merge the data frames based on station, year, and month

merged_df = pd.merge(df1, df2, on=['Station', 'Year', 'Month'])
merged_df = pd.merge(merged_df, df3, on=['Station', 'Year', 'Month'])
merged_df = pd.merge(merged_df, df4, on=['Station', 'Year', 'Month'])
merged_df = pd.merge(merged_df, df5, on=['Station', 'Year', 'Month'])

# Write the merged data frame to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)
