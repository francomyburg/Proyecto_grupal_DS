import pandas as pd
import streamlit as st
import datetime as datetime
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('data/df.csv',index_col=13)
df.index = pd.to_datetime(df.index)
proy_Y = pd.read_csv('data/proy_Y.csv',index_col=0)
proy_Y.index = pd.to_datetime(proy_Y.index)
# Dashboard layout
st.set_page_config(page_title="Dashboard", page_icon=":car:", layout="wide")
fleet = st.sidebar.number_input('Fleet Number',1,100000,value=1000)

# Obtener la fecha seleccionada en el date_input
start_date = datetime.date(2015, 1, 1)  #st.date_input('Start Date',
end_date = datetime.date(2024, 11, 1)    # st.date_input('End Date',
current_date = datetime.date(2023, 1, 1)

selected_date = st.sidebar.slider("Select a date range:",
                    value=(current_date),
                    min_value=start_date,
                    max_value=end_date,
                    format="MMM YYYY",
                    # step = month,
                    key="date_range")
selected_date = selected_date.replace(day=1)
selected_date = pd.to_datetime(selected_date)
# Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
unique_vehicles_forecast = proy_Y.loc[selected_date, 'unique_vehicles']
market_share = fleet / (fleet + unique_vehicles_forecast)
market_share_percentage = market_share * 100

menu_items = ["Vehicles", "Trips", "Farebox", "Hours per Day", "Monthly Trips per Vehicle"]
menu_selection = st.sidebar.radio("Select a page", menu_items)
# Obtener la posición del índice `selected_date`
selected_date_pos = proy_Y.index.get_loc(selected_date)



# Dashboard page
if menu_selection == menu_items[0]:
    
    # st.write(f"El valor de unique_vehicles para la fecha proyectada ({selected_date}) es {unique_vehicles_forecast}")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Market Vehicles',int(unique_vehicles_forecast))
    with col2:
        st.metric('Taxi Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        st.metric('Fleet Vehicles', fleet)
    with col4:
        ev_market_share = 100* fleet / (fleet + unique_vehicles_forecast/100)
        st.metric('EV Taxi Market Share', f'{ev_market_share:.2f}%')

    # Crear una figura de Plotly
    fig = go.Figure()
    if  st.checkbox('Show FHVHV',value=False):
        fig.add_trace(go.Scatter(x=df[df['license_class']=='FHV - High Volume']['month_year1'], y=df[df['license_class']=='FHV - High Volume']['unique_vehicles'], mode='lines', name='FHV - High Volume'))
    # Agregar la línea del conjunto de datos `proy_Y`
    fig.add_trace(go.Scatter(x=proy_Y.index, y=proy_Y['unique_vehicles'], mode='lines', name='proy_Y'))
    fig.add_trace(go.Scatter(x=proy_Y.index, y=proy_Y['unique_vehicles_PC'], mode='lines', name='proy_Y_PC'))
    # Agregar la línea del conjunto de datos `df`
    fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['unique_vehicles'], mode='lines', name='Yellow'))
    # Agregar la línea vertical en la posición `selected_date_pos`
    fig.add_shape(type='line',
                x0=proy_Y.index[selected_date_pos],
                y0=0,
                x1=proy_Y.index[selected_date_pos],
                y1=max(df[df['license_class']=='Yellow']['unique_vehicles']),
                line=dict(color='red', width=2, dash='dash'))
    fig.add_shape(
                type='line',
                x0=proy_Y.index[0],
                y0=proy_Y.loc[proy_Y.index[selected_date_pos], 'unique_vehicles'],
                x1=proy_Y.index[-1],
                y1=proy_Y.loc[proy_Y.index[selected_date_pos], 'unique_vehicles'],
                line=dict(color='red', width=2, dash='dash'))
    x_value = proy_Y.index[selected_date_pos].strftime('%y-%m')
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=max(df[df['license_class']=='Yellow']['unique_vehicles']),
                   text="date: {}".format(x_value),
                   showarrow=True, arrowhead=1, ax=-50, ay=-50)
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=proy_Y.loc[proy_Y.index[selected_date_pos], 'unique_vehicles'],
                   text="value: {}".format(int(proy_Y.loc[proy_Y.index[selected_date_pos], 'unique_vehicles'])),
                   showarrow=True, arrowhead=1, ax=50, ay=50)

    
    # Configurar el diseño del gráfico
    fig.update_layout(title='Yellow Taxi: Average Vehicles per Day each Month',
                    xaxis=dict(title='Month & Year', showgrid=True),
                    yaxis=dict(title='Vehicles Per Day'))

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)


   # st.plotly

