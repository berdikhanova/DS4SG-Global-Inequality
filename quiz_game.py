
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
    put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/Quizality_logo.png?raw=true", width = '250px')
    put_markdown('# Welcome to the Quizality!').style( 'text-align: center; margin: auto;  width: 80%; font-size: 40px') 
    put_text('"Inequality" in itself is a term that can trigger a number of different ideas in the mind of the reader or listener based on their knowledge and prejudice. The meaning attached to ‘Economic Inequality’ is not self-explanatory. Individuals from developed countries often cannot envision the extent of deepening economic crises in the Global South. As students at an international university, we have had the unique opportunity to travel around the world and have witnessed firsthand the disparities in income, education, healthcare, and other socio-economic issues. Therefore, my peers and I signed up for a project for our tutorial class, ‘Data Science for Social Good’, for our Fall semester of 2022.')
    put_markdown('# Meet Our Team!').style( 'text-align: center; margin: auto;  width: 80%; font-size: 40px')
    put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/team_photo.png?raw=true", width='500px').style( 'display: block; margin-left: auto;  margin-right: auto;  width: 60%;')
    put_markdown('Are You Ready To Play?').style( 'text-align: center; margin: auto;  width: 80%; font-size: 40px') 
    put_text('# In this game... there are two modes.........').style('text-align: center;')
    put_markdown('## Choose your Game Mode').style('text-align: center;')
    put_buttons(['Normal Mode', 'Infinite Mode'], onclick=[question1, infinite_mode]).style('text-align: center;')

if __name__ == '__main__':
    main()
        
        

