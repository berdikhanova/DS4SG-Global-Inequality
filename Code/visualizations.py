import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bubbly.bubbly import bubbleplot 
from plotly.offline import iplot
from plotly.subplots import make_subplots
import plotly.graph_objs as go



df = pd.read_csv("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/Assignment/Data/Final/indicators.csv?raw=true")
df2 = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/Assignment/Data/Final/df_countries.csv")

# Plot birth registration in Brazil over time with plotly express

def income_distribution():
    df = df2
    # Share of GDP held by lowest 10% for the latest date available, by country
    lowest_10 = df[(df["Indicator Name"] == "Income share held by lowest 10%")].groupby(
        "Country Code").last()
    # GDP per capita for the latest date available, by country
    lowest_10_gdp = df[(df["Indicator Name"] == "GDP per capita (current US$)")].groupby(
        "Country Code").last()
    # Income share held by lowest 10% multiplied by GDP per capita, by country
    lowest_10["GDP per capita"] = lowest_10_gdp["value"]
    lowest_10["Income share of lowest 10%"] = lowest_10["value"]
    lowest_10["Share of GDP per capita of lowest 10%"] = lowest_10["Income share of lowest 10%"] / \
        10 * \
        lowest_10["GDP per capita"]  # divide by 10 to get the gdp per person in the lowest 10%


    # Share of GDP held by highest 10% for the latest date available, by country
    highest_10 = df[(df["Indicator Name"] == "Income share held by highest 10%")].groupby(
        "Country Code").last()
    # GDP per capita for the latest date available, by country
    highest_10_gdp = df[(df["Indicator Name"] == "GDP per capita (current US$)")].groupby(
        "Country Code").last()
    # Income share held by highest 10% multiplied by GDP per capita, by country
    highest_10["GDP per capita"] = highest_10_gdp["value"]
    highest_10["Income share of highest 10%"] = highest_10["value"]
    highest_10["Share of GDP per capita of highest 10%"] = highest_10["Income share of highest 10%"] / \
        10 * \
        highest_10["GDP per capita"]  # divide by 10 to get the gdp per person in the highest 10%

    # Merge the two dataframes
    merged = lowest_10.merge(highest_10, on="Country Code")
    merged = merged[["Country Name_x", "Share of GDP per capita of lowest 10%",
                    "Share of GDP per capita of highest 10%", "GDP per capita_x"]]
    merged = merged.rename(
        columns={"Country Name_x": "Country Name", "GDP per capita_x": "GDP per capita", 
        "Share of GDP per capita of lowest 10%": "Lowest 10% in income", "Share of GDP per capita of highest 10%": "Highest 10% in income"})

    merged["GDP Percentile"] = merged["GDP per capita"].rank(
        pct=True).sort_values()

    # Plot the data
    # Figure size

    # Plot a scatter plot GDP percentile on the x-axis and share of GDP per capita of lowest 10% and highest 10% on the y-axis using plotly.express
    fig = px.scatter(merged, x="GDP Percentile", y=["Lowest 10% in income", "Highest 10% in income"],
                    hover_name="Country Name",
                    labels={
                        "Share of GDP per capita of lowest 10%": "Lowest 10%", 
                        "Share of GDP per capita of highest 10%": "Highest 10%", 
                        "GDP Percentile": "GDP Percentile"})

    # fix legend at top left
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))


    # Axis labels
    fig.update_xaxes(title_text="GDP Percentile")
    fig.update_yaxes(title_text="GDP * income share")

    # Line at 0.9 percentile
    fig.add_shape(type="line", x0=0.9, y0=0, x1=0.9, y1=350000,
                line=dict(color="gray", width=2))
    fig.add_shape(type="line", x0=0.1, y0=0, x1=0.1, y1=350000,
                line=dict(color="gray", width=2))


    html = fig.to_html(include_plotlyjs="require", full_html=False)

    return html

def income_share():
    # Average income share held by the richest 10% in the world over time since the 2000s
    highest_10 = df[(df["Indicator Name"] == "Income share held by highest 10%")].groupby("Date").mean()
    highest_10 = highest_10.reset_index()
    highest_10 = highest_10.rename(columns={"value": "Income share held by highest 10% (%)"})

    # plot from 2000 to 2020
    highest_10 = highest_10[(highest_10["Date"] >= 2000) & (highest_10["Date"] <= 2020)]
    #plot
    fig = px.line(highest_10, x="Date", y="Income share held by highest 10% (%)", title="Average income share held by the richest 10% in the world over time since the 2000s")
    fig.update_xaxes(title_text="Year")

    # To html
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html

