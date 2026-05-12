import pandas as pd
import statsmodels.api as sm
import statsmodels.graphics.api as smg
import statsmodels.formula.api as sm_api
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

flights_filename = 'Flight_Delays_2018.csv'
flights_df = pd.read_csv(flights_filename)

coffee_filename = 'coffee.csv'
coffee_df = pd.read_csv(coffee_filename)

#Correlation Matrix - Flights Delays 2018
correlation_flights = flights_df.corr(numeric_only=True).round(2)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_flights, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix - Flights Delays 2018')
plt.show()

#Correlation Matrix - Coffee Data
correlation_coffee = coffee_df.corr(numeric_only=True).round(2)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_coffee, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix - Coffee Data')
plt.show()

#Countries that don't have a significant difference
countries_same = ['Ethiopia','Colombia','Vietnam']
subset_same = coffee_df[coffee_df['Location_Country'].isin(countries_same)]

subset_same.boxplot(column='Data_Scores_Total', by='Location_Country')
plt.title('Boxplot: No Significant Difference')
plt.suptitle('') 
plt.show()

model_same = sm_api.ols(f'Q("Data_Scores_Total") ~ C(Location_Country)', data=subset_same).fit()
print(sm.stats.anova_lm(model_same))

#Countries that have a significant difference
countries_diff = ['United States','Brazil','Indonesia']
subset_diff = coffee_df[coffee_df['Location_Country'].isin(countries_diff)]

subset_diff.boxplot(column='Data_Scores_Total', by='Location_Country')
plt.title('Boxplot: Significant Difference')
plt.suptitle('')
plt.show()

model_diff = sm_api.ols(f'Q("Data_Scores_Total") ~ C(Location_Country)', data=subset_diff).fit()
print(sm.stats.anova_lm(model_diff))
