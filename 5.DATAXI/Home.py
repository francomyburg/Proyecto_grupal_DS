import pandas as pd
import streamlit as st
from PIL import Image
import plotly.graph_objs as go
import plotly.express as px

# import utils.paths as path 
st.set_page_config(page_title="Dashboard", page_icon=":car:", layout="wide")


df = pd.read_csv("data/TLC_Monthy_Report_NYC.csv")

options = ['Home','Goals','Market']
query = st.sidebar.radio('Sección',options)

if query == options[0]:
    st.markdown("""
                <style>
    .wrapper {
    display: flex;
    justify-content: space-between;
    }

    .profile {
        display: flex;
        flex-direction: column;
        flex-basis: 18%;
        background-color: #f1f1f1;
        border: 2px solid #f1f1f1;
        text-align: center;
        font-size: 20px;
        padding: 10px;
        border-radius: 10px;
    }

    .profile a img {
        border-radius: 50%;
        width: 160px;
    }
    
    .profile-description {
    font-size: 1.2em;
    /* color: #FFF; */
    margin-bottom: 5px;
    text-align: center;
    }
    a {    
    display: block;
    padding: 10px;
    border-radius: 5px;
    text-decoration: none;
    color: #FFF;
    }

    a:hover {
    text-decoration: none;
    background-color: #00405d;
    color: #FFFFFF;
    border-radius: 5px;
    font-weight: 600;
    height: 100%;
    }
    a:hover a {
    background-color: #00405d;
    color: #FFFFFF;
    font-weight: 600;
    padding: 5px;
    height: 100%;
    }
    </style>  
                """, unsafe_allow_html=True)


    image = Image.open('pages/DGRL.png')
    st.image(image, use_column_width=True)

    
    st.markdown("""
                <h4 align="center">Team</h4>
                <div class="wrapper">
                
                <div class="profile">
                <a href="https://www.linkedin.com/in/franco-jonas-myburg-6095b8255/"> <img src="https://media.licdn.com/dms/image/D4D35AQGu2hOptaUNgg/profile-framedphoto-shrink_800_800/0/1683032373983?e=1684000800&v=beta&t=vSKbbBAGR2a7Nc1km58FA9SQXPc05H-268V0hVVetkw" alt="Franco" title="Connect with Franco"><br>DATA ENGINEER </a>
                </div>

                <div class="profile">
                <a href="https://www.linkedin.com/in/ivannagvdc/"><img alt="Ivanna" title="Connect with Ivanna" src="https://media.licdn.com/dms/image/C4E03AQHWmp3AQlPYSA/profile-displayphoto-shrink_200_200/0/1631153346220?e=1687996800&v=beta&t=1vKnwoPWjJgdPQ5JlEs3nBRxqYCo84X2wawG3Lj42fc"><br>DATA ANALYST</a>
                </div>

                <div class="profile">
                <a href="https://www.linkedin.com/in/jospinoponce/"><img alt="Jaime" title="Connect with Jaime" src="https://media.licdn.com/dms/image/D4E03AQFeOdXV4jJstA/profile-displayphoto-shrink_800_800/0/1682836288349?e=1688601600&v=beta&t=QCV7qJWXvFIkqHTEHuz7CHhVY-lSvfElf-eHIBzU-eE"><br>DATA ENGINEER</a>
                </div>

                <div class="profile">
                <a href="https://www.linkedin.com/in/takticflow/"><img alt="Luciano" title="Connect with Luciano" src="https://media.licdn.com/dms/image/D4D03AQFWWFxX4oYttw/profile-displayphoto-shrink_200_200/0/1674740829816?e=1687996800&v=beta&t=J1iCwMtATTUJmi-uo0g7aqijSuvQtjrBhcj8JAk1vY8"><br>PROJECT MANAGER & DATA SCIENTIST</a>
                </div>

                <div class="profile">
                <a href="https://www.linkedin.com/in/royquillca/"><img alt="Roy" title="Connect with Roy" src="https://media.licdn.com/dms/image/D4E35AQHQg3nYCccKSA/profile-framedphoto-shrink_800_800/0/1682912414782?e=1683644400&v=beta&t=V2tI9NsN_ExYqXSHIfqvht2mnOdOPyN8DcP1iHP4FxM" class="profile-description"><br>DATA ENGINEER</a>

                </div>
                </div>
                """, unsafe_allow_html=True)


if query == options[1]:
    st.markdown("""
                <style>
                .objectives {
                        display: flex;
                        flex-direction: row;
                        background-color: #f1f1f1;
                        border: 2px solid #f1f1f1;
                        text-align: center;
                        font-size: 20px;
                        padding: 5px;
                        border-radius: 10px;
                        height: 120px;
                        margin-bottom: 20px;
                        color:#002b36;
                        justify-content: space-between;
                        align-items: center;
                        align-content:center;
                    }
                .objectives h4 {
                    padding-left:30px;
                    width: 60%;
                    text-align: center;
                    # margin: auto;
                    color:#002b36;
                }
                .objectives p {
                    # margin: auto;
                    width: 30%;
                    text-align: center;
                    font-size : 20px;
                    font-weight: 600;
                }
                </style>
                """, unsafe_allow_html=True)
    
    st.markdown("""
                <h2 align="center"> Goals </h2>
                <h3 align="center">This work aims to answer the following questions:</h3>
                <div class="objectives">
                    <h4 align="center">¿What are the dimensions of the market?</h4>
                    <p>Market Share</p>
                </div>
                <div class="objectives">
                    <h4 align="center">¿What are the market prospects?</h4>
                    <p>Trends</p>
                </div>
                <div class="objectives">
                    <h4 align="center">¿What are the areas with the highest demand?</h4>
                    <p>Metrics</p>
                </div>
                <div class="objectives">
                    <h4 align="center">¿What are the projected revenues?</h4>
                    <p>KPIs</p>
                </div>
                <div class="objectives">
                    <h4 align="center">¿What is the projected positive environmental impact?</h4>
                    <p>Calculator</p>
                </div>
                """, unsafe_allow_html=True)

if query == options[2]:
    st.subheader('Market')
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('New York City')
        image = Image.open('pages/NYC.png')
        st.image(image, caption='Boroughs')
    with col2:
        st.write('Boroughs')
        image = Image.open('pages/NYCTable.png')
        st.image(image, caption='Data')
    
    
    
    
    

