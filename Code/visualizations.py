import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/Assignment/Data/Final/indicators.csv?raw=true")

# Plot birth registration in Brazil over time with plotly express
def brazil_gdp():
    """
    Plots GDP per capita in Brazil over time
    """
    # Subsetting data
    brazil_gdp = df[(df['Country Code'] == 'BRA') & (df['Indicator Code'] == 'NY.GDP.PCAP.CD')]
    brazil_gdp = brazil_gdp[pd.to_numeric(brazil_gdp['Date'], errors='coerce').notnull()]

    # Plotting
    fig = px.line(brazil_gdp, x="Date", y="value", title='GDP per capita in Brazil')
    
    html = fig.to_html(include_plotlyjs="require", full_html=False)

    return html