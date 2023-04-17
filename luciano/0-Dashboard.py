import pandas as pd
import streamlit as st
import datetime
import plotly.graph_objs as go
import plotly.express as px

df = pd.read_csv('Proyecto_grupal_DS/luciano/df.csv',index_col=13)
# Convertir el índice del dataframe en datetime
df.index = pd.to_datetime(df.index)
df = df[df['license_class']=='Yellow']

# Dashboard layout
# def dashboard_ui():
st.set_page_config(page_title="Dashboard", page_icon=":car:", layout="wide")
fleet = st.sidebar.number_input('Fleet Number',1,100000,value=1000)
monthdate = st.sidebar.date_input("Month Date", datetime.date(2023, 1, 1))
# Obtener la fecha seleccionada en el date_input
selected_date = pd.to_datetime(monthdate)
# Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
unique_vehicles_value = df.loc[selected_date, 'unique_vehicles']
market_share = fleet / (fleet + unique_vehicles_value)
market_share_percentage = market_share * 100
# Sidebar menu
# st.sidebar.title("Menu")
menu_items = ["Vehicles", "Trips", "Farebox", "Ratios"]
menu_selection = st.sidebar.radio("Select a page", menu_items)
colors = {'Yellow': 'Yellow', 'Green': 'Green', 'FHV - High Volume': 'FHVHV','FHV - Black Car':'Black','FHV - Lux Limo':'Lux Limo','FHV - Livery':'Livery'}
df['color'] = df['license_class'].map(colors)

# Dashboard page
if menu_selection == menu_items[0]:
    
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='unique_vehicles', color='color')
    fig.update_layout(
    title='Unique Vehicles',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Unique Vehicles'))
    st.plotly_chart(fig, use_container_width=True)
    
    # df = df[df['license_class']=='Yellow']
    # Mostrar el valor en la interfaz de Streamlit
    st.write(f"El valor de unique_vehicles para la fecha seleccionada ({selected_date}) es {unique_vehicles_value}")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Market Vehicles',unique_vehicles_value)
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        st.metric('Fleet Vehicles', fleet)
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='unique_drivers', color='color')
    fig.update_layout(
    title='Unique Drivers',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Unique Drivers'))
    st.plotly_chart(fig, use_container_width=True)
    
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='drivers_vehicles_ratio', color='color')
    fig.update_layout(
    title='Drivers / Vehicles Ratio',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Drivers / Vehicles Ratio'))
    st.plotly_chart(fig, use_container_width=True)

if menu_selection == menu_items[1]:
    # st.header("Dashboard")
    # st.sidebar.subheader("Choose a Date Range")

    # colors = {'Yellow': 'Yellow', 'Green': 'Green', 'FHV - High Volume': 'FHVHV','FHV - Black Car':'Black','FHV - Lux Limo':'Lux Limo','FHV - Livery':'Livery'}

    # # Create a new column with the corresponding color for each license class
    # df['color'] = df['license_class'].map(colors)
    # Create two line charts with different license classes
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='trips_per_day', color='color')
    # fig2 = px.line(df[df['license_class']=='Green'], x='month_date', y='trips_per_day',color='color')
    # fig3 = px.line(df[df['license_class']=='FHV - High Volume'], x='month_date', y='trips_per_day', color='color')
    # fig4 = px.line(df[df['license_class']=='FHV - Black Car'], x='month_date', y='trips_per_day', color='color')
    # fig5 = px.line(df[df['license_class']=='FHV - Livery'], x='month_date', y='trips_per_day',color='color')
    # fig6 = px.line(df[df['license_class']=='FHV - Lux Limo'], x='month_date', y='trips_per_day', color='color')
    # fig.add_traces(fig2.data + fig3.data + fig4.data + fig5.data + fig6.data)
    fig.update_layout(
    title='Trips per Day',
    xaxis=dict(title='Month & Year', showgrid=True),
    yaxis=dict(title='Trips Per Day'))

    st.plotly_chart(fig, use_container_width=True)  #
    col1, col2, col3 = st.columns(3)
    with col1:
        # Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
        trips_day_value = df.loc[selected_date, 'trips_per_day']
        st.metric('Market Trips per day USD',trips_day_value)
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        shared_trips = int(trips_day_value * market_share)
        st.metric('Fleet Trips per day USD',shared_trips)
    # st.plotly_chart(df['trips_per_day'], use_container_width=True)
    # st.plotly_chart(df['trips_year'], use_container_width=True)
    
    # st.write("### Trips per Month")
    # st.plotly_chart(df['trips_per_month'], use_container_width=True)
    # st.write("### Medallions per Month")
    # st.plotly_chart(df['medallions_per_month'], use_container_width=True)
    
    # st.sidebar.subheader("Monthly")
    # monthlydate = st.sidebar.date_input("Monthly Date", [datetime.date(2016, 1, 1), datetime.date.today()])
    # element_id1_m = st.sidebar.selectbox("Select Your Variable for x-axis", ("month_date", "week", "year"))
    # element_id2_m = st.sidebar.selectbox("Select Your Variable for y-axis", ("trips_per_day", "trips_per_day_shared", "farebox_per_day", "unique_drivers", "unique_vehicles", "avg_minutes_per_trip", "avg_days_vehicles_on_road", "avg_hours_per_day_per_vehicle", "avg_days_drivers_on_road", "avg_hours_per_day_per_driver", "percent_of_trips_paid_with_credit_card"))
    # element_id3_m = st.sidebar.selectbox("Select Your Grouping Variable", ("license_class",))
    
    # st.write("### Outputs")
    # st.write("#### id1_m")
    # st.write("#### id2_m")
    # st.write("#### id3_m")


   # st.plotly

