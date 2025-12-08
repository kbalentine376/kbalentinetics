import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

#load our data frame
df = pd.read_csv('students_dat00.csv')
pennData = pd.DataFrame(df)

print()
print("-_"*20)
print()
print("Head of the DataFrame") # First five rows of the dataframe
print(pennData.head())

print()
print("-_"*20)
print()
print("Tail of the DataFrame") # Last five rows of the dataframe
print(pennData.tail())

print()
print("-_"*20)
print()
print("Summary") # Summary of the dataframe
print(pennData.info())

print()
print("-_"*20)
print()
print("Statistics") # Stats of the dataframe
print(round(pennData.describe()))

print()
print("-_"*20)
print()
print("Counts of Students in Pathways")
print(pennData['Pathway'].value_counts())

print()
print("-_"*20)
print()
print("Average GPA Per Year")
print(pennData.groupby('Year')['GPA'].mean())

print()
print("-_"*20)
print()
print("Top Three Students by GPA")
print(pennData.sort_values(by = 'GPA', ascending = False).head(3))

print()
print("-_"*20)
print()
print("Students With GPA > 3.5")
print(pennData[pennData['GPA']>3.5])

print()
print("-_"*20)
print()
print("First Student Data")
print(pennData.iloc[0])