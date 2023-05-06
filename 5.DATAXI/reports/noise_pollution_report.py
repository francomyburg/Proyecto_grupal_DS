# Gestion de rutas

# Importacion de librerías
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots


# Directorio de los datos crudos / raw data

noise_pollution_dir = 'data/noise_pollution.parquet'
vehicular_volume_dir = 'data/vehicular_volume.csv'

def kpi_prepros_data(noise_poll_dir, veh_vol_dir):
    # Lectura del archivo
    noise_poll = pd.read_parquet(f"{noise_poll_dir}")
    vehicle_density = pd.read_csv(f"{veh_vol_dir}")

    vehicle_density['year'] = pd.to_datetime(vehicle_density['date']).dt.year
    
    # Filtro de fecha del 2016 al 2019
    vehicle_density = vehicle_density[(vehicle_density['year'] <= 2019) & (vehicle_density['year'] >= 2016)]
    # Conversion de la métrica del volumen vehicular en días
    vehicle_density[['volume']] = (vehicle_density.loc[::,['volume']])*(4*24)

    # Union de los datasets a través del identificador de borough
    data_v0 = pd.merge(vehicle_density[['date','id_borough','volume']], noise_poll, left_on='id_borough',right_on='id_borough')

    return data_v0

data_v0 = kpi_prepros_data(noise_pollution_dir, vehicular_volume_dir)


def kpi_noise_pollution_reduction(data, electric_vehs, borough):
    df = data.groupby(['year','month','day','borough_name'])[['volume','engine_sounds','alert_signal_sounds','total_sounds']].mean()
    df['prop_engsound_traffic'] = df['engine_sounds'] / df['volume']
    df['reduction_pct'] = 1 - ((df['total_sounds'] - (electric_vehs * df['prop_engsound_traffic'])) / df['total_sounds'])
    df = df.reset_index()
    df = df[df['borough_name'] == borough]
    avg_daily_reduction_pct = df['reduction_pct'].mean() * 100
    return {
        "avg_daily_reduction_pct": avg_daily_reduction_pct,
        "electric_vehs": electric_vehs,
        "borough_name": borough
    }


def cal_prop_noise_traffic(df_preprosseced):
    # Eliminando la columna id_borough
    data_v1 = df_preprosseced.drop('id_borough', axis=1)
    # Convertir la columna de fecha a datetime
    data_v1['date'] = pd.to_datetime(data_v1['date'], format='%Y-%m-%d')

    # Suma de registros diarios totales
    data_v1 = data_v1.groupby(['borough_name','date']).sum()
    # Reseteamos el index
    data_v1 = data_v1.reset_index()

    # Calculo del ratio sonidos registrados de motores por volumen de tráfico diariamente
    data_v1['prop_soundeng_voltraf'] = data_v1['engine_sounds'] / data_v1['volume']
    # Cálculo del ratio sonidos registrados de señales de alerta por volumen de tráfico diariamente.
    data_v1['prop_alertsig_voltraf'] = data_v1['alert_signal_sounds'] / data_v1['volume']
    # Cálculo del ratio total de sonidos registrados por volumen de tráfico diariamente.
    data_v1['prop_totalsoun_voltraf'] = data_v1['total_sounds'] / data_v1['volume']
    
    return data_v1

data_v1 = cal_prop_noise_traffic(data_v0)

# Nombre de los Borough
unique_boroughs = data_v1['borough_name'].unique()

# GRAFICAS RATIO SONIDOS CON VOLUMEN

