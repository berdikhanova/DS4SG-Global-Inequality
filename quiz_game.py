
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

# Questions
from Code.questions import *

# Import csv from url
df = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Data/Final/indicators.csv")

#### MAKE LANDING PAGE ####
#@use_scope('score', clear=True)


def main():
    first_page()

if __name__ == '__main__':
    explain_gdp()
        
        