if menu_selection == menu_items[1]:
    col1, col2, col3 = st.columns(3)
    with col1:
        # Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
        trips_day_value = proy_Y.loc[selected_date, 'trips_per_day']
        st.metric('Market Trips per day',trips_day_value)
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        shared_trips = int(trips_day_value * market_share)
        st.metric('Fleet Trips per day',shared_trips)

        
    
    # Plotly combinado
    fig = go.Figure()
    if  st.checkbox('Show FHVHV',value=False):
        fig.add_trace(go.Scatter(x=df[df['license_class']=='FHV - High Volume']['month_year1'], y=df[df['license_class']=='FHV - High Volume']['trips_per_day'], mode='lines', name='FHV - High Volume'))
    fig.add_trace(go.Scatter(x=proy_Y.index, y=proy_Y['trips_per_day'], mode='lines', name='proy_Y'))
    fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['trips_per_day'], mode='lines', name='Yellow'))
    fig.add_shape(type='line',
                x0=proy_Y.index[selected_date_pos],
                y0=0,
                x1=proy_Y.index[selected_date_pos],
                y1=max(proy_Y['trips_per_day']),
                line=dict(color='red', width=2, dash='dash'))
    fig.add_shape(
                type='line',
                x0=proy_Y.index[0],
                y0=proy_Y.loc[proy_Y.index[selected_date_pos], 'trips_per_day'],
                x1=proy_Y.index[-1],
                y1=proy_Y.loc[proy_Y.index[selected_date_pos], 'trips_per_day'],
                line=dict(color='red', width=2, dash='dash'))
    
    x_value = proy_Y.index[selected_date_pos].strftime('%y-%m')
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=max(df[df['license_class']=='Yellow']['trips_per_day']),
                   text="date: {}".format(x_value),
                   showarrow=True, arrowhead=1, ax=-50, ay=-50)
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=proy_Y.loc[proy_Y.index[selected_date_pos], 'trips_per_day'],
                   text="value: {}".format(int(proy_Y.loc[proy_Y.index[selected_date_pos], 'trips_per_day'])),
                   showarrow=True, arrowhead=1, ax=50, ay=50)
    
    fig.update_layout(title='Yellow Taxi: Total Trips per Day each Month',
                    xaxis=dict(title='Month & Year', showgrid=True),
                    yaxis=dict(title='Trips Per Day'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.write('Monthly Taxi trip counts steadily decreased from 2013 to 2023, partially due to the expansion of High-Volume For-Hire Services (HVFHS)')
        
if menu_selection == menu_items[2]:
    col1, col2, col3 = st.columns(3)
    with col1:
        # Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
        farebox_day_value = proy_Y.loc[selected_date, 'farebox_per_day']
        st.metric('Market Farebox per day USD',farebox_day_value)
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        shared_farebox = int(farebox_day_value * market_share)
        st.metric('Fleet Farebox per day USD',shared_farebox)
    

    # Plotly combinado
    fig = go.Figure()
    st.write('FHVHV: no data')

    fig.add_trace(go.Scatter(x=proy_Y.index, y=proy_Y['farebox_per_day'], mode='lines', name='proy_Y'))
    fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['farebox_per_day'], mode='lines', name='Yellow'))
    fig.add_trace(go.Scatter(x=proy_Y.index, y=proy_Y['farebox_per_day_PC'], mode='lines', name='proy_Y_PC'))
    fig.add_shape(type='line',
                x0=proy_Y.index[selected_date_pos],
                y0=0,
                x1=proy_Y.index[selected_date_pos],
                y1=max(proy_Y['farebox_per_day']),
                line=dict(color='red', width=2, dash='dash'))
    fig.add_shape(
                type='line',
                x0=proy_Y.index[0],
                y0=proy_Y.loc[proy_Y.index[selected_date_pos], 'farebox_per_day'],
                x1=proy_Y.index[-1],
                y1=proy_Y.loc[proy_Y.index[selected_date_pos], 'farebox_per_day'],
                line=dict(color='red', width=2, dash='dash'))
    
    x_value = proy_Y.index[selected_date_pos].strftime('%y-%m')
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=max(df[df['license_class']=='Yellow']['farebox_per_day']),
                   text="date: {}".format(x_value),
                   showarrow=True, arrowhead=1, ax=-50, ay=-50)
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=proy_Y.loc[proy_Y.index[selected_date_pos], 'farebox_per_day'],
                   text="value: {}".format(int(proy_Y.loc[proy_Y.index[selected_date_pos], 'farebox_per_day'])),
                   showarrow=True, arrowhead=1, ax=50, ay=50)
    
    fig.update_layout(title='Yellow Taxi: Total Farebox per Day each Month',
                    xaxis=dict(title='Month & Year', showgrid=True),
                    yaxis=dict(title='Farebox Per Day'))
    st.plotly_chart(fig, use_container_width=True)
    
    
