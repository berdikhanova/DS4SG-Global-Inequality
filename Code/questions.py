import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
from pywebio.platform import *
import random 

# import visualizations
from Code.visualizations import *
from quiz_game import *

score = 0 
n_questions = 0

def show_score(score):
    put_markdown(f"## Score: {score}/{n_questions}")

def explanatory_page(topic, text, graph = False):
    clear()

    # Add logo on the top left 
    put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/Quizality_logo.png?raw=true", width = '250px')

    put_markdown(f"## {topic}")
    put_text(text)
    if graph:
        put_html(graph())

def make_question_checkbox(prompt, options, correct, explanation, graph = False, df = None):
    # Clears the page
    global score
    global n_questions
    clear()

    # Add logo on the top left 
    put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/Quizality_logo.png?raw=true", width = '250px')

    show_score(score)
    # Creates a checkbox prompt
    answer = radio(prompt, options = options)

    # Checks if the answer is correct
    if answer == options[correct-1]:
        # Add one to score
        score+=1
        encouragement = random.choice(["That's right!", "You got it!", "Correct!", "Nice job!", "You're a genius!", "You're a rockstar!", "You're a superstar!", "You're a legend!", "You're a champion!", "You're a boss!", "You're a pro!", "You're a master!", "You're a guru!", "You're a wizard!", "You're a ninja!", "You're a superhero!", "You're a rockstar!", "You're a superstar!", "You're a legend!", "You're a champion!", "You're a boss!", "You're a pro!", "You're a master!", "You're a guru!", "You're a wizard!",])
        put_markdown(f"**{encouragement}**").style('text-align: center;')
    else:
        put_text("Not quite").style('text-align: center;')

    # Add one to number of total questions so far 
    n_questions += 1

    if graph:
        if df:
            put_html(graph(df))
        else:
            put_html(graph())

    put_text(explanation).style('text-align: center;')

def make_question_input(prompt, options, correct, explanation, graph = False):
    # Clears the page
    clear()

    # Add logo on the top left 
    put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/Quizality_logo.png?raw=true", width = '250px')

    show_score()
    # Creates a checkbox prompt
    answer = input(prompt, type=options)

    # Checks if the answer is correct
    if abs(answer-correct) <= 5 :
        score += 1
        put_text("Good guess!, You are so close by ",round(abs(answer - correct), 1), "points!")
    else:
        put_text("Not quite, Your answer is ", round(abs(answer - correct),1), "points away.")

    if graph:
        put_html(graph())

    put_text(explanation)

def make_question_elephant(prompt, options, correct, explanation, graph = False):
    # Clears the page
    global score
    global n_questions
    clear()
    show_score(score)

    # Add logo on the top left 
    put_image('https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Resources/elephant.png')
   
    # Creates a checkbox prompt
    answer = radio(prompt, options = options)

    # Checks if the answer is correct
    clear()
    if answer == options[correct-1]:
        # Add one to score
        score+=1
        encouragement = random.choice(["That's right!", "You got it!", "Correct!", "Nice job!", "You're a genius!", "You're a rockstar!", "You're a superstar!", "You're a legend!", "You're a champion!", "You're a boss!", "You're a pro!", "You're a master!", "You're a guru!", "You're a wizard!", "You're a ninja!", "You're a superhero!", "You're a rockstar!", "You're a superstar!", "You're a legend!", "You're a champion!", "You're a boss!", "You're a pro!", "You're a master!", "You're a guru!", "You're a wizard!",])
        put_markdown(f"**{encouragement}**")
    else:
        put_text("Not quite")

    # Add one to number of total questions so far 
    n_questions += 1
    
    # Add logo on the top left 
    put_image('https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Resources/elephant_answer.png')

    put_text(explanation)

score_infinite = 0

def restart():
    global score_infinite
    score_infinite = 0
    infinite_mode()

