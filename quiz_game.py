
# Pywebio
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
from pywebio.platform import *

# Other
import sys as s
from typing import Tuple, List

# Plotting libraries
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

# Visualizations
from Code.visualizations import *

# Import csv from url
df = pd.read_csv("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/Assignment/Data/Final/indicators.csv?raw=true")


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

    graph = brazil_gdp(df)
    
    put_html(graph)
    put_text("As you can see in this graph, although there were some fluctutions, Brazil's GDP per capita has increased over time.")


def question1():
    clear_page()
    answer = checkbox("Has GDP per capita increased or decreased in Brazil?", options = ["Increased", "Decreased", "Stayed the same"])
    
    if answer[0] == "Increased":
        put_text("That's right!")
    else:
        put_text("Not quite")

    graph = brazil_gdp(df)
    put_html(graph)
    put_text("As you can see in this graph, although there were some fluctutions, Brazil's GDP per capita has increased over time.")



def main():

    question1()

    put_button("Next", onclick=question2)


if __name__ == '__main__':
    start_server(main, debug=True, remote_access=True)