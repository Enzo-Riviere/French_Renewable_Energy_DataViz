# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:19:10 2024

@author: enzor
"""

import streamlit as st
# importing numpy and pandas to work with sample data.
import numpy as np
import pandas as pd
import os


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)



st.markdown("<h1 style='color: #5d91bf;'>Some information about myself</h1>", unsafe_allow_html=True)
st.write("Hi ! My name is Enzo Rivière, and I am in the first year of my master's degree at EFREI Paris, pursuing a degree in data engineering with an expected graduation in 2026.")
st.write("If you want to learn more about me, you can check that below ! :point_down:")

# Get the current directory
current_dir = os.path.dirname(__file__)

with st.sidebar:
    st.write("Hello ! :wave:")
    st.write("In this app, you will be able to learn about me, discover some of my works\
             on two uber datasets and on a dataset about renewable energies in Frances,\
            we will manipulate and analyze them to create my first Dashboard !")
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
    
    
col1, col2, col3 = st.tabs(["My studies", "My projects", "My Hobbies"])

with col1:
    st.markdown("<h2 style='color: #90b5d5;'>My studies :</h2>", unsafe_allow_html=True)
    
    st.write("My academic background includes a high school diploma with honors in Mathematics and Physics-Chemistry from Lycée Marcelin Berthelot in Saint-Maur Des Fossés.\
             I have developed a strong foundation in scientific and technical fields, allowing me to easily grasp new concepts and technologies.")
             
    st.markdown('''
                Here are some key academic skills :
                - **IT Skills** :computer: : I have extensive knowledge in Python, C, Linux, Matlab, and Java, combined with expertise in web development technologies such as HTML, CSS, JavaScript, Vue, and Express. 
                I am proficient in working with databases like MySQL and have hands-on experience designing digital circuits using VHDL.
                
                -  **Tools** :wrench: : I regularly work with GitHub for version control and collaboration, 
                and I am proficient in using the Microsoft Office Suite for presentations, data analysis, and documentation.
                
                - **Languages** : Fluent in English, scoring 920 on the TOEIC exam, along with a B2 level in Italian and intermediate Japanese. 
                My multilingual abilities make it easier for me to work in international teams and environments.
                
                - **International Experience** :world_map: : I spent the Fall semester of 2026 studying abroad at Concordia University, Montreal, Canada. 
                This experience broadened my academic and cultural perspectives.
                ''')
                
    st.write("If you want more information, you can download my resume :")

    cv_path = os.path.join(current_dir, "images", "CV_Enzo_Riviere.pdf")
    with open(cv_path, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="CV_Enzo_Riviere.pdf",
            mime="application/pdf"
        )
    
    
with col2:
    st.markdown("<h2 style='color: #90b5d5;'> My projects :</h2>", unsafe_allow_html=True)
    
    st.write("Throughout my studies, I have actively participated in a variety of projects, where I leveraged my technical skills to develop innovative solutions. ")
    
    st.markdown('''
                Some of my key projects include:
                - **R.E.M.I (Dart)** :iphone: : I developed an application designed to assist visually impaired individuals by reading and recognizing expiration dates on products, and then reading them out loud.
                This project not only improved my skills in mobile application development but also taught me how technology can be used to solve accessibility challenges.
                
                - **Not my Tempo (Vue JS/Express)** :globe_with_meridians: : This is an online platform where musicians can share, browse and download music sheets. 
                I worked on both the front-end (using Vue.js) and back-end (Express.js), enhancing my full-stack development capabilities.
                The project aimed to create a collaborative space for musicians to easily access and share their music.
                
                - **Explain (Mastercamp, Python)** :bar_chart: : I participated in a month-long data science project as part of a Mastercamp, where my team and I were tasked with building a patent classification model based on their content. 
                This project involved gathering and analyzing large datasets, feature engineering, and implementing a machine learning model using Python.
                This project deepened my understanding of machine learning and its applications in the real world.
                ''')
        
    url_github = "https://github.com/Enzo-Riviere"
    st.markdown("[You can find my projects on GitHub !](%s)"%url_github)

with col3:
    st.markdown("<h2 style='color: #90b5d5;'>My hobbies :</h2>", unsafe_allow_html=True)
        
    st.markdown('''
                Outside of academics and professional experiences, I have several hobbies that have shaped who I am:
                - **Music** :musical_note: : I am a passionate musician, having graduated from the Conservatoire de Saint-Maur in 2021, where I specialized in saxophone. 
                I’ve played saxophone for over a decade and participated in numerous performances and student concerts. 
                In addition to the saxophone, I play guitar, ukulele, drums, piano, and bass, which allows me to explore different musical styles and genres. 
                I’ve been part of several bands, and performing in front of audiences has taught me creativity, discipline, and collaboration.
                
                - **Basketball** :basketball: : I played for VGA Basketball from 2015 to 2018, where I developed my teamwork skills and discipline. 
                I still enjoy playing basketball recreationally, as it helps me stay active and maintain a healthy balance between my professional and personal life.
                
                - **Other Interests** :cooking::video_game: : In addition to music and sports, I love to explore my culinary skills. 
                Cooking allows me to relax and experiment with flavors from different cuisines. 
                I am also an avid gamer, enjoying both console and PC gaming as a way to challenge my strategic thinking and reflexes.
                    ''')