df_raw = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Data/Final/indicators.csv")
info_df = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Data/Final/countries.csv")
df_raw = df_raw.merge(info_df, left_on="Country Code", right_on="iso_alpha", how = "inner")

def infinite_mode():
    global score_infinite
    correct = True
    old_country = df_raw.sample()["Country Name"].values[0]
    while correct:
        clear()
        # Add logo on the top left 
        put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/Quizality_logo.png?raw=true", width = '250px')

        put_markdown(f"## Score: {score_infinite}")
        # random country

        while True:
            try:
                # old country
                        # Random indicator
                indicator = df_raw.sample()["Indicator Name"].values[0]
                # latest date available for each country
                df = df_raw[df_raw["Indicator Name"] == indicator]
                df = df.groupby("Country Name").apply(lambda x: x[x["Date"] == x["Date"].max()]).reset_index(drop=True)
                old_country_indicator = df[df["Country Name"] == old_country]["value"].values[0]
            except:
                continue
            break

        put_markdown(f"**{old_country}** has a {indicator} of {round(old_country_indicator, 2)}.")

        # random country
        country = df.sample()["Country Name"].values[0]

        put_markdown(f"Is that higher or lower than **{country}**?")

        # correct answer is the country with the highest GDP per capita
        
        country_indicator = df[df["Country Name"] == country]["value"].values[0]
        correct_answer = "Lower" if old_country_indicator < country_indicator else "Higher"

        answer = radio("", options=["Higher", "Lower"])

        if answer != correct_answer and old_country_indicator != country_indicator:
            correct = False
            put_markdown(f"Sorry, but that's wrong!")
            put_markdown(f"{old_country} has a {indicator} of {round(old_country_indicator, 2)}, and {country} has a {indicator} of {round(country_indicator, 2)}")

            put_markdown("# Final Score: " + str(score_infinite))

            score_infinite = 0
            put_button("Play again", first_page)
        else:
            score_infinite += 1
            put_markdown(f"Answer {answer} is Correct!")
            put_markdown(f"{old_country} has a {indicator} of {old_country_indicator}, and {country} has a {indicator} of {country_indicator}")
        
        old_country = country

 

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
        "explanation": """
        Answer: 48.7 % of chilfren in Zimbabue have completed the birth registration and had a legal proof of identity. 
        Lack of birth registration can contribute to global inequality by denying children and their families access to legal protection, education, and other services that are essential for their well-being and development. 
        Legal rights: Birth registration is important for establishing a child's legal rights, including the right to a name, nationality, and protection from abuse and exploitation. Without birth registration, children may be denied access to these legal rights, which can impact their ability to access education, healthcare, and other services.
        """,
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
    },

    "question9":{
        "prompt":"Is comparing GDP per capita of countries the best way to measure inequality?",
        "options": ["Yes", "No"],
        "correct": 2,
        "explanation": """
        Comparing GDP per capita of different countries can be a useful way to compare their relative levels of economic output and wealth. However, it is important to note that GDP per capita is not a perfect measure of a country's wealth or well-being, and it should not be considered the sole measure of inequality.
        There are several reasons why comparing GDP per capita is not the best measure of inequality. First, GDP per capita only considers the economic output of a country and does not take into account other factors that can affect a person's quality of life, such as access to education, healthcare, and other public services.
        """,
        "graph": None
    },

    "question10":{
        "prompt":"What do you think this graph shows?",
        "options": [
            "The number of doctors working in disaster relief over the last 30 years", 
            "Predicted fluctuations in population for the next 30 years", 
            "The increase in real income from different percentiles of the world population over the last 30 years",
            "Proportion of people with access to a green space within 2km of their household, at different percentiles of income"],
        "correct": 3,
        "explanation": """
        The graph, created by Branko Milanovic and published in 2013, shows the increase in real income for different percentiles of income in the world from 1988 to 2008. The horizontal axis represents the income distribution, from poorest to richest. The 99th percentile (on the right of the graph) shows the richest 1%. We see that economic development affected people very differently. One of the main beneficiaries (in terms of relative change) were the global middle class, mainly due to the economic growth of China, India, and Eastern Europe. The very richest also had a huge boost in income, while the very poor are even poorer today. Interestingly, the 60th to 90th percentile of the population (the middle class in richer countries) did not grow their income very much. 
        The graph highlights the uneven nature of economic development and the widening gap between the very rich and the very poor, but also shows a conversion in the "middle" section of the population, as previously poor countries develop. 
        """,
        "graph": None
    },

    "question11":{
        "prompt":"Wei is the average person in Singapore, earning $102,000 per year. If we summed up the salaries of one average person from each of the poorest countries in the world, how many countries would we have to go through until having the same salary as Wei, adjusted for the cost of living of each country?",
        "options": NUMBER,
        "correct": 40,
        "explanation": """
        If we added up the salaries from one person from each of the lowest income countries in the world, we would need to go through 40 countries. This shows how vast the difference in earnings can be across countries. Usually, we talk about the difference between specific individuals, which is even greater, but the inequality in different regions of the world is also extremely high. 
        In the chart above, you see the proportion that each country would make-up in order to achieve Wei's yearly income. Note in the chat that the colors represent the continents. Do you see any patterns? 
        """,
        "graph": tree_map
    },

    "question12":{
        "prompt":"Which of the following is NOT a factor that can affect population growth rate?",

        "options": [ "Birth rates","Death rates", "Immigration",  "Natural disasters"],
        "correct": 4,
        "explanation": """
        Birth rates, death rates, and immigration are factors that can affect population growth rate.       
        Birth rates: Birth rates refer to the number of live births per 1,000 people in a population. A high birth rate can lead to rapid population growth, while a low birth rate can result in slower population growth or population decline. Birth rates can be influenced by a variety of factors, including cultural and societal norms, access to family planning and reproductive healthcare, and economic and education opportunities for women.
        Death rates: Death rates refer to the number of deaths per 1,000 people in a population. A high death rate can lead to population decline, while a low death rate can result in population growth. Death rates can be affected by factors such as access to healthcare, living conditions, and environmental factors.
        Immigration: Immigration refers to the movement of people into a country from another country. Immigration can have an impact on population growth rate by adding to the total population size. Immigration can be influenced by a variety of factors, including economic opportunity, political instability, and conflict in the home country.
        """,
        "graph": continent_pop
    },

    "question13":{
        "prompt":"The WHO estimates that at least 2.5 medical staff (physicians, nurses and midwives) per 1,000 people are needed to provide adequate coverage with primary care interventions. What percentage of countries in the world have fewer physicians than this level? Please answer between 0 and 100",
        "options": NUMBER,
        "correct":68,
        "explanation": """
        The WHO estimates that at least 2.5 medical staff (physicians, nurses and midwives) per 1,000 people are needed to provide adequate coverage with primary care interventions. 
        Hoever, 68% of countries on the globe have fewer physicians than the level so far. As you can see in the graph, there is significant global inequality in terms of the number of physicians per population. This can have significant impacts on the quality and accessibility of healthcare in different countries. One factor that contributes to global inequality in the number of physicians is the distribution of medical schools and training programs. Many high-income countries have a large number of medical schools and training programs, while low-income countries may have fewer such programs or may not have the resources to train as many physicians. As a result, there is often a higher density of physicians in high-income countries compared to low-income countries.
        """,
        "graph": physicians
    },


    "question14":{
        "prompt":"Which of the following factors has been shown to be associated with lower suicide rates?",
        "options": ["Higher levels of social support","Higher levels of economic stability", "Higher levels of education", "All of the above"],
        "correct": 4,
        "explanation": """
        Global inequality can be related to suicide rate in terms of socio-economic status, access to mental health services and treatment, stigma surrounding mental health, and access to social support and strong social connections.
        Studies have shown that lower socio-economic status is associated with higher suicide rates. This can be due to a range of factors, including financial stress, lack of access to resources and support, and social isolation. Inequality in terms of socio-economic status can therefore contribute to higher suicide rates in certain populations.
        Stigma surrounding mental health and seeking help can also contribute to higher suicide rates. In some cultures, seeking help for mental health problems may be viewed as a sign of weakness or shame, leading individuals to feel unable to seek help and support. 
        """,
        "graph": suicide
    },
    ## Add more questions here
    "question15":{
       "prompt": "True of False: Almost 1 in every 5 women is unemployed in Middle East & North Africa, excluding high income population.",
       "options": ["True", "False"],
       "correct": 1,
       "explanation": "Defined by the International Labour Organization as the share of the labor force that is without work but available for and seeking employment, unemployment can signal and be a result of a myriad of other factors, both good and bad. Nevertheless, in the absence of a proper safety net in lower income countries, high unemployment signals inadequate allocation of resources. In the Middle East and North Africa region, women continue facing gender inequality in many areas. Despite its recent progress in and focus on health and education, many issues remain in the region due to the political and economic upheaval, conflict, occupation, and the COVID-19 pandemic. Moreover, in their comprehensive analysis of the women in development in MENA region UNICEF reports: many States in the region still allow such norms and practices to restrict the rights of females relative to males, and limit access for women and girls to targeted education regarding their rights and other substantive empowerment initiatives. Thus, higher unemployment can occur in countries with a high level of economic development and low rates of poverty, in the MENA region it is segregated and affects only the female population, with a decreasing rate of unemployment for males.",
       "graph": female_unemployment
   },
   "question16":{
       "prompt": "Did the female labor force increase, decrease or stay the same since 2013 in Afghanistan?",
       "options": ["Increased", "Decreased", "Stayed the same"],
       "correct": 3,
       "explanation": "Afghanistan has been an area of international concern when it came to women’s rights due to continuous gender-based violence and many restrictive norms and laws enforced on a national level with varying sub-national practices. More specifically, at the time of this writing, women are mostly restricted from working outside the home, they must cover their faces in public, and they have to be accompanied by a male chaperone when they travel. The country is an example of the adverse effects of conflict on the wellbeing of the country on multiple levels, including economic and societal. Despite international efforts through donations and many programs initiated by the UN, due to recent political conflicts in Afghanistan, the efforts of the abovementioned programs fell back, and the female participation in labor has decreased dramatically, which signals lower female autonomy and higher dependence on the husbands. Women in Afghanistan currently remain neglected and in need of immediate intervention from the international authorities.",
       "graph": labor_force
   },
   "question17":{
       "prompt": "Estimate the percentage of post-secondary enrollment in Least Developed Countries as of 2021",
       "options": NUMBER,
       "correct": 11,
       "explanation": "UNESCO Institute of Statistics reports that despite an overall increasing trend the school enrollment in tertiary education in the Least Development Countries remains low, at about 11% of gross on average in those countries, compared to the EU’s 73%. One of the reasons for such low numbers could be that tertiary education, whether or not to be an advanced research qualification, normally requires, as a minimum condition of admission, the successful completion of education at the secondary level. Education in the Least Developed Countries, albeit progress in the recent decades at a primary and secondary levels, defined as one of the Millenium Development Goals as well as the Sustainable Development Goals, needs global attention. While enrollment in post-secondary education is linked to higher income and better life outcomes, many minorities in the least developed countries remain at a disadvantage when it comes to equal access to education.",
       "graph": post_enrollment
   }
}


explanations_dict = {
    "gdp_per_capita": """
    GDP per capita is a measure of a country's economic output per person. It is calculated by dividing a country's gross domestic product (GDP) by its population. GDP is the total value of goods and services produced by a country in a given year.
GDP per capita is often used as an indicator of a country's standard of living and economic well-being. Countries with higher GDP per capita are generally considered to be wealthier and have higher living standards than countries with lower GDP per capita.
However, GDP per capita is not a perfect measure of a country's wealth or well-being. It only considers the economic output of a country and does not take into account other factors that can affect a person's quality of life, such as access to education, healthcare, and other public services. Additionally, GDP per capita does not account for income inequality within a country, so two countries with the same GDP per capita may have very different levels of inequality.
GDP per capita can also be affected by a variety of other factors, such as a country's natural resources, level of industrialization, and trade policies. For these reasons, GDP per capita should not be considered the sole measure of a country's wealth or well-being.
In terms of global inequality, GDP per capita can be used as a rough indicator of the relative wealth of different countries. However, it is important to consider other factors and not rely solely on GDP per capita when comparing the wealth of different countries.
                    """,
    "Life_Expectancy": """
    A lot of researches found a positive relationship between life expectancy and GDP per capita, meaning that countries with higher GDP per capita tend to have higher life expectancy.
    Higher levels of GDP per capita are often associated with access to better healthcare, nutrition, education, and other factors that contribute to overall health and well-being.
    In the context of global inequality, there is a significant gap in life expectancy between high-income and low-income countries. For example, according to data from the World Bank, the average life expectancy in high-income countries is around 82 years, while the average life expectancy in low-income countries is around 67 years. This gap in life expectancy is often attributed to the fact that high-income countries have greater access to healthcare, education, and other factors that contribute to overall health and well-being.
                    """,
    "unemployment": """
    According to the OECD, the definition of “unemployment” is the following: “people above a specified age not being in paid employment or self-employment but currently available for work during the reference period. Unemployment is measured by the unemployment rate, which is the number of people who are unemployed as a percentage of the labour force”. There are several types of unemployment: cyclical, structural and frictional unemployment.
The Reserve Bank of Australia provides the following definitions:
Cyclical unemployment occurs with changes in economic activity over the business cycle. Structural unemployment occurs when there is a mismatch between the jobs that are available and the people looking for work. This mismatch could be because jobseekers don’t have the skills required to do the available jobs, or because the available jobs are a long way from the jobseekers.
Frictional unemployment occurs when people move between jobs in the labour market, as well as when people transition into and out of the labour force.
Thus, even when an economy is operating at its maximum efficiency, there will still be natural unemployment. In general accepted theory, when the growth rate of a country's economy increases, it is expected that employment will increase and the unemployment rate will decrease on average. 
                    """
    ## Add more explanations here
}



