import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
from pywebio.platform import *

# import visualizations
from Code.visualizations import *

def make_question_checkbox(prompt, options, correct, explanation, graph = False, df = None):
    # Clears the page
    clear()

    # Creates a checkbox prompt
    answer = checkbox(prompt, options = options)

    # Checks if the answer is correct
    if answer[0] == options[correct-1]:
        put_text("That's right!")
    else:
        put_text("Not quite")

    if graph:
        if df:
            put_html(graph(df))
        else:
            put_html(graph())

    put_text(explanation)

def make_question_input(prompt, options, correct, explanation, graph = False):
    # Clears the page
    clear()

    # Creates a checkbox prompt
    answer = input(prompt, type=options)

    # Checks if the answer is correct
    if abs(answer-correct) <= 5 :
        put_text("Good guess!, You are so close by ",abs(answer - correct), "points!")
    else:
        put_text("Not quite, Your answer is ", abs(answer - correct), "points away.")

    if graph:
        put_html(graph())

    put_text(explanation)


question_dict = {
    "question1": {
        "prompt": "If all you cared about was income, would you rather be in the bottom 10% of a rich country or in the top 10% of a poor country? ",
        "options": ["Bottom 10% of a rich country", "Top 10% of a poor country"],
        "correct": 1,
        "explanation": "The first is correct",
        "graph": income_distribution
    },

    "question2": {
        "prompt": "Has the average income share held by the richest 10% increased or decreased in the last 20 years",
        "options": ["Increased", "Decreased", "Stayed the same"],
        "correct": 1,
        "explanation": "It has decreased",
        "graph": income_share
    },

    "question3":{
        "prompt": "Hong Kong and the Central African Republic have the highest and lowest life expectancy at birth. What is the difference in life expectancy between these two countries? ",
        "options": ["15 years", "20 years", "25 years", "30 years"],
        "correct": 4,
        "explanation": "Life expectancy ranges from 54.26  years in the Central African Republic to 85.29  years in Hong Kong – a staggering gap of 30 years. These extreme health inequities partly reflect wealth inequities between countries. Generally, wealthier countries have a higher average life expectancy than poorer countries, which can be argued to be achieved through higher standards of living, more effective health systems, and more resources invested in determinants of health (e.g. sanitation, housing, education).",
        "graph": life_expectancy
    },

    "question4":{
        "prompt": "How many percentage of children in Zimbabue completed the birth registration and had legal proof of idenity in 2019? Please answer between 0 and 100",
        "options": NUMBER,
        "correct": 48.7,
        "explanation": "This legal proof of identity can help protect children from violence, abuse and exploitation. Without a birth certificate, children are unable to prove their age, which puts them at a much higher risk of being forced into early marriage or the labour market, or recruited into armed forces.",
        "graph": birth_registration
    }
    
    ## Add more questions here
}


def question1():
    make_question_checkbox(**question_dict["question1"])
    put_buttons(["Next"], onclick=[question2])

def question2():
    make_question_checkbox(**question_dict["question2"])
    put_buttons(["Next"], onclick=[question3])

def question3():
    make_question_checkbox(**question_dict["question3"])
    put_buttons(["Next"], onclick=[question4])

def question4():
    make_question_input(**question_dict["question4"])
    put_buttons(["Next"], onclick=[question5])

def question5():
    #make_question(**question_dict["question3"])
    clear()
    put_text("In Development")
    