if menu_selection == menu_items[2]:
    # colors = {'Yellow': 'Yellow', 'Green': 'Green', 'FHV - High Volume': 'FHVHV','FHV - Black Car':'Black','FHV - Lux Limo':'Lux Limo','FHV - Livery':'Livery'}
    # df['color'] = df['license_class'].map(colors)
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='farebox_per_day', color='color')
    # fig2 = px.line(df[df['license_class']=='Green'], x='month_date', y='farebox_per_day',color='color')
    # fig.add_traces(fig2.data)
    fig.update_layout(
    title='Average Farebox per Day',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Farebox Per Day'))
    st.plotly_chart(fig, use_container_width=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        # Obtener el valor de unique_vehicles correspondiente a la fecha seleccionada
        farebox_day_value = df.loc[selected_date, 'farebox_per_day']
        st.metric('Market Farebox per day USD',farebox_day_value)
    with col2:
        st.metric('Market Share', f'{market_share_percentage:.2f}%')
    with col3:
        shared_farebox = int(farebox_day_value * market_share)
        st.metric('Fleet Farebox per day USD',shared_farebox)

    
if menu_selection == menu_items[3]:
    

    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='monthly_farebox_per_vehicle_on_road', color='color')
    fig.update_layout(
    title='Monthly Farebox Per Vehicle On Road',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Monthly Farebox Per Vehicle On Road'))
    st.plotly_chart(fig, use_container_width=True)
    
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='monthly_farebox_per_trip_on_road', color='color')
    fig.update_layout(
    title='Monthly Farebox Per Trip On Road',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Monthly Farebox Per Trip On Road'))
    st.plotly_chart(fig, use_container_width=True)
    
    fig = px.line(df[df['license_class']=='Yellow'], x='month_date', y='monthly_trips_per_vehicle_on_road', color='color')
    fig.update_layout(
    title='Monthly Trips Per Vehicle On Road',
    xaxis=dict(title='Month & Year', showgrid=False),
    yaxis=dict(title='Monthly Trips Per Vehicle On Road'))
    st.plotly_chart(fig, use_container_width=True)
# start_date = st.sidebar.date_input('Start Date',datetime.date(2013, 1, 1))
# end_date = st.sidebar.date_input('End Date',datetime.date(2023, 1, 1)) 