# Tendencia del índice en el tiempo
@st.cache_data
def plot_rat_sounds_voltrafic(df, list_cols, ratio_selected, borough='manhattan'):
    sound_types_dict = {
        'prop_soundeng_voltraf': 'señales de alerta',
        'prop_alertsig_voltraf': 'motores',
        'prop_totalsoun_voltraf': 'señales de alerta y motores',
    } 
    df = df[list_cols]
    df = df[df['borough_name'] == borough]
    fig = go.Figure()
    
    # Crear la figura
    fig = fig.add_trace(go.Scatter(x=df["date"], y=df[ratio_selected], mode='lines', name="Proporción sonidos por volumen vehicular",line=dict(shape='spline', smoothing=0.6, color='#FFF', width=2.4)))
    # Personalizar el aspecto de la gráfica
    fig.update_layout(
        title={
            "text": f"<b>Proporción de sonidos ({sound_types_dict.get(ratio_selected)}) por volumen de tráfico en {borough.title()}</b>",
            "x": 0,
            "y": 1,
            "font": dict(
                size=14, 
                color='white'
                ),
            },
        xaxis_title="Años",
        yaxis_title="Proporción (sonidos registrados / volumen vehicular)",
        plot_bgcolor='rgba(0,0,0,0)',
        height=500,
    )
    # Cambiar el nombre de la variable en la leyenda
    fig.update_traces(name=f"{ratio_selected}")
    # Cambiar los nombres de la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='h',
            yanchor='top',
            y=1.22,
            xanchor='right',
            x=1.,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            ))
    # Agregar línea punteada horizontal en el valor limite de proporcion igual 1
    fig.add_trace(go.Scatter(x=[df['date'].min(), df['date'].max()], y=[10, 10],
                            mode='lines', 
                            name='Very Noisy', 
                            line=dict(color='#FFA500',
                            width=3, dash='dash')))
    # Agregar línea punteada horizontal en el valor limite de proporcion igual 1
    fig.add_trace(go.Scatter(x=[df['date'].min(), df['date'].max()], y=[1, 1],
                            mode='lines', 
                            name='Moderately Noisy', 
                            line=dict(color='#FFFF00',
                            width=3, dash='dash')))
    # Agregar línea punteada horizontal en el valor limite de proporcion igual 1
    fig.add_trace(go.Scatter(x=[df['date'].min(), df['date'].max()], y=[0.1, 0.1],
                            mode='lines', 
                            name='Slightly Noisy', 
                            line=dict(color='#ADD8E6',
                            width=3, dash='dash')))
    
    # Agregar línea punteada horizontal en el valor limite de proporcion igual 1
    fig.add_trace(go.Scatter(x=[df['date'].min(), df['date'].max()], y=[0.01, 0.01],
                            mode='lines', 
                            name='Quiet', 
                            line=dict(color='#a2c11c',
                            width=3, dash='dash')))
    
    # Escala logarítmica en el eje Y
    fig.update_yaxes(type='log')

    # Formatear eje X
    fig.update_layout(xaxis=dict(tickformat='%Y', dtick='M12'))

    
    # Mostrar la gráfica
    return fig

@st.cache_data
def plot_count_sounds_vehvol(df, borough_option):
    
    data = df[data_v0['borough_name'] == borough_option]
    data = data.groupby(['year']).sum().reset_index()
    
    fig = make_subplots(rows=2, cols=1, shared_xaxes=False, vertical_spacing=0.4 )
    
    fig.add_trace(go.Scatter(x=data['year'], y=data['total_sounds'], mode='lines', name='Total Sounds', line=dict(color='#ff6f3c', width=3)), row=1, col=1)
    fig.add_trace(go.Scatter(x=data['year'], y=data['engine_sounds'], mode='lines', name='Engine Sounds', line=dict(color='#ffc93c', width=3)), row=1, col=1)
    fig.add_trace(go.Scatter(x=data['year'], y=data['alert_signal_sounds'], mode='lines', name='Alert Signal Sounds', line=dict(color='#ff9a3c', width=3)), row=1, col=1)

    # Formatear eje X
    fig.update_xaxes(title_text="Años", row=1, col=1)
    fig.update_yaxes(title_text="N° de registros de sonidos", row=1, col=1)
    fig.update_yaxes(type='log', row=1, col=1)

    fig.update_xaxes(
        dtick="M12",
        tickformat="%Y",
        range=[data['year'].min(),
        data['year'].max()],
        row=1, col=1
    )
    
    fig.update_xaxes(title_text="Años", row=2, col=1)
    fig.update_yaxes(title_text="Volumen vehicular", row=2, col=1)
    fig.update_yaxes(type='log', row=2, col=1)

    fig.update_xaxes(
        dtick="M12",
        tickformat="%Y",
        range=[data['year'].min(),
        data['year'].max()],
        row=2, col=1
    )

    fig.update_layout(
        annotations=[
            {'text': f"<b>Cantidad de registros de sonidos en {borough_option.title()}</b>", 'x': 0.5, 'y': 1.35, 'xref': 'paper', 'yref': 'paper', 'showarrow': False,
            'font': dict(size=15, color='white')},
            {'text': f"<b>Volumen de tráfico vehicular en {borough_option.title()}</b>", 'x': 0.5, 'y': 0.40, 'xref': 'paper', 'yref': 'paper', 'showarrow': False,
            'font': dict(size=15, color='white')}
        ]
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)"
    )
    # Cambiar los nombres de la leyenda
    fig.update_layout(
        legend=dict(
            title='<b>Leyenda:</b>',
            orientation='h',
            yanchor='top',
            y=1.25,
            xanchor='right',
            x=1.,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            ))
    
    
    # Mostrar la gráfica
    fig.add_trace(go.Scatter(x=data['year'], y=data['volume'], mode='lines', name="Volume", line=dict(color='#e7eaf6', width=3)), row=2, col=1)
    
    return fig