def first_page():
    clear()
    # add logo
    put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/Resources/quizality_logo.png?raw=true", width = '250px')
    put_markdown('# Welcome to the Quizality!').style( 'text-align: center; margin: auto;  width: 80%; font-size: 40px') 
    # add team introduction
    put_text('"Inequality" in itself is a term that can trigger a number of different ideas in the mind of the reader or listener based on their knowledge and prejudice. The meaning attached to ‘Economic Inequality’ is not self-explanatory. Individuals from developed countries often cannot envision the extent of deepening economic crises in the Global South. As students at an international university, we have had the unique opportunity to travel around the world and have witnessed firsthand the disparities in income, education, healthcare, and other socio-economic issues. Therefore, my peers and I signed up for a project for our tutorial class, ‘Data Science for Social Good’, for our Fall semester of 2022.')
    # add start buttons
    put_markdown('Are You Ready To Play?').style( 'text-align: center; margin: auto;  width: 80%; font-size: 40px') 
    put_text('In this game, there are two modes:').style('text-align: center;')
    put_text('1. Normal Mode, where you learn new economic concepts and test your knowledge with diverse set of questions.').style('text-align: center;')
    put_text('2. Infinite Mode to test your knowledge on how much your know about other contries across a variety of topics. Check your score and share with your friend!').style('text-align: center;')
    put_markdown('## Choose your Game Mode').style('text-align: center;')
    put_buttons(['Normal Mode', 'Infinite Mode'], onclick=[question1, infinite_mode]).style('text-align: center;')
    put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/Resources/team_photo.png?raw=true", width='500px').style( 'display: block; margin-left: auto;  margin-right: auto;  width: 60%;')
