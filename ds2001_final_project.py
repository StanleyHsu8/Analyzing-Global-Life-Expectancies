#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DS2001 - Final Project
Life Expectancy

Stanley Hsu, Justin Lee, Tim Rohan
"""

import pandas as pd
import matplotlib.pyplot as plt
import random as rand
import numpy as np

import sklearn
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm


life_CSV = "life_expectancy_data.csv"

country_df = pd.read_csv(life_CSV)



count = 0
all_countries_d = {}

for index, year in enumerate(country_df['Year']):
    
    if year == 2015:
        count += 1
        country = country_df['Country'].values[index]
        gdp_per_capita = country_df['GDP'].values[index]
        life_exp = country_df['Life_expectancy'].values[index]
        
        all_countries_d[country] = [gdp_per_capita, life_exp]
        
        
        #print(country)
        #print("GDP:", gdp_per_capita)
        #print("Life expectancy:", life_exp, "\n")

print(count)

print(all_countries_d)

'''
df = pd.DataFrame(all_countries_d)

df_cleaned = df.dropna()
print(df)
'''

'''
for country in all_countries_list:
    if type(country[1]) != int:
        all_countries_list.pop()

print(all_countries_list)
'''

for key in all_countries_d:
    value = all_countries_d[key]
    x_coord = value[0]
    y_coord = value[1]
    plt.scatter(x_coord, y_coord)

#plt.xlim(0,20000)



#gdp_life_model = sm.ols(formula="Life_expectancy ~ percentage_expenditure", data=country_df).fit()
#print(gdp_life_model.summary())



'''
NEW
'''

    
    


def regression_results():
    # Load the data
    life_CSV = "life_expectancy_data.csv"
    country_df = pd.read_csv(life_CSV)

    # Filter the DataFrame for the year 2015
    data_2015 = country_df[country_df['Year'] == 2015]

    # Remove NaN values to avoid errors in regression analysis
    data_2015 = data_2015[['GDP', 'Life_expectancy']].dropna()

    # Performing regression analysis
    gdp_life_model = sm.ols(formula="Life_expectancy ~ GDP", data=data_2015).fit()
    print(gdp_life_model.summary())
    return






def life_exp():
    ### SCATTER PLOT TO COMPARE 
    
    # Load the data
    life_CSV = "life_expectancy_data.csv"
    country_df = pd.read_csv(life_CSV)
    
    # Filter the DataFrame for the year 2015
    data_2015 = country_df[country_df['Year'] == 2015]
    
    # Separate data for developed and developing countries
    developed_countries = data_2015[data_2015['Status'] == 'Developed'].dropna(subset=['GDP', 'Life_expectancy'])
    developing_countries = data_2015[data_2015['Status'] == 'Developing'].dropna(subset=['GDP', 'Life_expectancy'])
    
    # Scatter plot for developed countries
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, first plot
    plt.scatter(developed_countries['GDP'], developed_countries['Life_expectancy'], color='blue')
    plt.title('Developed Countries')
    plt.xlabel('GDP')
    plt.ylabel('Life Expectancy')
    
    # Scatter plot for developing countries
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, second plot
    plt.scatter(developing_countries['GDP'], developing_countries['Life_expectancy'], color='green')
    plt.title('Developing Countries')
    plt.xlabel('GDP')
    plt.ylabel('Life Expectancy')
    
    plt.tight_layout()
    plt.show()
    return


def percentage_change():
    # Load the data
    life_CSV = "life_expectancy_data.csv"
    country_df = pd.read_csv(life_CSV)
    
    # Pivot the DataFrame
    expenditure_pivot = country_df.pivot(index='Country', columns='Year', values='percentage_expenditure')

    # Calculate the change in health expenditure from 2000 to 2015 for each country
    change_in_expenditure = ((expenditure_pivot[2014] - expenditure_pivot[2000]) / expenditure_pivot[2000]) * 100
    
    print(change_in_expenditure)
    
    life_expectancy_pivot = country_df.pivot(index='Country', columns='Year', values='Life_expectancy')

    # Calculate the change in health expenditure from 2000 to 2015 for each country
    change_in_life_expectancy = ((life_expectancy_pivot[2014] - life_expectancy_pivot[2000]) / life_expectancy_pivot[2000]) * 100
    
    print(change_in_life_expectancy[0])
    
    plt.scatter(change_in_expenditure, change_in_life_expectancy)
    plt.title("Expenditure vs. Life Expectancy (from 2000-2015)")
    plt.xlabel("Percent change in healthcare expenditure")
    plt.ylabel("Percent change in life expentancy")
    plt.xlim(-100,5000)
    #plt.ylim(0,200)
    
    
def schooling():
    ### SCATTER PLOT TO COMPARE 
    
    # Load the data
    life_CSV = "life_expectancy_data.csv"
    country_df = pd.read_csv(life_CSV)
    
    # Filter the DataFrame for the year 2015
    data_2015 = country_df[country_df['Year'] == 2015]
    
    # Separate data for developed and developing countries
    developed_countries = data_2015[data_2015['Status'] == 'Developed'].dropna(subset=['Schooling', 'Life_expectancy'])
    developing_countries = data_2015[data_2015['Status'] == 'Developing'].dropna(subset=['Schooling', 'Life_expectancy'])
    
    plt.figure(figsize=(8, 5))
    
    # Plot developed countries in blue
    plt.scatter(developed_countries['Schooling'], developed_countries['Life_expectancy'], color='blue', label='Developed', marker='o')
    
    # Plot developing countries in green
    plt.scatter(developing_countries['Schooling'], developing_countries['Life_expectancy'], color='green', label='Developing', marker='x')
    
    plt.title('Comparison of Developed and Developing Countries')
    plt.xlabel('Years of Schooling')
    plt.ylabel('Life Expectancy')
    plt.legend()  # Show legend to differentiate between developed and developing countries
    
    plt.tight_layout()
    plt.show()
    return
    
    
    
    
    

if __name__ == "__main__":
    regression_results()
    life_exp()
    percentage_change()
    schooling()






















