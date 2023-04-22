import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')
    x=df["Year"]
    y=df["CSIRO Adjusted Sea Level"]
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.scatter(x,y)

    # Create first line of best fit
    x1 = range(1880, 2051, 1)
    res = linregress(x,y)
    plt.plot(x1, res.intercept + res.slope*x1, 'r',label='fitted line 1')
    # Create second line of best fit
    df2 = df.loc[df["Year"] >= 2000]
    x2 = df2["Year"]
    y2 = df2["CSIRO Adjusted Sea Level"]
    res2 = linregress(x2,y2) 
    years2 = pd.Series(range(2000,2051))
    ax.plot(years2, res2.intercept + res2.slope*years2,'b',label='second line of best fit')
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()