
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
# df = pd.read_csv("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/Assignment/Data/Final/indicators.csv?raw=true")

#### MAKE LANDING PAGE ####
#@use_scope('score', clear=True)


def main():

    put_markdown('# Welcome to the Global Inequality Quiz Game!')
    put_markdown('## Choose your Game Mode')

    put_button('Normal Mode', onclick=question1)
    put_button('Infinite Mode', onclick= infinite_mode)
    
    


if __name__ == '__main__':
    main()
        
        