# ECONOMIC
# Income in poor v rich countries
def question1():
    make_question_checkbox(**question_dict["question1"])
    put_buttons(["Next"], onclick=[question2])

#income increased or decreased
def question2():
    make_question_checkbox(**question_dict["question2"])
    put_buttons(["Next"], onclick=[explain_gdp])


def explain_gdp():
    explanatory_page("GDP per capita", explanations_dict["gdp_per_capita"], graph = gdp_per_capita)
    put_button("Test my knowledge!", onclick=question9)

# gdp per capita
def question9():
    make_question_checkbox(**question_dict["question9"])
    put_buttons(["Next"], onclick=[question10])

def question10():
    make_question_elephant(**question_dict["question10"])
    put_buttons(["Next"], onclick=[question11])

def question11():
    make_question_input(**question_dict["question11"])
    put_buttons(["Next"], onclick=[question12])

# HEALTH
# Population Growth in each continents
def question12():
    make_question_checkbox(**question_dict["question12"])
    put_buttons(["Next"], onclick=[question4])

# Birth Registration
def question4():
    make_question_input(**question_dict["question4"])
    put_buttons(["Next"], onclick=[question3])

# Life Expectancy
def question3():
    make_question_checkbox(**question_dict["question3"])
    put_buttons(["Next"], onclick=[explain_life_expectancy])