def tree_map():
    new_df = df[df["Indicator Code"] == "NY.GNP.PCAP.PP.CD"]
    new_df = new_df.groupby("Country Name").apply(lambda x: x[x["Date"] == x["Date"].max()]).reset_index(drop=True)
    info_df = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Data/Final/countries.csv")
    # merge 
    new_df = new_df.merge(info_df, left_on="Country Code", right_on="iso_alpha", how = "inner")

    # Highest gdp per capita
    new_df = new_df.sort_values("value", ascending=False)
    highest = new_df.head(1)['value'].values[0]
    # Cumulative sum of gdp per capita
    new_df = new_df.sort_values("value", ascending=True)
    new_df['cumsum'] = new_df['value'].cumsum()

    lowest_df = new_df[new_df['cumsum']< highest]
    lowest_df['Highest'] = "Monaco"

    fig = px.treemap(lowest_df, path=['Highest', 'Country Name'], values='value',
                  color='continent', 
                  color_discrete_sequence= px.colors.qualitative.Set2
            )
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig.data[0].hovertemplate = '%{label}<br>Yearly Income ($): %{value}<br>Continent: %{customdata[0]}'
    
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html

def life_expectancy():
    """
    Plots world life expectancy
    """
    # Subsetting data
    le_total = df[(df["Indicator Code"] == "SP.DYN.LE00.IN")& (df["Date"] == 2020)]
    le_total = le_total.rename(columns={"value": "Average Life Expectancy"})

    # Plotting
    fig = px.choropleth(le_total, locations="Country Code",
                    color="Average Life Expectancy", 
                    hover_name="Country Name", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='Average Life Expectancy across the Globe in 2020')
    
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html


# Health Section
def life_expectancy_sub():
    """
    Plots world life expectancy
    """
    # Subsetting data
    df_health_countries = pd.read_csv('/Users/norika_machome/GitHub/DS4SG-Global-Inequality/Data/Final/Health/health_countries.csv')
    df_continent =  pd.read_csv("https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv")
    df_continent = df_continent[['alpha-3','region','sub-region']]
    df_health_countries = df_health_countries.merge(df_continent, left_on='Country Code', right_on='alpha-3')
    df_health_countries_gdp = df_health_countries[df_health_countries['Indicator Name']=='GDP per capita (current US$)']
    df_health_countries_lifeexp = df_health_countries[df_health_countries['Indicator Name']=='Life expectancy at birth, total (years)']
    df_health_countries_pop = df_health_countries[df_health_countries['Indicator Name']=='Population, total']
    df_health_gdp_lifeexp = df_health_countries_gdp.merge(df_health_countries_lifeexp, on = ['Date', 'Country Code'])
    df_health_gdp_lifeexp_pop = df_health_gdp_lifeexp.merge(df_health_countries_pop, on = ['Date', 'Country Code'])
    df_health_gdp_lifeexp_pop = df_health_gdp_lifeexp_pop[['Country Name_x', 'Country Code', 'Date', 'value_x','value_y','value', 'region_x', 'sub-region_x']].sort_values(by='Date')

    fig = px.scatter(df_health_gdp_lifeexp_pop, x="value_x", y="value_y", animation_frame="Date", animation_group="Country Name_x",
           size="value", color="region_x", hover_name="Country Name_x",
           log_x=True, size_max=55, range_x=[50,100000], range_y=[25,90]).update_layout(
           xaxis_title="GDP per Capita (Log Scale)", yaxis_title="Life Expectancy"
)
    #fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 50
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html

def birth_registration():
    """
    Plots birth registration
    """
    # Subsetting data
    df_health_countries = pd.read_csv('/Users/norika_machome/GitHub/DS4SG-Global-Inequality/Data/Final/Health/health_countries.csv')
    df_continent =  pd.read_csv("https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv")
    df_health_countries = df_health_countries.merge(df_continent, left_on='Country Code', right_on='alpha-3')
    df_health_countries_birth = df_health_countries[df_health_countries['Indicator Name']=="Completeness of birth registration (%)"]
    
    fig = px.box(df_health_countries_birth, x="region", y="value", color="region")
    fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
    fig.update_layout(height=500, width=800,
                      title = 'Birth Registration Completness across different continents',
                      barmode='overlay')
    fig.update_xaxes(title_text = 'Continents', tickangle = 60, row=1, col=1)
    fig.update_yaxes(title_text='Birth Registration', row=1, col=1)
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html

def continent_pop():
    df_health_countries = pd.read_csv('/Users/norika_machome/GitHub/DS4SG-Global-Inequality/Data/Final/Health/health_countries.csv')
    df_continent =  pd.read_csv("https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv")

    df_health_countries = df_health_countries.merge(df_continent, left_on='Country Code', right_on='alpha-3')
    df_health_countries_pop = df_health_countries[df_health_countries['Indicator Name']=='Population, total']
    fig = px.bar(df_health_countries_pop, x="region", y="value", color="region",
                 labels={
                     "value": "Population",
                     "region": "Continent",
                 },
                title="Population Growth between 1960 and 2022",
                animation_frame="Date", animation_group= "Country Name", range_y=[0,5000000000])
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 50
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    return html

