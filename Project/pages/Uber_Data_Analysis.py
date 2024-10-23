# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:30:22 2024

@author: enzor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

st.markdown("<h1 style='color: #f58d44 ;'>Analyzing an uber Dataset</h1>", unsafe_allow_html=True)

# Get the current directory
current_dir = os.path.dirname(__file__)

with st.sidebar:
    st.write("This page is for a previous data visualization project I realized where the goal was to manipulate some Uber Data.")
    st.write("Where you can find me :")
    
    logo_path = os.path.join(current_dir, "images", "logo_linkedin.png")
    st.image(logo_path)
    url_linkedin = "www.linkedin.com/in/enzo-rivière-a55b07221"
    st.markdown("[Find me on Linkedin !](%s)"%url_linkedin)
    
    logo_path = os.path.join(current_dir, "images", "github_logo.png")
    st.image(logo_path)
    url_github = "https://github.com/Enzo-Riviere"
    st.markdown("[Find me on GitHub !](%s)"%url_github)
    
    st.write("Or contact me on my email adress :")
    st.write("enzo.riviere@efrei.net")

path2 = "https://raw.githubusercontent.com/uber-web/kepler.gl-data/master/nyctrips/data.csv"
data2 = pd.read_csv(path2, delimiter = ',')
st.write(data2.head())

@st.cache_data
def convert_datetime(data):
    # Convert the columns to datetime
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])
    return data


def get_hour(dt):
    return dt.hour #.hour is an attribute

@st.cache_data
def get_data_hour(data):
    data['pickup_hour'] = data['tpep_pickup_datetime'].map(get_hour)
    data['dropoff_hour'] = data['tpep_dropoff_datetime'].map(get_hour)
    return data

# Assuming 'data2' is your DataFrame
data2 = convert_datetime(data2)
st.write(data2.head())

st.write("We add two columns for pickup hour and dropoff hour :")

data2 = get_data_hour(data2)
st.write(data2.head())

st.write("We plot the frequency of pickups by hours :")

fig = px.histogram(data2, x='pickup_hour', nbins=24, range_x=(-0.5, 24), title='Frequency by Hour - Uber - January 15th 2015')
fig.update_layout(
    xaxis_title="Hour of the day for the pickup",
    yaxis_title="Frequency",
    bargap=0.2  # Adjusts the width of the bars
)
st.plotly_chart(fig)

st.write("We plot the frequency of dropoffs by hours :")

fig = px.histogram(data2, x='dropoff_hour', nbins=24, range_x=(-0.5, 24), title='Frequency by Hour - Uber - January 15th 2015')
fig.update_layout(
    xaxis_title="Hour of the day for the dropoffs",
    yaxis_title="Frequency",
    bargap=0.2  # Adjusts the width of the bars
)
st.plotly_chart(fig)

st.write("We can see which hours has the most pickups and dropoffs. For the two of them, it is at 10pm that it's the maximum.")

st.write("We plot the frequency by number of passengers :")

fig = px.histogram(data2, x='passenger_count', title='Frequency by number of passengers - Uber - January 15th 2015')
fig.update_layout(
    xaxis_title="Number of passengers",
    yaxis_title="Frequency",
    bargap=0.2  # Adjusts the width of the bars
)
st.plotly_chart(fig)

st.write("We can see that most of the time, there is only 1 passenger.")

st.write("Let's see how is distributed the data")

st.write(data2.describe())

st.write("Most of our data is around the pickup_latitude 40.7 :")

fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.hist(data2["pickup_latitude"], bins=100, range=(40.6, 40.9), color='r', alpha=0.5)
ax.set_xlabel('Pickup Latitude')
ax.set_ylabel('Frequency')
ax.set_title('Pickup Latitude - Uber - January 15th 2015')
st.pyplot(fig)

st.write("Most of our data is around the pickup_longitude -73.9 :")

fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.hist(data2["pickup_longitude"], bins=100, range=(-74.1,-73.7), color='g', alpha=0.5)
ax.set_xlabel('Pickup longitude')
ax.set_ylabel('Frequency')
ax.set_title('Pickup longitude - Uber - January 15th 2015')
st.pyplot(fig)

st.write("We have for the Pickups :")

fig, ax1 = plt.subplots(figsize=(10, 10), dpi=100)
ax1.set_title('Longitude and Latitude distribution for pickups - Uber - January 15th 2015', fontsize = 15)
ax1.hist(data2["pickup_latitude"], bins=100, range=(40.6, 40.9), color='r', alpha=0.5, label = 'Pickup Latitude')
ax1.legend(loc = 'best')
ax2 = ax1.twiny()
ax2.hist(data2["pickup_longitude"], bins=100, range=(-74.1,-73.7), color='g', alpha=0.5, label = 'Pickup Longitude')
ax2.legend(loc = 'upper left')
st.pyplot(fig)

st.write("Most of our data is around the dropoff_latitude 40.7 :")

fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.hist(data2["dropoff_latitude"], bins=100, range=(40.6, 40.9), color='r', alpha=0.5)
ax.set_xlabel('Dropoff Latitude')
ax.set_ylabel('Frequency')
ax.set_title('Dropoff Latitude - Uber - January 15th 2015')
st.pyplot(fig)

st.write("Most of our data is around the dropoff_longitude -73.9 :")

fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.hist(data2["dropoff_longitude"], bins=100, range=(-74.1,-73.7), color='g', alpha=0.5)
ax.set_xlabel('Dropoff longitude')
ax.set_ylabel('Frequency')
ax.set_title('Dropoff longitude - Uber - January 15th 2015')
st.pyplot(fig)

st.write("We have for the Dropoffs :")

fig, ax1 = plt.subplots(figsize=(10, 10), dpi=100)
ax1.set_title('Longitude and Latitude distribution for pickups and Dropoffs - Uber - January 15th 2015', fontsize = 15)
ax1.hist(data2["dropoff_latitude"], bins=100, range=(40.6, 40.9), color='r', alpha=0.5, label = 'Pickup Latitude')
ax1.legend(loc = 'best')
ax2 = ax1.twiny()
ax2.hist(data2["dropoff_longitude"], bins=100, range=(-74.1,-73.7), color='g', alpha=0.5, label = 'Pickup Longitude')
ax2.legend(loc = 'upper left')
st.pyplot(fig)

st.write("Now visualizing it with a scatter :")
fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.scatter(data2["pickup_latitude"], data2["pickup_longitude"], s=0.8, alpha = 0.4)
ax.set_ylim(-74.1,-73.8)
ax.set_xlim(40.6,40.9)
ax.set_xlabel('Pickup Latitude')
ax.set_ylabel('Pickup Longitude')
ax.set_title('Scatter plot for pickups - Uber - January 15th 2015')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.scatter(data2["dropoff_latitude"], data2["dropoff_longitude"], s=0.8, alpha = 0.4, color = "y")
ax.set_ylim(-74.1,-73.8)
ax.set_xlim(40.6,40.9)
ax.set_xlabel('Dropoff Latitude')
ax.set_ylabel('Dropoff Longitude')
ax.set_title('Scatter plot for Dropoffs - Uber - January 15th 2015')
st.pyplot(fig)

fig, ax1 = plt.subplots(figsize=(10, 10), dpi=100)
ax1.set_title('Longitude and Latitude distribution for dropoff - Uber - January 15th 2015', fontsize = 15)
ax1.scatter(data2["pickup_latitude"], data2["pickup_longitude"], s=0.8, alpha = 0.4) #Without list also shows the same plot
ax1.legend(loc = 'best') 
ax2 = ax1.twiny()
ax2.scatter(data2["dropoff_latitude"], data2["dropoff_longitude"], s=0.8, alpha = 0.2, color = 'y') #Without list also shows the same plot
ax2.legend(loc = 'upper left')
ax2.set_ylim(-74.1,-73.8)
ax2.set_xlim(40.6,40.9)
st.pyplot(fig)
