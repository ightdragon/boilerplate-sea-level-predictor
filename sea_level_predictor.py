import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv') 

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extend = pd.Series([i for i in range(1880, 2051)])
    sea_levels_extend = intercept + slope * years_extend
    plt.plot(years_extend, sea_levels_extend,'r', label='Fit all Data')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000_extend = pd.Series([i for i in range(2000, 2051)])
    sea_levels_2000_extend = intercept_2000 + slope_2000 * years_2000_extend
    plt.plot(years_2000_extend, sea_levels_2000_extend, 'g', label='Fit 2000 Onwards')  

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()