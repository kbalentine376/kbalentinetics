import pandas as pd
import matplotlib.pyplot as plt

pennData =  pd.read_csv('pennDataB320k.csv')


df =  pd.DataFrame(pennData)

print(df.describe())

print(df.info())

print(df.groupby('Year')['GPA'].mean())

df.groupby('Year')['GPA'].mean().plot(kind='bar', color='green', edgecolor='black')
plt.title('Average GPA by Year')
plt.xlabel('Year')
plt.ylabel('Average GPA')
plt.show()

df['GPA'].plot(kind='hist', bins=5,edgecolor='black')
plt.title('GPA Distribution')
plt.xlabel('GPA')
plt.ylabel('Number of Students')
plt.show()