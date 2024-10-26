import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    years_extended = np.arange(1880, 2050, 1)

    fig, ax = plt.subplots()
    sctgrph = plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line = [lr.slope*xi + lr.intercept for xi in years_extended]
    plt.plot(years_extended, line, c='blue')

    # Create second line of best fit
    q1 = (df['Year'] >= 2000)
    lr = linregress(df[q1]['Year'], df[q1]['CSIRO Adjusted Sea Level'])
    line = [lr.slope*xi + lr.intercept for xi in years_extended]
    plt.plot(years_extended, line, c='red')
    # Add labels and title
    plt.xlabel("Year")  # add X-axis label
    plt.ylabel("Sea Level (inches)")  # add Y-axis label
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()