def health_expenditure():
    df_health_countries = pd.read_csv('/Users/norika_machome/GitHub/DS4SG-Global-Inequality/Data/Final/Health/health_countries.csv')
    df_continent =  pd.read_csv("https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv")

    df_health_countries = df_health_countries.merge(df_continent, left_on='Country Code', right_on='alpha-3')
    df_health_countries = df_health_countries[df_health_countries["Indicator Name"] == "Physicians (per 1,000 people)"]
    df_health_countries = df_health_countries.groupby("Country Name").apply(lambda x: x[x["Date"] == x["Date"].max()]).reset_index(drop=True)
    fig = px.treemap(df_health_countries, path=[px.Constant("world"), 'region', 'Country Name'], values='value',
                  color='value', hover_data=['alpha-3'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df_health_countries['value'], weights=df_health_countries['value']))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    return html

def suicide():
    fig = make_subplots(rows = 1, cols=1)
    df_health_countries = pd.read_csv('/Users/norika_machome/GitHub/DS4SG-Global-Inequality/Data/Final/Health/health_countries.csv')

    df_health_suicide_total = df_health_countries[df_health_countries["Indicator Name"] == "Suicide mortality rate (per 100,000 population)"]
    df_health_suicide_female =df_health_countries[df_health_countries["Indicator Name"] == "Suicide mortality rate, female (per 100,000 female population)"].sort_values(by = 'value')
    df_health_suicide_male =df_health_countries[df_health_countries["Indicator Name"] == "Suicide mortality rate, male (per 100,000 male population)"].sort_values(by = 'value')

    fig.add_trace(go.Bar(
                         x = df_health_suicide_male["Country Name"],
                         y = df_health_suicide_male["value"],
                         name = 'Male Proportion'                     
                           ), row=1, col=1)

    fig.add_trace(go.Bar(
                         x = df_health_suicide_female["Country Name"],
                         y = -1 * np.array(df_health_suicide_female["value"]),
                         name = 'Female Proportion'                     
                           ), row=1, col=1)


    fig.update_layout(height=800, width=1200,
                      title = 'Suicides and its Proportion in different Countries among Genders',
                      barmode='overlay')

    fig.update_xaxes(title_text = 'Country', tickangle = 60, row=1, col=1)
    fig.update_yaxes(title_text='Suicide mortality rate (per 100,000 population)', row=1, col=1)

    html = fig.to_html(include_plotlyjs="require", full_html=False)
    return html


def mau_share():
    """
    Share of youth not in education, employment or training, total (% of youth population) in Mauritius vs. OECD countries
    """
    # Subsetting data
    mau_share = df[(df['Country Code'] == "MUS") | (df['Country Code'] == "OED")]
    mau_share = mau_share[(mau_share['Indicator Code'] == 'SL.UEM.NEET.ZS') & (mau_share['Date'] > 2003)]

    # Plotting
    fig = px.line(mau_share, x="Date", y="value", labels = {"Date":"Year", "value":"Share of youth population","Country Name":"Country"},color = "Country Name", title='Share of youth not in education, employment or training, total (% of youth population)', markers = True)
    
    html = fig.to_html(include_plotlyjs="require", full_html=False)

    return html

def teachers_share():
    """
    Trained teachers in secondary education (% of total teachers) in least developed countries*
    """
    # Subsetting data
    ldc_teachers = df[(df['Country Code'] == "LDC") & (df['Indicator Code'] == "SE.SEC.TCAQ.ZS")]

    # Plotting
    fig = px.bar(ldc_teachers, x='Date', y='value', text_auto='.3s', range_y=[0,100], labels = {"Date":"Years", "value":"Share of total teachers","Country Name":"Country"}, title='Trained teachers in secondary education (% of total teachers) in least developed countries*')
    
    html = fig.to_html(include_plotlyjs="require", full_html=False)

    return html


def gdp_per_capita():
    new_df = df[df["Indicator Name"] == "GDP per capita (current US$)"]
    new_df = new_df.groupby("Country Name").apply(lambda x: x[x["Date"] == x["Date"].max()]).reset_index(drop=True)
    # log values
    new_df["log_value"] = np.log10(new_df["value"])
    # Figure size

    fig = px.choropleth(
        new_df, locations="Country Code",
        color="log_value", 
        hover_name="Country Name", # column to add to hover information
        hover_data=["value"],
        color_continuous_scale=px.colors.sequential.Plasma,
        title='GDP per capita in the World',
        labels={'log_value':'Log of GDP per capita (current US$)', 'value':'GDP per capita (current US$)'},
        )

    fig.update_layout(height=600, 
                        width=1000,
                        coloraxis_colorbar=dict(
                            #len=0.75,
                            title='GDP per capita (current US$)', 
                            tickvals = [3, 4, 5],
                            ticktext = ['1k', '10k', '100k'],
                            yanchor="bottom",
                            y=0.1,
                            xanchor="left",
                            x=0.01,
                            len = .4),
                        margin=dict(l=10, r=10, t=50, b=10)
                    )

    html = fig.to_html(include_plotlyjs="require", full_html=False)

    return html