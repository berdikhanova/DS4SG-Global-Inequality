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
        "explanation": 
        '''
        Although we often discuss inequality within a country, the disparity between countries is usually much larger. The discrepancy between poor and rich countries is more prominent than any inequality within one country. This might be unintuitive, but if we care solely about having the highest income, then being a poor person in a rich country is much better than being a rich person in a poor country. 
        Look at the graph above. We plotted the percentile of GDP per capita on the horizontal axis and the amount of GDP that would go to each person in a country if they received it proportionally to their income on the vertical axis. We plot two groups: the top 10% and the bottom 10% of earners in each country. Feel free to hover your mouse over the data points to see which country each dot represents and the income of that group. The two black lines show the top and bottom 10% of countries in terms of GDP per capita. 
        If you hover your mouse around the line on the right, you will see the UK, which is in the 90th percentile of the wealthiest countries. The bottom 10% earners of their population would receive $12.306 if we divided their GDP proportionally to their earnings. On the other end, Uganda is in the 10th percentile of GDP per capita, and the wealthiest 10% population would get only $2.960. That's 4 times less!    
        ''',
        "graph": income_distribution
    },

    "question2": {
        "prompt": "Has the average income share held by the richest 10% increased or decreased in the last 20 years",
        "options": ["Increased", "Decreased", "Stayed the same"],
        "correct": 2,
        "explanation": "The last 20 years saw a reversal of a trend of increasing inequality. In the previous 20 years, the wealthiest 10% have received a smaller share of the country's total income. However, 2020 saw a big jumpy upward. Will inequality increase again?",
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
    },

    "question7":{
        "prompt": "Estimate the share of teachers in secondary education who did not receive training in Least Developed Countries?",
        "options": ["10%", "40%", "60%", "80%"],
        "correct": 2,
        "explanation": "According to the UNESCO Institute for Statistics, there are only 62% of trained teachers in secondary education in 2019 in the Least Developed Countries (as per the UN’s classification, see the full list of countries below), compared to the global 83% average. Trained teachers refer to the teaching force with the necessary pedagogical skills to teach and use teaching materials in an effective manner. The share of trained teachers reveals a country's commitment to investing in the development of its human capital engaged in teaching. Teachers’ incompetence and absenteeism remain one of the biggest challenges in developing countries as incompetent teachers present a host of problems for school and district leaders, such as producing poor student achievement results, distracting other faculty members, and consuming large amounts of administrative time (Painter, 2000; Yariv, 2004). While the problem is absent in developed countries with 100% of teachers having the necessary pedagogical skills at all levels of education, countries like Niger and Madagascar have 17% and 20% of trained teachers respectively, making it almost impossible for students to escape a poverty trap.  UN list of least developed countries by regions:  Africa (33): Angola, Benin, Burkina Faso, Burundi, Central African Republic, Chad, Comoros, Democratic Republic of the Congo, Djibouti, Eritrea, Ethiopia, Gambia, Guinea, Guinea-Bissau, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mozambique, Niger, Rwanda, Sao Tome and Principe, Senegal, Sierra Leone, Somalia, South Sudan, Sudan, Togo, Uganda, United Republic of Tanzania and Zambia. Asia (9): Afghanistan, Bangladesh, Bhutan, Cambodia, Lao People’s Democratic Republic, Myanmar, Nepal, Timor-Leste, and Yemen. Caribbean (1): Haiti. Pacific (3): Kiribati, Solomon Islands, and Tuvalu",
        "graph": teachers_share 
    }, 

    "question8":{
        "prompt": "What percentage of total youth in Mauritius are not pursuing education or work?",
        "options": NUMBER,
        "correct": 41.72,
        "explanation": "According to the International Labour Organization and the World Bank, youth unemployment is an important policy issue for many economies. Now more than ever, young men and women face increasing uncertainty in their hopes of undergoing a satisfactory transition in the labor market, and that effect is enhanced in developing markets. While underemployment and unemployment in the 20s were proven to increase depression rates and suicide rates, the effect of generational unemployment is yet to be studied. According to the economist at the World Bank, unemployed or underemployed youth are less able to contribute effectively to national development and have fewer opportunities to exercise their rights as citizens. They have less to spend as consumers, less to invest as savers, and often have no voice to bring about change in their lives and communities. As seen on the graph, almost 42% of the youth in Mauritius are not participating in education or labor as of 2020, compared to the OECD’s average of 15%. We can also see a rapid increase in this indicator in 2020 - the same trend can be observed in other developing countries, like the Dominican Republic, where the number jumped from roughly 25% to 38% in the same time period. While we do see a slight increase in OECD’s average, the rapid jumps in this indicator in developing countries once again illustrate the striking effect of the pandemic on the developing world.",
        "graph": mau_share
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
    put_buttons(["Next"], onclick=[question7])

def question7():
    make_question_checkbox(**question_dict["question7"])
    put_buttons(["Next"], onclick=[question8])

def question8():
    make_question_input(**question_dict["question8"])
    put_buttons(["Next"], onclick=[question5])

def question5():
    #make_question(**question_dict["question3"])
    clear()
    put_text("In Development")
    