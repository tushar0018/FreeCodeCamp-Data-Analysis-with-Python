import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col=0,parse_dates=
                True)

# Clean data
df = df = df[ df["value"].between( df["value"].quantile(.025), df["value"].quantile(.975) ) ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10,5))
    plt.plot(df.index, df['value'])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month_name()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  
    fig,ax = plt.subplots(figsize=(15,5))
    ax = sns.barplot(x="year", hue="month", y="value", data=df_bar,hue_order=months,errorbar=None)
    ax.set(xlabel = "Years",ylabel = "Average Page Views") 
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['monthnumber'] = df.index.month
    df_box = df_box.sort_values('monthnumber')
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(ax = axes[0],data=df_box, x="year", y="value").set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    sns.boxplot(ax = axes[1], x='month', y='value', data=df_box ).set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")

  
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig