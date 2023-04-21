# <h1> Análisis de datos para observar viabilidad de vehículos Eléctricos en el Servicio de Transporte de taxis en la ciudad de New York </h1> 
## **HENRY BOOTCAMP | Proyecto Final**
<hr>

# 1. Introducción

Se lleva a cabo un análisis del sector de transporte público en los taxis amarillos de la ciudad de Nueva York con el fin de evaluar la viabilidad de invertir en tecnologías sostenibles, como la implementación de flotas de vehículos eléctricos.<br>

Se analizan datos en NYC de: los sonidos registrados por el trafico, la contaminación en el aire, el movimiento de vehículos por zona y los viajes que realizan los taxis en la ciudad para  los 5 Boroughs (distritos) de New York: **Manhattan (New York County), Brooklyn (Kings County), Queens (Queens County), The Bronx (Bronx County) & Staten Island (Richmond County)**.<br>

 Se implementa un modelo ML para estimar tendencias a futuro de los principales indicadores. Se realiza un Dashboard para la visualización de los datos con el mes de mayor actividad en el sector (Diciembre 2022).
 <br>

El proyecto se ejecuta bajo metodología ágil Scrum y se desarrolla en cuatro etapas.<br>

**Etapa 1: Recopilación de los datos**<br>
Procesos de recopilación y limpieza de la información. Se desarrolla un EDA.  <br>

**Etapa 2: Creación de base de datos** <br>
Creación de una base de datos SQL con una carga inicial automatizada de manera incremental en el servicio cloud de Microsoft Azure.<br>

**Etapa 3: Análisis Económico del sector & KPIs** <br>
Análisis del sector económico y generación de insights <br>

**Etapa 4: Modelo ML** <br>
Desarollo de modelo de Machine Learning de clasificación de clientes, resultados. <br>

La gestión del proyecto se desarrolla en:<br>
*Actividades [Task:](https://trello.com/b/BBq6OTiJ/proyecto-final) Cronograma [Gant:](https://docs.google.com/spreadsheets/d/10gupD91IRV9KfblHfoy6fAw1rV6vu_gw6LNHp0itnfo/edit#gid=1709744959)*

<hr>

# 2. Objetivos

- Identificar patrones y tendencias en los movimientos de taxis en NYC (2010-2022).<br>
  *Mayor promedio de distancias según origen/destino, Cantidad de viajes según origen/destino, Montos de viajes según origen/destino, Días y horarios con mayor demanda.* <br>

- Explorar y analizar la calidad del aire, la contaminación sonora en NYC relacionando el movimiento de los taxis.<br>

- Evaluar la relación entre el movimiento de los taxis y la calidad del aire o la contaminación sonora y determinar si hay correlación significativa. <br>

- Realizar un análisis de las ganancias económicas del sector. <br>
  *Ingreso bruto promedio hora/día/mes, Proporcion de ingresos por tarifa cliente/empresa.*<br>

- Desarrollar un Modelo de ML de clasificación de usuarios de taxis en la ciudad de Nueva York  para  plantear  estrategias de marketing por microsegmentación.<br>
  *Modelo de estimación de tarifa según borough y horario.* <br>

- Identificar oportunidades para la implementación de vehículos eléctricos en el sector de transporte de pasajeros.

<hr>

# 3. Desarrollo

<img src="src/esquema.png" width="900" height="300"/>


## 3.1 KPIs 

- 1. Distancia por vehículo (ganancia por kilometro)

      Mayores promedios de distancias según origen/destino.<br> 
      Cantidad de viajes según origen/destino  
      Montos de viajes según origen/destino.<br> 
      Dias y horarios con mayor demanda.<br> 

- 2. % disminución de contaminantes en el aire por vehículos eléctricos (% Variación promedio de PM 2,5)

- 3. % disminución de contaminación por ruido por vehículos eléctricos (% Variación promedio de sonidos registrados)

- 4. Ingresos brutos/netos cliente/empresa por dia/mes

      Tarifa/distancia (correlación)

- 5. Cuota del mercado proyectado
<br>

## 3.2 Recursos implementados

- Gestión de proyectos: Google meet, Trello.<br>

- Ingenieria de datos (EDA, ETL, SQL BD): Python, Beautiful Soup, Pandas, Matplotlib,  Seaborn , SQLAlchemy , Azure SQL.<br> 

- Análisis de datos (Business Intelligence & Machine Learning): Python, Pandas, SQLAlchemy , Plotly, PowerBI, Scikit-learn, Streamlit.<br> 

- Escalabilidad On Cloud: Azure (Azure Data Factory, Azure Blob Storage, Azure Synapse Analytics) <br>

## 3.3 Obtencción de los Datos

Los datos se extraen de fuentes oficiales que proporciona la ciudad de New York.  **Taxi & Limousine Commission**  https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page y de los datos abiertos de New York, **Open_Data_NYC** https://data.cityofnewyork.us/.<br> 

*El **Diccionario de los datos** puede consultarse en [data_dict](https://github.com/francomyburg/Proyecto_grupal_DS).*


<hr>

# 4. ETL

Se extraen los datos. Se emplean procesos de transformación. Se generan 5 tablas y se cargan a una base de datos SQL en Azure[nombre](https://github.com/francomyburg/Proyecto_grupal_DS/tree/main/1.ETL/DATABASE).  <br>

| **table** | **name** | **descripción** |
|:---:|:---:|---|
| _table_0_ | _TLC_Monthy_Report_NYC.csv_ | _relaciona datos de los viajes mensuales de taxi en NYC_ |
| _table_1_ | _yellow_2022_12.parquet_ | _relaciona datos de los viajes diarios de taxi en NYC_ |
| _table_2_ | _air_pollution.csv_ | _relaciona datos de las cargas contaminantes en el aire en NYC_ |
| _table_3_ | _vehicular_volume.csv_ | _relaciona datos de los flujos de vehículos en NYC_ |
| _table_4_ | _noise_pollution.csv_ | _relaciona datos de registros de sonidos molestos por vehículos en NYC_ |

*Los aspectos más importantes de este proceso se pueden consultar en: [ETL](https://github.com/francomyburg/Proyecto_grupal_DS/tree/main/1.ETL).*<br>



<hr>

# 5. EDA
<hr>

# 6. Resultados
<hr>

# 7. Conclusiones

<hr>

*Developed by*

<a href="https://www.linkedin.com/in/franco-jonas-myburg-6095b8255/"><img alt="Franco" title="Connect with Franco" src="https://img.shields.io/badge/Franco Myburg-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/ivannagvdc/"><img alt="Ivanna" title="Connect with Ivanna" src="https://img.shields.io/badge/Ivanna Villa-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ANALYST**

<a href="https://www.linkedin.com/in/jospinoponce/"><img alt="Jaime" title="Connect with Jaime" src="https://img.shields.io/badge/Jaime Ospino-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/takticflow/"><img alt="Luciano" title="Connect with Luciano" src="https://img.shields.io/badge/Luciano Larrea-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **PROJECT MANAGER & DATA SCIENTIST**

<a href="https://www.linkedin.com/in/royquillca/"><img alt="Roy" title="Connect with Roy" src="https://img.shields.io/badge/Roy Quillca-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**




