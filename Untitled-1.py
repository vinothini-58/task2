
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")  
print(df.head())
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
print(df.info())
plt.figure(figsize=(14, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', hue='Region', data=df)
plt.title('Unemployment Rate Over Time by Region')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()