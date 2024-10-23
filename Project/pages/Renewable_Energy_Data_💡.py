# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:58:24 2024

@author: enzor
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
#If you do not have missingno you need to : !pip install missingno
import missingno as msno
import json
import os

# Get the current directory
current_dir = os.path.dirname(__file__)

path = 'Datasets/prod-region-annuelle-enr.csv'

st.set_page_config(
    page_title="Renewable Energy Data",
    page_icon="💡"
    )

with st.sidebar:
    st.write("This is my main data visualization project. The goal of this project is to manipulate and analyze the production of renewable energy in France to understand production trends and regional differences.")
    st.write("Where you can find me :")
    
    logo_path = os.path.join(current_dir, "../images", "logo_linkedin.png")
    st.image(logo_path)
    url_linkedin = "www.linkedin.com/in/enzo-rivière-a55b07221"
    st.markdown("[Find me on Linkedin !](%s)"%url_linkedin)
    
    logo_path = os.path.join(current_dir, "../images", "github_logo.png")
    st.image(logo_path)
    url_github = "https://github.com/Enzo-Riviere"
    st.markdown("[Find me on GitHub !](%s)"%url_github)
    
    st.write("Or contact me on my email adress :")
    st.write("enzo.riviere@efrei.net")

banner_path = os.path.join(current_dir, "../images", "energias.jpg")
st.image(banner_path)

st.markdown("<h1 style='color: #81d839;'>Analizing the French Regional Production of Renawable Energy</h1>", unsafe_allow_html=True)

st.write("The global shift toward renewable energy makes it crucial to understand production trends and regional differences.\
         Furthermore, as a lot of students from my generation I consider that the theme of ecology and the protection of the environment is an emergency, so I wanted to focus my studies on this theme.\
         I found the dataset of the French Regional Production of Renawable Energy on the data.gouv.fr website and it immediately grabbed my attention.\
        Analizing this data could be interesting and respond to questions such as 'what is the most common renewable energy source in France ?  '")

st.write("This is why on this page, we will take a look at the regional production of renewable energies in France dataset.\
         We will understand the dataset, handle the missing values or wrong datatypes and manipulate our data to visualize and understand better what are working with.")


with st.expander("Understanding the dataset"):
    st.markdown("<h2 style='color: #78b049;'>Understanding the dataset :</h2>", unsafe_allow_html=True)
             
    st.write("First let's take a look at our dataset :")
    
    
    data = pd.read_csv(path, delimiter = ';')
    st.write(data.head())
    
    st.write("The shape of our dataset is : ", data.shape)
    
    st.markdown('''
                So in our dataset we have : 
                - **"année"** : the year when the data was harvested
                - **"nom_insee_region"** : the name of the french region where the energy production was recorded
                - **"code_insee_region"** : the numerical code associated with each region in France
                - **"production_hydraulique_renouvelable"** : The quantity of hydraulic power produced (in GWh) in a region for a particular year
                - **"production_bioenergies_renouvelable"** : The quantity of bioenergies power produced (in GWh) in a region for a particular year
                - **"production_eolienne_renouvelable"** : The quantity of wind power produced (in GWh) in a region for a particular year
                - **"production_solaire_renouvelable"** : The quantity of solar power produced (in GWh) in a region for a particular year
                - **"production_electrique_renouvelable"** : The total renewable electricity production for a region during a specific year. This is typically the sum of hydraulic, bioenergies, wind, and solar energy production. (in GWh)
                - **"production_gaz_renouvelable"** : The quantity of gaz power produced (in GWh) in a region for a particular year
                - **"production_totale_renouvelable"** : The total quantity of renewable energy produced (in GWh)
                - We also have two last columns **"geo_shape_region"** and **"geo_point_region"**, two categories that are coordinates, for the first one to plot a map with the regions colored and the other one to plot a map with a point in these regions.
                    ''')

