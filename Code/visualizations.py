import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objs as go



df = df_final = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Data/Final/indicators.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Data/Final/df_countries.csv")
#df_final =  pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Data/Final/df_final.csv")


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
    info_df = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/final_assignment/Data/Final/countries.csv")
    # merge 
    new_df = new_df.merge(info_df, left_on="Country Code", right_on="iso_alpha", how = "inner")
    new_df = new_df.groupby("Country Name").apply(lambda x: x[x["Date"] == x["Date"].max()]).reset_index(drop=True)

    # Highest gdp per capita
    new_df = new_df.sort_values("value", ascending=False)
    highest = new_df.head(1)['value'].values[0]
    # Cumulative sum of gdp per capita
    new_df = new_df.sort_values("value", ascending=True)
    new_df['cumsum'] = new_df['value'].cumsum()

    lowest_df = new_df[new_df['cumsum']< highest]
    lowest_df['Highest'] = "Singapore"

    fig = px.treemap(lowest_df, path=['Highest', 'Country Name'], values='value',
                  color='continent_y', 
                  color_discrete_sequence= px.colors.qualitative.Set2
            )
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig.data[0].hovertemplate = '%{label}<br>Yearly Income ($): %{value}<br>Continent: %{customdata[0]}'
    
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html

# Health Section
def life_expectancy():
    """
    Plots world life expectancy
    """
    # Subsetting data
    df = df_final[(df_final["Indicator Code"] == "SP.DYN.LE00.IN")& (df_final["Date"] == 2020)]
    df = df.rename(columns={"value": "Average Life Expectancy"})

    # Plotting
    fig = px.choropleth(df, locations="Country Code",
                    color="Average Life Expectancy", 
                    hover_name="Country Name", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='Average Life Expectancy across the Globe in 2020')
    
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html

def life_expectancy_sub():
    """
    Plots world life expectancy vs gdp per capita
    """
    # Subsetting data
    df = df_final[~df_final.continent.isna()]

    df_gdp = df[df['Indicator Name']=='GDP per capita (current US$)']
    df_lifeexp = df[df['Indicator Name']=='Life expectancy at birth, total (years)']
    df_pop = df[df['Indicator Name']=='Population, total']

    df_merged = df_gdp.merge(df_lifeexp, on = ['Date', 'Country Code'])
    df_merged = df_merged.merge(df_pop, on = ['Date', 'Country Code']).drop(columns=[col for col in df_merged if col not in ['Country Code','Indicator Name_x', 'Date', 'value_x', 'Indicator Name_y', 'value_y', 'Country Name', 'Indicator Code','value','continent']])
    df_merged

    fig = px.scatter(df_merged, x="value_x", y="value_y", animation_frame="Date", animation_group="Country Name",
               size="value", color="continent", hover_name="Country Name",
               log_x=True, size_max=55, range_x=[50,100000], range_y=[25,90]).update_layout(
        xaxis_title="GDP per Capita (Log Scale)", yaxis_title="Life Expectancy")

    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 50
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html

def birth_registration():
    """
    Plots birth registration box chart
    """
    # Subsetting data
    df = df_final[~df_final.continent.isna()]
    df = df[df['Indicator Name']=="Completeness of birth registration (%)"]
    
    fig = px.box(df, x="continent", y="value", color="continent")
    fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
    fig.update_layout(height=500, width=800,
                      title = 'Birth Registration Completness across different continents',
                      barmode='overlay')
    fig.update_xaxes(title_text = 'Continents', tickangle = 60, row=1, col=1)
    fig.update_yaxes(title_text='Birth Registration', row=1, col=1)
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    
    return html

def continent_pop():
    """
    Plots population growth in each continent
    """
    df = df_final[~df_final.continent.isna()]
    df = df[df['Indicator Name']=='Population, total']
    fig = px.bar(df, x="continent", y="value", color="continent",
                 labels={
                     "value": "Population",
                     "continent": "Continent",
                 },
                title="Population Growth between 1960 and 2022",
                animation_frame="Date", animation_group= "Country Name", range_y=[0,5000000000])
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 50
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    return html

def physicians():
    """
    Plots physicians
    """
    df = df_final[~df_final.continent.isna()]
    df = df[df["Indicator Name"] == "Physicians (per 1,000 people)"]
    df = df.groupby("Country Name").apply(lambda x: x[x["Date"] == x["Date"].max()]).reset_index(drop=True)
    fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'Country Name'], values='value',
                  color='value', hover_data=['Country Code'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['value'], weights=df['value']))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    return html

def suicide():
    fig = make_subplots(rows = 1, cols=1)
    df = df_final 

    df_female =df[df["Indicator Name"] == "Suicide mortality rate, female (per 100,000 female population)"].sort_values(by = 'value')
    df_male =df[df["Indicator Name"] == "Suicide mortality rate, male (per 100,000 male population)"].sort_values(by = 'value')

    fig.add_trace(go.Bar(
                         x = df_male["Country Name"],
                         y = df_male["value"],
                         name = 'Male Proportion'                     
                           ), row=1, col=1)

    fig.add_trace(go.Bar(
                         x = df_female["Country Name"],
                         y = -1 * np.array(df_female["value"]),
                         name = 'Female Proportion'                     
                           ), row=1, col=1)


    fig.update_layout(height=800, width=800,
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

def female_unemployment():
   """
   Female unemployment (% of total labor force) in Middle East & North Africa (excluding high income)
   """
   # Subsetting data
   mna_female = df[(df['Country Code'] == "MNA") & (df['Indicator Code'] == "SL.UEM.TOTL.FE.ZS")]
 
   # Plotting
   fig = px.line(mna_female, x='Date', y='value', range_y=[0,100], labels = {"Date":"Years", "value":"Female unemployment ($%$ of total labor force)","Country Name":"Country"}, title='Female unemployment (% of total labor force) in Middle East & North Africa (excluding high income)')
  
   html = fig.to_html(include_plotlyjs="require", full_html=False)
 
   return html
 
def labor_force():
   """
   Female labor force (% of total labor force) in Afghanistan vs. European Union
   """
   # Subsetting data
   afg_female = df[(df['Country Code'] == "AFG") | (df['Country Code'] == "EUU")]
   afg_female = afg_female[(afg_female['Indicator Code'] == "SL.TLF.TOTL.FE.ZS")]
 
   # Plotting
   fig = px.line(afg_female, x='Date', y='value', range_y=[0,100], labels = {"Date":"Years", "value":"Female labor force (% of total labor force)","Country Name":"Country"}, color = "Country Name", title='Female labor force (% of total labor force) in Afghanistan vs. European Union')
  
   html = fig.to_html(include_plotlyjs="require", full_html=False)
 
   return html
 
def post_enrollment():
   """
   Post-secondary school enrollment (% of gross) in Least Developed Countries
   """
   # Subsetting data
   enrollmentpost = df[(df['Country Code'] == "LDC") | (df['Country Code'] == "EUU")]
   enrollmentpost = enrollmentpost[(enrollmentpost['Indicator Code'] == "SE.TER.ENRR")]
 
   # Plotting
   fig = px.line(enrollmentpost, x='Date', y='value', range_y=[0,100], labels = {"Date":"Years", "value":"Post-secondary school enrollment (% of gross)","Country Name":"Country"}, color = "Country Name", title='Post-secondary school enrollment (% of gross) in Least Developed Countries vs. European Union')
  
   html = fig.to_html(include_plotlyjs="require", full_html=False)
 
   return html