if menu_selection == menu_items[3]:
    
    col1, col2, col3 = st.columns(3)
    with col1:
        # Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
        hours_day_value = proy_Y.loc[selected_date, 'avg_hours_per_day_per_vehicle']
        st.metric('Hours per day per vehicle',round(hours_day_value,1))
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        hours_day_fleet = int(hours_day_value * fleet)
        st.metric('Fleet Total Hours per day',hours_day_fleet)
    
    
    # Plotly combinado
    fig = go.Figure()
    if  st.checkbox('Show FHVHV',value=False):
        fig.add_trace(go.Scatter(x=df[df['license_class']=='FHV - High Volume']['month_year1'], y=df[df['license_class']=='FHV - High Volume']['avg_hours_per_day_per_vehicle'], mode='lines', name='FHV - High Volume'))
    fig.add_trace(go.Scatter(x=proy_Y.index, y=proy_Y['avg_hours_per_day_per_vehicle'], mode='lines', name='proy_Y'))
    fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['avg_hours_per_day_per_vehicle'], mode='lines', name='Yellow'))
    fig.add_shape(type='line',
                x0=proy_Y.index[selected_date_pos],
                y0=0,
                x1=proy_Y.index[selected_date_pos],
                y1=max(proy_Y['avg_hours_per_day_per_vehicle']),
                line=dict(color='red', width=2, dash='dash'))
    fig.add_shape(
                type='line',
                x0=proy_Y.index[0],
                y0=proy_Y.loc[proy_Y.index[selected_date_pos], 'avg_hours_per_day_per_vehicle'],
                x1=proy_Y.index[-1],
                y1=proy_Y.loc[proy_Y.index[selected_date_pos], 'avg_hours_per_day_per_vehicle'],
                line=dict(color='red', width=2, dash='dash'))
    
    x_value = proy_Y.index[selected_date_pos].strftime('%y-%m')
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=max(df[df['license_class']=='Yellow']['avg_hours_per_day_per_vehicle']),
                   text="date: {}".format(x_value),
                   showarrow=True, arrowhead=1, ax=-50, ay=-50)
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=proy_Y.loc[proy_Y.index[selected_date_pos], 'avg_hours_per_day_per_vehicle'],
                   text="value: {}".format(round(proy_Y.loc[proy_Y.index[selected_date_pos], 'avg_hours_per_day_per_vehicle'],1)),
                   showarrow=True, arrowhead=1, ax=50, ay=50)
    
    fig.update_layout(title='Yellow Taxi: Average Hours per Day each Vehicle',
                    xaxis=dict(title='Month & Year', showgrid=True),
                    yaxis=dict(title='Hours Per Day'))
    st.plotly_chart(fig, use_container_width=True)

if menu_selection == menu_items[4]:
    
    col1, col2, col3 = st.columns(3)
    with col1:
        # Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
        trips_day_value = proy_Y.loc[selected_date, 'monthly_trips_per_vehicle_on_road']
        st.metric('Market Trips per vehicle',int(trips_day_value))
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        fleet_trips = int(trips_day_value * fleet)
        st.metric('Monthly Fleet Trips',fleet_trips)
    
    # Plotly combinado
    fig = go.Figure()
    if  st.checkbox('Show FHVHV',value=False):
        fig.add_trace(go.Scatter(x=df[df['license_class']=='FHV - High Volume']['month_year1'], y=df[df['license_class']=='FHV - High Volume']['monthly_trips_per_vehicle_on_road'], mode='lines', name='FHV - High Volume'))
    fig.add_trace(go.Scatter(x=proy_Y.index, y=proy_Y['monthly_trips_per_vehicle_on_road'], mode='lines', name='proy_Y'))
    fig.add_trace(go.Scatter(x=df[df['license_class']=='Yellow']['month_year1'], y=df[df['license_class']=='Yellow']['monthly_trips_per_vehicle_on_road'], mode='lines', name='Yellow'))
    fig.add_shape(type='line',
                x0=proy_Y.index[selected_date_pos],
                y0=0,
                x1=proy_Y.index[selected_date_pos],
                y1=max(proy_Y['monthly_trips_per_vehicle_on_road']),
                line=dict(color='red', width=2, dash='dash'))
    
    fig.add_shape(
                type='line',
                x0=proy_Y.index[0],
                y0=proy_Y.loc[proy_Y.index[selected_date_pos], 'monthly_trips_per_vehicle_on_road'],
                x1=proy_Y.index[-1],
                y1=proy_Y.loc[proy_Y.index[selected_date_pos], 'monthly_trips_per_vehicle_on_road'],
                line=dict(color='red', width=2, dash='dash'))

    x_value = proy_Y.index[selected_date_pos].strftime('%y-%m')
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=max(df[df['license_class']=='Yellow']['monthly_trips_per_vehicle_on_road']),
                text="date: {}".format(x_value),
                showarrow=True, arrowhead=1, ax=-50, ay=-50)
    fig.add_annotation(x=proy_Y.index[selected_date_pos], y=proy_Y.loc[proy_Y.index[selected_date_pos], 'monthly_trips_per_vehicle_on_road'],
                text="value: {}".format(int(proy_Y.loc[proy_Y.index[selected_date_pos], 'monthly_trips_per_vehicle_on_road'])),
                showarrow=True, arrowhead=1, ax=50, ay=50)
    fig.update_layout(title='Yellow Taxi: Total Trips per Vehicle each Month',
                    xaxis=dict(title='Month & Year', showgrid=True),
                    yaxis=dict(title='Trips per Vehicle'))
    st.plotly_chart(fig, use_container_width=True)