with st.expander("Handling data problems"):
    st.markdown("<h2 style='color: #78b049;'>Handling data problems :</h2>", unsafe_allow_html=True)
    
    
    st.write("These are the different types in the dataset : ",data.dtypes)
    st.write("As we can see, there is no type problems in our Dataset, all the numerical values are either integers or floats. The geo_shape_region and geo_point_region are a special kind of data that we will look to more in detail later.")
    
    st.write("Let's check if we have any missing values : ")
    fig, ax = plt.subplots()
    msno.bar(data, ax=ax)
    ax.set_title("Number of non missing values for each features")
    ax.set_ylabel("Number of non missing values")
    st.pyplot(fig)
    st.write("So we can conclude that we have some missing values (7 in total). \
             For these missing values, we will act as if they were zeros, since that in our case it is probably representing no production or availability of the .")
             
    st.write("To do this we are going to use the fillna function : ")
    st.code("data.fillna(0, inplace=True) #inplace=True means we apply the modification on data.", language= 'python')
    data.fillna(0, inplace=True)
    
    st.write("We are now going to verify if we don't have missing data anymore :")
    fig, ax = plt.subplots()
    msno.bar(data, ax=ax)
    ax.set_title("Number of non missing values for each features")
    ax.set_ylabel("Number of non missing values")
    st.pyplot(fig)
    st.write("Our data is now complete and ready to use !")

