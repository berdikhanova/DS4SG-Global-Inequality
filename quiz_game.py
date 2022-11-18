
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



def main():

    question1()
    


if __name__ == '__main__':
    main()
    #start_server(main, debug=True, remote_access=True)
    
    
if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server as start_http_server
    from pywebio import start_server as start_ws_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_http_server(main, port=args.port)

