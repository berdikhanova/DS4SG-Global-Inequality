
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
from pywebio.platform import *
import sys as s
from typing import Tuple, List
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

# Sample graph
df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 trendline="ols",
                 title="Log-transformed fit on linear axes")
html = fig.to_html(include_plotlyjs="require", full_html=False)

# Import csv from url
df = pd.read_csv("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/Assignment/Data/Final/indicators.csv?raw=true")

# FIGURE 1

# Plot birth registration in Brazil over time with plotly express
brazil_gdp = df[(df['Country Code'] == 'BRA') & (df['Indicator Code'] == 'NY.GDP.PCAP.CD')]

brazil_gdp = brazil_gdp[pd.to_numeric(brazil_gdp['Date'], errors='coerce').notnull()]

fig1 = px.line(brazil_gdp, x="Date", y="value", title='GDP per capita in Brazil')



html1 = fig1.to_html(include_plotlyjs="require", full_html=False)
def clear_page():
    clear()

def question2():
    clear_page()
    put_text("This is question 2")
    answer = checkbox("Has GDP per capita increased or decreased in Brazil?", options = ["Increased", "Decreased", "Stayed the same"])
    
    if answer[0] == "Increased":
        put_text("That's right!")
    else:
        put_text("Not quite")
    
    put_html(html1)
    put_text("As you can see in this graph, although there were some fluctutions, Brazil's GDP per capita has increased over time.")


def question1():
    clear_page()
    answer = checkbox("Has GDP per capita increased or decreased in Brazil?", options = ["Increased", "Decreased", "Stayed the same"])
    
    if answer[0] == "Increased":
        put_text("That's right!")
    else:
        put_text("Not quite")
    
    put_html(html1)
    put_text("As you can see in this graph, although there were some fluctutions, Brazil's GDP per capita has increased over time.")



def main():

    question1()

    put_button("Next", onclick=question2)


if __name__ == '__main__':
    start_server(main, debug=True, remote_access=True)