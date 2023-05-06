import streamlit as st
from reports.noise_pollution_report import plot_rat_sounds_voltrafic, data_v0, kpi_noise_pollution_reduction, data_v1, unique_boroughs, plot_count_sounds_vehvol
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard", page_icon=":car:", layout="wide")

sp_1, bor_col, sp_2, prop_type_col, sp_3  = st.columns((.1, 1, 0.1, 1,.1))
sp_left, body_col ,sp_right = st.columns((.1, 9.8, .1))

with prop_type_col:
    dict_props ={
        'Engine sounds / Volume': 'prop_soundeng_voltraf',
        'Alert Sounds / Volume': 'prop_alertsig_voltraf',
        'Total Sounds / Volume': 'prop_totalsoun_voltraf',
    }
    ratio_option = st.selectbox('**Proportion**', tuple(list(dict_props.keys())))

with bor_col:
    borough_option = st.selectbox('**Borough**',(unique_boroughs))
    
    # Seleccionar las columnas relevantes del dataframe
    rat_cols = ['prop_soundeng_voltraf', 'prop_alertsig_voltraf','prop_totalsoun_voltraf', 'borough_name', 'date']
    electric_cars = st.sidebar.number_input('**Number of electric cars**',1,10000000,value=1000)


with body_col:
    dict_data = kpi_noise_pollution_reduction(data_v0, electric_cars, borough_option)
    st.markdown(
        """
        <style>
        .container {
        border: 2.5px solid #fafafa;
        border-radius: 8px;
        padding: 10px;
        margin: 10px;
        font-size: 16px;
        margin-bottom: 40px; 
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(f"""
                <div class='container'>
                <p 
                    style='text-align:center';
                    font-size:20px;
                >
                    Implementando <b>{dict_data['electric_vehs']} vehículos eléctricos</b> que recorran diariamente en el <b>Borough {str(dict_data['borough_name']).title()}</b> se puede reducir un <b>{round(dict_data['avg_daily_reduction_pct']),4}%</b> de registros de sonidos de motores respecto del total de sonidos registrados relacionados a vehículos.</p>
                </div>    
                """, unsafe_allow_html=True)


plot_1, sp_center ,plot_2 = st.columns((4.5, 0.1, 4.5))

with plot_1:
    fig_count = plot_count_sounds_vehvol(data_v0, borough_option)
    st.plotly_chart(fig_count, config=dict(displayModeBar=False), use_container_width=True, use_container_height=False)

    
with plot_2:
    fig_prop = plot_rat_sounds_voltrafic(data_v1, rat_cols, dict_props.get(ratio_option), borough_option)
    st.plotly_chart(fig_prop, config=dict(displayModeBar=False), use_container_width=True)


