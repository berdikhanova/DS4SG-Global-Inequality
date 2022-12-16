
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
CSS = """
    * {margin: 0; padding: 0; font-family: "Roboto", sans-serif; font-size: 18px; text-align: left; }
    """



def main():
    config(css_style=CSS)
    set_env(title='Quiz Game',output_max_width='90%')
    first_page()

if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server as start_http_server
    from pywebio import start_server as start_ws_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("--http", action="store_true", default=False, help='Whether to enable http protocol for communicates')
    args = parser.parse_args()

    if args.http:
        start_http_server(main, port=args.port)
    else:
        # Since some cloud server may close idle connections (such as heroku),
        # use `websocket_ping_interval` to  keep the connection alive
        start_ws_server(main, port=args.port, websocket_ping_interval=30)
        
        