with st.expander("Manipulating the data"):
    st.markdown("<h2 style='color: #78b049;'>Manipulating the data :</h2>", unsafe_allow_html=True)
    
    
    st.markdown("<h3 style='color: #a0cb7c;'>Observing the evolution of the different renewable energies over the year</h3>", unsafe_allow_html=True)
    
    
    st.write("Now we will take a look at the different types of renewable energies and how they evolved over the years :")
    
    
    st.write("To do this, you will have to choose which type of energy you want to visualize : ")
    energy_type = st.selectbox(
        "Which type of energy would you like to select ?",
        ('production_hydraulique_renouvelable','production_bioenergies_renouvelable','production_eolienne_renouvelable','production_solaire_renouvelable','production_gaz_renouvelable'),
    )
    
    st.write("To be able to visualize how different types of renewable energies evolves over the years, we first need to group our data (to be able to use matplotlib because else it does not take in account the sum of the production for all the regions)")
    st.code("data_grouped = data.groupby('annee')[[energy_type, 'production_electrique_renouvelable', 'production_totale_renouvelable']].sum().reset_index()", language = "python")
    #To use with matplotlib because else it does not take in account all the regions
    data_grouped = data.groupby('annee')[[energy_type, 'production_electrique_renouvelable', 'production_totale_renouvelable']].sum().reset_index()
    
    fig, ax = plt.subplots()
    ax.bar(data_grouped["annee"], data_grouped[energy_type])
    ax.set_title(f"Evolution of the {energy_type} over the years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Production (GWh)")
    st.pyplot(fig)
    
    st.write("What we can see is that the evolution of the production of a renewable energy doesn't necessarily mean a growing over the years.\
             For example with the hydraulic production, it really fluctuates around the 25 000 GWh whereas with the wind power there is a real growth over the years.")
    st.write("We can go even further to see how much participated each region to the production of a renewable energy :")
    
    fig = px.bar(data, x="annee", y=energy_type, color = "nom_insee_region")
    event = st.plotly_chart(fig, on_select="rerun")
    
    st.write("We can observe that for some type energies, there are regions that seems to have their specialties.\
             For example, Auvergne Rhône Alpes is a major provider of hydraulic energy compared to other regions.")
    
    
    st.markdown("<h3 style='color: #a0cb7c;'>Observing the evolution of the total renewable energies over the year :</h3>", unsafe_allow_html=True)
    
    
    
    fig, ax = plt.subplots()
    ax.bar(data_grouped["annee"], data_grouped["production_electrique_renouvelable"])
    ax.set_title("Evolution of the Renewable electric production over the years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Production")
    st.pyplot(fig)
    
    st.write("At first I chose to plot this feature because I didn't understand what it was refering to.\
             Thanks to this plot, I understood that the 'production_electrique_renouvelable' represents the total production without the gas production (since it is a special data that only arrives in 2015 and it is not electric energy).")
    
    fig = px.bar(data, x="annee", y="production_electrique_renouvelable", color = "nom_insee_region")
    event = st.plotly_chart(fig, on_select="rerun")
    
    st.write("We can observe on with these two plots, that over the years, we had a clear growth of the electricity produced with renewable energy.\
             We can also see on the second plot, that Auvegne Rhône Alpes is the region producing the most.")
    st.write("Let's now take a look at the total production :")
    
    fig, ax = plt.subplots()
    ax.bar(data_grouped["annee"], data_grouped["production_totale_renouvelable"])
    ax.set_title("Evolution of the total renewable production over the years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Production")
    st.pyplot(fig)
    
    st.write("In a same way than with the electricity, we can see a clear growth of the energy produced by renewable energies over the years.\
             It is also interesting to notify a small decrease on the period 2020-2021-2022, we could maybe think to Covid being a reason of this decreasing,\
                 since people couldn't work as they want.")
    
    fig = px.bar(data, x="annee", y="production_totale_renouvelable", color = "nom_insee_region")
    event = st.plotly_chart(fig, on_select="rerun")
    
    #Transition vers après avec comparaison
    st.write("We can see that even on the total production, Auvergne Rhône Alpes stays the region producing the most.")
    st.write("Thanks to pyplot we were able to have a first look at how different regions contribute to the production of renewable energies. \
                 But it can be interesting to study more in detail the comparison between regions.")
    
    st.markdown("<h3 style='color: #a0cb7c;'>Overview region comparison :</h3>", unsafe_allow_html=True)
    
    
    data_sort_year = data.sort_values(by='annee')
    
    fig = px.line(data_sort_year, x="annee", y="production_totale_renouvelable", color = "nom_insee_region")
    event = st.plotly_chart(fig, on_select="rerun", key="line_compare")
    
    st.write("Analizing the total production of each regions over the years on a line plot, make us realize how the Auvergne Rhône Alpes region is above all the other region, no matter the year.")
    
    st.markdown("<h3 style='color: #a0cb7c;'>Comparing regions in more details</h3>", unsafe_allow_html=True)
    
    st.write("A thing that we can do to compare regions, is to analyze them for each year. So you will have to select which year you want to analyze :")
    year = st.selectbox(
        "Which year would you like to select ?",
        (2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023),
    )
    
    st.write("First we will need to select only the data corresponding to the chosen year", year, " :")
    
    st.code('data_year = data[data["annee"] == year]', language = 'python')
    
    #We select the data corresponding to the selected date
    data_year = data[data["annee"] == year]
    
    st.write("To observe more in details, we would like to see for each region in the year selected, what was the proportion of each renewable energy.\
             To do this we need to use the data_melt pandas function that allows us to reshape our dataset :")
    
    st.code("data_melted = data_year.melt(\n\
            id_vars=['nom_insee_region'],\n\
            value_vars=['production_hydraulique_renouvelable', 'production_bioenergies_renouvelable',\n\
                        'production_eolienne_renouvelable', 'production_solaire_renouvelable',\n\
                            'production_gaz_renouvelable'],\n\
            var_name='energy_type',\n\
            value_name='production')", language = 'python')
    
    st.write("What is doing the data_year.melt, is taking each column in the vale_vars, identified by the nom_insee_region, and putting them into one column that has for each name of region + type of energy a value of production.\
             As we can see below :")
    
    #We use the pandas melt function to reshape the data
    data_melted = data_year.melt(
                          id_vars=['nom_insee_region'],
                          value_vars=['production_hydraulique_renouvelable', 'production_bioenergies_renouvelable', 
                                      'production_eolienne_renouvelable', 'production_solaire_renouvelable', 
                                      'production_gaz_renouvelable'],
                          var_name='energy_type',
                          value_name='production')
    
    st.write(data_melted.head(20))
    
    
    st.write(f"Using this new data format, we could for example group the total of each type of energy for the year {year}")
    energy_production = data_melted.groupby('energy_type')['production'].sum().reset_index()
    st.write(energy_production.head(20))
    
    st.write("And visualize it in a pie plot !")
    fig = px.pie(energy_production, values = "production", color = 'energy_type', names = 'energy_type', title = f"Proportion of different renewable energies in {year}",)
    event = st.plotly_chart(fig, on_select="rerun")
    
    st.write("As we can see, the hydraulic production is the main renewable energy produced throughout the years.\
             However, we can see that more and more there is a growth of the other renewable energies, especially the wind power.")
             
    st.write("To analyze further, we can plot for each region the proportion of the different energy they use.")
    
    # Plot the bar chart
    fig = px.bar(data_melted, 
                 x='nom_insee_region', 
                 y='production', 
                 color='energy_type', 
                 title=f'Total Renewable Energy Production by Region for the year {year}',
                 labels={'production':'Total Production (GWh)', 'nom_insee_region':'Region', 'energy_type':'Energy Type'})
    
    
    st.plotly_chart(fig)
    
    st.write("And to continue going in more details we could analyze for a year and region given, the proportions of renewable energies produced.")
    
    region = st.selectbox(
        "Which year would you like to select ?",
        data["nom_insee_region"].unique(),
        placeholder="Choose your region...",
    )
    
    data_region = data_melted[data_melted["nom_insee_region"] == region]
    
    fig = px.pie(data_region, values = "production", color = 'energy_type', names = 'energy_type', title = f"Proportion of different renewable energies in {region} in {year}",)
    event = st.plotly_chart(fig, on_select="rerun")
    
    st.write("Each time we can observe that throughout the years, there is a real diversification of the renewable energies produced nowadays.")
    
    st.markdown("<h3 style='color: #a0cb7c;'>Geographic representations :</h3>", unsafe_allow_html=True)
    
    st.write("To plot our geographical data, we will use the 'geo_point_region' column but we need to separate it in two columns 'lat' and 'lon'.")
    
    data['lat'] = data['geo_point_region'].apply(lambda x: float(x.split(',')[0]))
    data['lon'] = data['geo_point_region'].apply(lambda x: float(x.split(',')[1]))
    st.write(data)
    
    st.write("Now that we have these two columns, we can plot our geographical data using the plotly scatter_mapbox.")
    
    year = st.slider("Slide to see the evolution over the years", 2008, 2023, 2023)
    
    fig = px.scatter_mapbox(data[data["annee"] == year], lat='lat', lon='lon', 
                            size='production_totale_renouvelable',  # Size of the circles based on production
                            hover_name='nom_insee_region',
                            hover_data={'production_totale_renouvelable': True},
                            color_discrete_sequence=["blue"], zoom=5, height=500)
    
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("Using a slider, the page is reloading so we can't observe the evolution clearly.")
    
    st.write("This is why we can use the plotly express option that allows us to have the same thing but working better and without reloading the page :")
    
    data_sort_year = data.sort_values(by='annee')
    fig = px.scatter_mapbox(data_sort_year, lat='lat', lon='lon', 
                            size='production_totale_renouvelable',  # Size of the circles based on the total production
                            hover_name='nom_insee_region',
                            hover_data={'production_totale_renouvelable': True},
                            color_discrete_sequence=["blue"], zoom=5, height=500,
                            animation_frame="annee")
    
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)
    
    st.write("What we can observe is that for the regions that already produced renewable energies, there is not a real evolution of the total production, whereas in the region that were not producing, there is a real growth over the years.")
    
    st.markdown('''
                As a conclusion, we can say that throughout the years, there are clear evolutions of the renewable energies produced :
                - We have a clear growth of renewable energies such as wind power, solar power, bioenergy power that increased so much since 2008 (whereas the hydraulic power is pretty stable)
                - We also could determine our "big winner", the region that produces the most renewable energies, Auvergne-Rhône-Alpes that still today produces more (mainly hydraulic powered) than other regions. There is a reason for that : 
                    after some research I found out that, thanks to its geography (in the middle of the Alpes), this region is home to the biggest Hydraulic Park producing 45% of hydrauelectricity power in France.
                - After that, we were able to observe the the diversification in each regions of the way of producing renewable energies.
                - Finaly, we analized geographically the evolution of the total renewable energy produced in each region over the years and realized that the places where there was a real growth were the least producing regions that produced more and more.
                    ''')
