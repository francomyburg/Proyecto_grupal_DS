import pandas as pd
import streamlit as st
# import utils.paths as path
import base64
from io import BytesIO
# Ruta del directorio que contiene el archivo
# data_dir = path.make_dir_function(['app','data']) #'roy',
# Lectura del PDF como un objeto binario
with open("data/Informe_Final.pdf", "rb") as f:
    archivo_pdf = f.read()
# Transformando el pdf a 
def codificar_base64(archivo):
    with open(archivo, "rb") as f:
        datos = f.read()
        base64_pdf = base64.b64encode(datos).decode('utf-8')
    return base64_pdf

st.markdown("""
            <style>
            .btn-download-pdf {
                display: flex;
                flex-direction: column;
                align-content: center;
                text-align: center;
                width: 210px;
            }
            .btn-download-pdf a{
                text-decoration: none;
            }
            </style>
            """, unsafe_allow_html=True)
# Boton de descarga
descarga = st.button('Generate Analysis Report in Spanish', type='primary')
if descarga:
    b64 = codificar_base64('data/Informe_Final.pdf')
    href = f"""
    <p class="btn-download-pdf" align="center">
        <a href="data:application/octet-stream;base64,{b64}" download="Informe_Final.pdf">Download PDF</a>
    </p>"""
    st.markdown(href, unsafe_allow_html=True)

st.title('Summary')
st.header('The State of the Taxi Industry')
st.subheader('Taxi Trip Counts and Locations')
st.write('Monthly Taxi trip counts steadily decreased more than 80% since 2013 to 2023.')
st.write('Total trips per vehicle decreased more than 75% since 2013 to 2023.')
st.write('Trip locations for Taxis have remained fairly constant, centralized in Manhattan and at JFK and LaGuardia airport.')
st.subheader('Driver Statistics')
st.write('The number of “active” Taxi Vehicles decreased 43% since 2013 to 2023.')
st.write('The number of “active” Taxi Drivers decreased 68% since 2013 to 2023.')
st.write('The ratio of Drivers/Vehicles decreased from 2,5 in 2013 to 1,4 in 2023.')
st.subheader('Gross Income')
st.write('The average Farebox per Day decreased 65% since 2013 to 2023.')
st.write('The average Farebox per Vehicle decreased 50% since 2013 to 2023.')
st.header('Forecasting of the Taxi Industry')
st.write('The number of vehicles is projected to peak at 9,500 total taxis by April 2024 and then begin to decline again.')
st.write('By the end of 2025, 8,770 vehicles are projected, 1,000 more than january 2023.')
st.write('If the downward trend continues, it could reach a minimum by August 2024, this date being the most critical point for the taxi industry.')
st.header('Recommendations')
st.write('In December 2022, the average daily collection was USD 2,358,924 among 7,872 vehicles, averaging a daily income of USD 300 per vehicle.')
st.write('The Manhattan borough concentrates 90% of New York travel volume, therefore it is highly recommended to deploy the fleet in this borough.')
st.write('The recommended average work schedule is 8 hours per vehicle between 12:00 and 20:00, given that there is a greater volume of trips lasting between 10 and 15 minutes, which translates into higher revenue per journey. The average collection for Manhattan at that time for December 2022 was approximately USD 24,135,184 among a total of 2,360 vehicles averaging a revenue of USD 10,266 per month or USD 395 per day.')
st.write('The difference between investing without taking into account the recommendations and investing following the recommendations of this report is **32%**.')
st.write('A differential profit of **USD 95 per day per vehicle** represents an additional profit of **USD 2,470 per month per vehicle** or USD 2,470,000 per month for a fleet of 1,000 vehicles.')
st.header('Conclusions')
st.write('While investing in a bear market is extremely risky, it also represents an opportunity for those who wish to strongly position themselves in the market.')
st.write('Those who manage to survive the looming crisis in the yellow taxi industry and manage to position themselves as leaders in service, sustainability and innovation will be the ones who dominate the future of the market.')