# Life Expetancy explanation
def explain_life_expectancy():
    explanatory_page("Life Expectancy", explanations_dict["Life_Expectancy"], graph = life_expectancy_sub)
    put_button("Next Question!", onclick=question13)

# The number of physicians
def question13():
    make_question_input(**question_dict["question13"])
    put_buttons(["Next"], onclick=[question14])

# Suicide
def question14():
    make_question_checkbox(**question_dict["question14"])
    put_buttons(["Next"], onclick=[question7])

# EDUCATION
def question7():
    make_question_checkbox(**question_dict["question7"])
    put_buttons(["Next"], onclick=[question8])

def question8():
    make_question_input(**question_dict["question8"])
    put_buttons(["Next"], onclick=[explain_unemployment])

def explain_unemployment():
    explanatory_page("Unemployment", explanations_dict["unemployment"])
    put_button("Test my knowledge!", onclick=question15)

def question15():
   make_question_checkbox(**question_dict["question15"])
   put_buttons(["Next"], onclick=[question16])
 
def question16():
   make_question_checkbox(**question_dict["question16"])
   put_buttons(["Next"], onclick=[question17]) 
 
def question17():
   make_question_input(**question_dict["question17"])
   put_buttons(["Next"], onclick=[last_page])


def question5():
    #make_question(**question_dict["question3"])
    clear()
    put_text("In Development")

# Environment

## Add more functions here

def last_page():
    global score
    global n_questions
    clear()
    
    # Add logo on the top left 
    put_image("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/final_assignment/Quizality_logo.png?raw=true", width = '250px')

    put_markdown("## Thanks for playing!")

    sheet_url = "https://docs.google.com/spreadsheets/d/1A_CfyV9tRbG71JAbPN2s94h22JuAprrEKcXGQC5RlgA/edit#gid=0"
    url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    df = pd.read_csv(url_1)
    scores = df['score']

    put_markdown(f"## Your final score was {score}, that's better than {round((scores < score).sum() / len(scores) * 100, 1)}% of players!")

    put_markdown("## You can check out the [source code](https://github.com/berdikhanova/DS4SG-Global-Inequality) on GitHub.")

    score = 0
    n_questions = 0
    put_button("Play again", first_page)