#Déjà développés développe pas temps mais claire démocratisation chez ceux qui étaient pas prod avant
with st.expander("To go further..."):
    st.markdown("<h2 style='color: #78b049;'>To go further...</h2>", unsafe_allow_html=True)
    st.write("I also wanted to try to analyze and compare the greenhouse gas emissions of each region in France to see if there was a link between the regions that produces the most renewable energies, and the regions emitting less greenhouse gas.")
    st.write("The problem that I encountered is that in the dataset I found, the emissions are not by regions but by municipality. So, I decided to try to use the gouvernment geo api that can find a region code from a municipality code.")
    st.write("This is the code :")
    
    st.code('''
            path2 = 'C:/Users/enzor/OneDrive - Efrei/Documents/M1 EFREI/DataViz/Project/Datasets/IGT-Pouvoir-de-réchauffement-global.csv'

            data_gg = pd.read_csv(path2, delimiter = ',')
            st.write(data_gg.head())
        
            st.write("The shape of our dataset is : ", data_gg.shape)
        
            fig, ax = plt.subplots()
            msno.bar(data_gg, ax=ax)
            st.pyplot(fig)
        
        
        
            def get_region_from_commune(code_insee_commune):
                url = f"https://geo.api.gouv.fr/communes/{code_insee_commune}?fields=nom,codeRegion"
                response = requests.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    return data['codeRegion']
                else:
                    return None
        
            data_gg["region_code"] = data_gg["INSEE commune"].apply(get_region_from_commune)
            st.write(data_gg.head())
            ''', language = "python")
            
    st.write("This solution works but I chose to not implement it because applying it on the column takes a really long time. This could be an interesting analyze to do in the future.")
    
