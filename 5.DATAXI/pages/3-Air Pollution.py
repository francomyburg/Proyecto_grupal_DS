import streamlit as st
import pandas as pd

from reports.air_pollution_report import kpi_brooklyn, kpi_manhattan, kpi_queen, kpi_staten_island, kpi_the_bronx, taxis




st.set_page_config(page_title="Dashboard", page_icon=":car:", layout="wide")


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
  margin:0;
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
  padding-right: 10px;
}

img {
  width: 330px;
  height: 300px;
  
}
.right-container img {
  # border-radius: 50%;
  # color: 
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
  color: #FFFF;
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
url = "assets/Pm2.png"
table_html = f"""
<h3 align="center"><b>KPI: Valor Porcentual de disminución de la contaminación al aire de PM 2,5 por número de Vehículos Eléctricos </b></h3>
<div class ="air-poll-container">
  <div class="left-container">
  <h6 align="center"><b>La contaminación al aire por PM 2.5 Promedio al año en los distintos distritos de New York es: </b></h6>
    <table align="center" class="table-container">
        <tr align="center">
          <th class="table-title">borough</th>
          <th class="table-title">Pm 2,5</th>
      </tr>
        <tr align="center">
          <td>Bronx</td>
        <td>9.7</td>
      </tr>
        <tr align="center">
          <td>Brooklyn</td>
        <td>9.3</td>
      </tr>
        <tr align="center">
          <td>Manhattan</td>
        <td>10.9</td>
      </tr>
        <tr align="center">
          <td>Queens</td>
        <td>8.9</td>
      </tr>
        <tr align="center">
          <td>Staten Island</td>
        <td>8.5</td>
      </tr>
    </table>
  </div>
  <div align="center" class="right-container">
    <img src="https://github.com/francomyburg/Proyecto_grupal_DS/blob/main/5.DATAXI/pages/Pm2.png?raw=true" width="300px" height="300px" />
    <p style="color:#085f63; ">El sector de transporte genera el 17% de la contaminacón.</p>
  </div>
</div>
"""

st.markdown(table_html, unsafe_allow_html=True)

st.markdown("""
       <p align="center" style="font-size: 18px;">
        Se genera un indicador clave de rendimiento que estipula el Porcentaje de disminución de la contaminacón al aire por el uso de carros electricos.
       </p>
            """
  , unsafe_allow_html=True)

electric_cars = st.sidebar.number_input('**Number of electric cars**',1,10000000,value=1000)
kpi_vals = calcular_kpis(electric_cars)

st.markdown(
        """
        <style>
        .air-poll-kpi-container {
        display: flex;          
        justify-content: space-around;
        align-items: center;
        flex-direction: row;
        border: 2.5px solid #fafafa;
        border-radius: 8px;
        padding: 10px;
        margin: 10px;
        font-size: 16px;
        }

      .kpi-left-container {
        width: 50%;
        paddin-left: 20px;
      }

      .kpi-right-container {
        display: flex;
        flex-direction:column;
        justify-content: center;
        align-items: center;
        width: 50%;
        padding-right: 30px;
        color: #FAFAFA;
      }
      .kpi-right-container p {
        font-weight: bold;
        text-align: justify;
      }

      .kpi-table-container .kpi-table-title {
        color: #FAFAFA;
        background-color: #085f63;
        font-weight: bold;
      }

      .kpi-table-container td, .kpi-table-container th {
        border: 2px solid #FAFAFA;
        color: #FAFAFA;
        font-weight: normal;
      }
        </style>
        """,
        unsafe_allow_html=True
    )

kpi_table_html = f"""
<div class ="air-poll-kpi-container">
  <div class="kpi-left-container">
  <h5 align="center">{kpi_vals['electric_carrs']} carros eléctricos disminuyen la contaminación al aire por PM 2,5 generada por el sector de los automoviles en: </h5>
    <table align="center" class="kpi-table-container">
        <tr align="center">
          <th class="kpi-table-title">Borough</th>
          <th class="kpi-table-title">Reduction (%)</th>
      </tr>
        <tr align="center">
          <td>Bronx</td>
        <td>{kpi_vals['kpi_bx']}% </td>
      </tr>
        <tr align="center">
          <td>Brooklyn</td>
        <td>{kpi_vals['kpi_b']}%</td>
      </tr>
        <tr align="center">
          <td>Manhattan</td>
        <td>{kpi_vals["kpi_m"]}%</td>
      </tr>
        <tr align="center">
          <td>Queens</td>
        <td>{kpi_vals["kpi_q"]}%</td>
      </tr>
        <tr align="center">
          <td>Staten Island</td>
        <td>{kpi_vals['kpi_s']}%</td>
      </tr>
    </table>
  </div>
  <div align="center" class="kpi-right-container">
    <p><b>{int(kpi_vals['electric_carrs'])} taxis eléctricos</b> disminuyen un <b>{kpi_vals["kpi_taxis"]}%</b> de la contaminacón al aire por PM 2.5 generada por el sector de taxis en NYC
  </div>
</div>
"""
st.markdown(kpi_table_html, unsafe_allow_html=True)
