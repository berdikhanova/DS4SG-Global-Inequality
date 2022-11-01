
from pywebio.output import *
from pywebio.input import *
import sys as s
from typing import Tuple, List
import plotly.express as px

df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 trendline="ols",
                 title="Log-transformed fit on linear axes")
html = fig.to_html(include_plotlyjs="require", full_html=False)


def main():
    name = checkbox("Who has the highest inequality?", options = ["Brazil", "Kazakhstan"])
    
    if name[0] == "Brazil":
        put_text("That's right! Brazil is an unequal place")
    else:
        put_text(f"You chose {name}")
        put_text("Not quite")
    put_text("Now look at this graph and learn.")
    put_html(html)

if __name__ == '__main__':
    main()