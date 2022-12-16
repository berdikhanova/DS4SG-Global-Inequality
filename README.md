# Quizality 🌍

## An interactive quiz game to illustrate the depth of global inequality 
*Data Science for Social Good, Fall 2022*

## Demo App
[Quizality](https://quizality-app.herokuapp.com/)

## Table of Contents:

[1. Research Question](#research-question)

[2. Why Do We Care about Global Inequality?](#why-do-we-care-about-global-inequality)

[3. Process](#process)

* [Step 1: Game Design](#step-1-game-design)
* [Step 2: Content Creation & Data](#step-2-content-creation-and-data)
* [Step 3: Web App Creation](#step-3-web-app-creation)

[4. Repository Structure](#repository-structure)

[5. How to run the application locally](#how-to-run-the-application-locally)

[6. License](#license)

[7. Cite](#cite)

## Research question:
*How can we effectively communicate the extent and depth of global inequality using data visualizations and summary statistics?*


## Why Do We Care about Global Inequality?
“Inequality” has become a popular buzzword among many media nowadays, and we are seeing more and more news reports about it. The Sustainable Development Goals (SGDs) have a call that aims at reducing inequality within and among countries, and the need to address global inequality on a global scale is clear. As Minervans, we have had the opportunity to travel around the world and have witnessed firsthand the disparities in income, and education, among others. Although we understand that reducing global inequality requires high-level transformative changes with appropriate political and economic policies, we believe there are several things we can do at the individual level. Our Data Science for Social Good project aims to create an interactive quiz game that helps users understand global inequality through active engagement with high-quality, evidence-based data visualizations and individual-level action items. Between 2008 and 2013, global inequality fell for the first time since the industrial revolution. The historic fall in global inequality was driven by robust growth in average incomes in populous developing countries such as China and India. Despite progress, two-thirds of global inequality is still due to differences in average incomes between countries. 

>While 50% of the global population owns 2% of the total wealth, another 1% of the population owns 38% of the total wealth. 

Moreover, when we look at a more granular breakdown of the data and examine gender equality (also one of the SDGs), we learn that while women’s share of labor in 1930 was 30%, it rose just five percentage points in 2020. ([World Inequality Report, 2022](https://wir2022.wid.world/)) Global inequality is certainly a complex concept, and we argue that by putting it in relative terms by comparing indicators across years and across countries (e.g., Global North vs. Global South) we can deliver the message to the general public the most effectively. 

## Process:
Although we acknowledge that reducing global inequality requires high-level transformative changes with appropriate political and economic policies, there are several things we can do at the individual level. Thus, we aim to explore the effects of global inequality across different levels of analysis (international, regional, and national) globally for four topics: health, income, environment, and education. Although it is by no means a complete list of topics where global inequality is present, we believe it is a solid start to start educating the general audience.

### Step 1: Game Design

We focused on game design. Firstly, we researched game interactivity to identify which design features would help users immerse themselves in the game. We realized that using choice architecture is crucial for establishing the basis of interactive games. We came across factfulnessquiz.com, which uses a quiz design to test audiences on facts about global trends in various topics. This inspired us to design our web app in a quiz form with a random question generator to keep the audience engaged and provide more explanation for each indicator and its subcategories. We also chose a multimodal approach, delivering information through an interactive aspect, visualizations, and text, as it is a more effective learning method for educational material, according to Carnegie Mellon University (2021).

### Step 2: Content Creation and Data

We set ourselves the challenge of identifying and analyzing the most comprehensive database available for measuring global inequality and development. The World Development Indicators database created by the World Bank has 1453 featured indicators for all member countries (based on data availability). We focused on eight indicators across four topics: health, environment, income, and environment. As data scientists, we aim to make such high-quality statistical data easily comprehensible for general audiences and demonstrate the potential of data storytelling.

### Step 3: Web App Creation

To make the Web App with the quiz game, we used the PyWebIO python library. The library allowed us to easily create the web components of our app using only Python so that we could focus on the content.

With the library, we can create all sorts of content and display them on the web, including images, tables, text, and buttons. Notably, the library allows us to get user input and use it to make customized visualizations and give instant feedback on their responses.

We used pandas to work with the dataset and pyplot to make visualizations, which we displayed in our web app using integration with PyWebIO. 

## Repository Structure:

**Main Directory**
| File | Content |
| ------------- | ------------- |
| quiz_game.py | Contains the actual PyWebIO application |
| requirements.txt | Contains all requirements (necessary for PyWebIO sharing) |

**data/Final/**
| File | Content |
| ------------- | ------------- |
| Datasets.zip| World Bank Development Indicators raw dataset |
| indicators.csv | Data containing the indicators for the app|
| Poverty.csv | Data on the Poverty Indicators |
| countries.csv | Data containing the list of countries |
| df_countries.csv | Data containing the list of countries |
| df_economic.csv | Data containing the list of countries |
| df_final_countries.csv | Data containing the list of countries |
| df_final_econstatus.csv | Data containing the list of countries |
| df_final_regions.csv | Data containing the list of countries |
| df_final_rest.csv | Data containing the list of countries |
| df_region.csv | Data containing the list of countries |

**Code**
| File | Content |
| ------------- | ------------- |
| DS4SG_Data_Importing.ipynb| Notebook used to change and filter the data and exctract a final dataset|
| questions.py | Python file used to include the questions & the order of the questions |
| visualizations.py | Python file containing visualizations for the questions |
| Tests.ipynb | Notebook used to ??? |
| Visualization Tests.ipynb | Notebook used to ??? |
| extracting_data.ipynb | Notebook used to ??? |
| norika_questions.ipynb | Notebook used to ??? |
| pyweb_example.py | Notebook used to ??? |

## How to Run the Application Locally
```
# clone the repository
git clone https://github.com/berdikhanova/DS4SG-Global-Inequality.git

# Go to the directory of the repository
cd DS4SG-Global-Inequality

# Install required packages
pip install -r requirements.txt

# Run app
python quiz_game.py
```

## License

Copyright (c) 2022 Berdikhanova, M., Oliveira, F., Narimatsu, N., & Ali, N.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Cite
Berdikhanova, M., Oliveira, F., Narimatsu, N., & Ali, N. (2022, November). Quizality. Quizality: An interactive quiz game to illustrate the depth 
&nbsp;&nbsp;&nbsp;&nbsp; of global inequality. https://quizality-app.herokuapp.com/ 
