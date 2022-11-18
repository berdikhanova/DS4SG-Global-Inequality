import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://github.com/berdikhanova/DS4SG-Global-Inequality/blob/Assignment/Data/Final/indicators.csv?raw=true")
df2 = pd.read_csv("https://raw.githubusercontent.com/berdikhanova/DS4SG-Global-Inequality/Assignment/Data/Final/df_countries.csv")
# Plot birth registration in Brazil over time with plotly express
def brazil_gdp():
    """
    Plots GDP per capita in Brazil over time
    """
    # Subsetting data
    brazil_gdp = df[(df['Country Code'] == 'BRA') & (df['Indicator Code'] == 'NY.GDP.PCAP.CD')]
    brazil_gdp = brazil_gdp[pd.to_numeric(brazil_gdp['Date'], errors='coerce').notnull()]

    # Plotting
    fig = px.line(brazil_gdp, x="Date", y="value", title='GDP per capita in Brazil')
    
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


def birth_registration():
    """
    Plots birth registration
    """
    # Subsetting data
    br_df = df2[(df2["Indicator Name"] == "Completeness of birth registration (%)") ]
    br_df = br_df.groupby("Country Code").last()
    br_df["Country Code"] = br_df.index.values
    br_df = br_df.sort_values(by=['value'])
    br_df = br_df.rename(columns={"value": "Completeness of birth registration (%)"})


    # Plotting
    fig = px.bar(br_df, x='Country Name', y='Completeness of birth registration (%)',
                 title = "Completeness of birth registration (%)")
    
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