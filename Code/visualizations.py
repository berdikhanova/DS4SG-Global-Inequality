import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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