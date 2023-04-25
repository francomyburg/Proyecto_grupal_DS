import streamlit as st
import pandas as pd

import utils.paths as path
from reports.air_pollution_report import kpi_brooklyn, kpi_manhattan, kpi_queen, kpi_staten_island, kpi_the_bronx, taxis

# from connection.get_data import get_data_azure_db
# df = get_data_azure_db("SELECT * FROM [air_pollution]")

def calcular_kpis(carros):
    kpi_b = kpi_brooklyn(carros)
    kpi_m = kpi_manhattan(carros)
    kpi_q = kpi_queen(carros)
    kpi_s = kpi_staten_island(carros)
    kpi_bx= kpi_the_bronx(carros)
    kpi_taxis = taxis(carros)
    return {
      "electric_carrs": carros, 
      "kpi_b": kpi_b,
      "kpi_m": kpi_m,
      "kpi_q": kpi_q,
      "kpi_s": kpi_s,
      "kpi_bx": kpi_bx,
      "kpi_taxis": kpi_taxis
    }

# URL de la imagen en GitHub
img_div_style = """
<style>
.air-poll-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: row;
  margin-bottom: 30px;
  background-color: #d8c51d;
  border-radius: 15px;
}

.left-container {
  flex: 1;
}

.right-container {
  display: flex;
  flex-direction:column;
  justify-content: center;
  align-items: center;
}
.right-container p {
  color: #f0f0f0;
  font-weight: bold;
}

img {
  width: 300px;
  height: 300px;
  
}
.right-container img {
  border-radius: 50%;
}

table {
  margin: auto;
  width: 80%;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  text-align: center;
  width: 30px;
}

.table-container .table-title {
  color: #fff;
  background-color: #085f63;
  font-weight: bold;
}

.table-container td, .table-container th {
  border: 2px solid #085f63;
  color: #085f63;
  font-weight: bold;
}

.air-poll-container .left-container  th {
  border: 2px solid #085f63;
}

</style>
"""
st.markdown(img_div_style, unsafe_allow_html=True)
url = 'https://github.com/francomyburg/Proyecto_grupal_DS/blob/main/3.REPORTS/source/Pm2.png?raw=true'
table_html = f"""
<h3 align="center"><b>KPI: Valor Porcentual de disminución de la contaminación al aire de PM 2,5 por número de Vehículos Eléctricos </b></h3>
<div class ="air-poll-container">
  <div class="left-container">
    <table align="center" class="table-container">
        <tr align="center">
          <th class="table-title">borough</th>
          <th class="table-title">Pm 2,5</th>
      </tr>
        <tr align="center">
          <td>bronx</td>
        <td>9.7</td>
      </tr>
        <tr align="center">
          <td>brooklyn</td>
        <td>9.3</td>
      </tr>
        <tr align="center">
          <td>manhattan</td>
        <td>10.9</td>
      </tr>
        <tr align="center">
          <td>queens</td>
        <td>8.9</td>
      </tr>
        <tr align="center">
          <td>staten island</td>
        <td>8.5</td>
      </tr>
    </table>
  </div>
  <div align="center" class="right-container">
    <img src="{url}" width="300px" height="300px" />
    <p>El sector de transporte genera el 17% de la contaminacón.</p>
  </div>
</div>
"""

st.markdown(table_html, unsafe_allow_html=True)

# Genera la cadena de texto con la etiqueta de imagen HTML

st.markdown("""
       Se genera un indicador clave de rendimiento que estipula el Porcentaje de disminución de la contaminacón al aire por el uso 
       de carros electricos.<br>
            """
  , unsafe_allow_html=True)

electric_cars = st.sidebar.number_input('**Number of electric cars**',1,10000000,value=1000)
kpi_vals = calcular_kpis(electric_cars)

st.markdown(
        """
        <style>
        .air-poll-kpi-container {
        # background-color: #FEFFA2;
        border: 2.5px solid #fafafa;
        border-radius: 8px;
        padding: 10px;
        margin: 10px;
        font-size: 16px;
        # color: #ff552e;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown(f"""
            <div class='air-poll-kpi-container'>
            <p>{kpi_vals['electric_carrs']} carros eléctricos generan un % de avance hacia la meta establecida por la OMS de:</p>
            <ol>
            <li>Brooklyn: {kpi_vals['kpi_b']}%</li>
            <li>Manhattan: {kpi_vals["kpi_m"]}%  </li>
            <li>Quenns: {kpi_vals['kpi_q']}% </li>
            <li>Staten: Islands {kpi_vals['kpi_s']}% </li>
            <li>Bronx: {kpi_vals['kpi_bx']}%" </li>
            </ol>
            <p>
              <b>{int(kpi_vals['electric_carrs'])} taxis eléctricos</b> disminuyen un <b>{kpi_vals["kpi_taxis"]}%</b> de la contaminacón al aire por PM 2.5 generada por el sector de taxis en NYC
            </p>
            <div>
            """, unsafe_allow_html=True)