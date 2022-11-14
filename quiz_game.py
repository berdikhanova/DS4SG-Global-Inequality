
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
import sys as s
from typing import Tuple, List
import plotly.express as px
import pandas as pd

# Sample graph
df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 trendline="ols",
                 title="Log-transformed fit on linear axes")
html = fig.to_html(include_plotlyjs="require", full_html=False)

# Import csv from url
df_test = pd.read_csv("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/df_indicator/Data/Final/test.csv?raw=true")
fig1 = px.scatter(df_test, x="column_1", y="column_2")
html1 = fig1.to_html(include_plotlyjs="require", full_html=False)

def main():
    name = checkbox("Who has the highest inequality?", options = ["Brazil", "Kazakhstan"])
    
    if name[0] == "Brazil":
        put_text("That's right! Brazil is an unequal place")
    else:
        put_text(f"You chose {name}")
        put_text("Not quite")
    put_text("Now look at this graph and learn.")
    put_html(html1)

if __name__ == '__main__':
    main()
    
#hello