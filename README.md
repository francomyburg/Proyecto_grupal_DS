# <h1> Análisis de mercado para evaluar la viabilidad de la incorporación de vehículos eléctricos en el servicio de taxis en la ciudad de Nueva York. </h1> 
## **HENRY BOOTCAMP | Proyecto Final**
<hr>

# 1. Introducción

Se lleva a cabo un análisis del sector de transporte público en los taxis amarillos de la ciudad de Nueva York con el fin de evaluar la viabilidad de invertir en tecnologías sostenibles como la implementación de flotas de vehículos eléctricos. Se analizan datos en NYC de los sonidos registrados por el tráfico, la contaminación en el aire, el movimiento de vehículos por zona y los viajes que realizan los taxis en la ciudad para  los 5 Boroughs (distritos) de New York: **Manhattan (New York County), Brooklyn (Kings County), Queens (Queens County), The Bronx (Bronx County) & Staten Island (Richmond County)**.Se implementa un modelo de Machine Learning  para estimar tendencias a futuro de los principales indicadores. Se realiza un Dashboard para la visualización de los datos y resultados obtenidos. <br>

El proyecto se ejecuta bajo metodología ágil Scrum y se desarrolla en cuatro etapas.<br>
**Etapa 1:** Recopilación de los datos, **Etapa 2:** Creación de base de datos, **Etapa 3:** Análisis Económico, KPIs y **Etapa 4:** Modelo ML. <br>

La gestión del proyecto se desarrolla en:<br>
*Actividades [Task:](https://trello.com/b/BBq6OTiJ/proyecto-final) Cronograma [Gant:](https://docs.google.com/spreadsheets/d/10gupD91IRV9KfblHfoy6fAw1rV6vu_gw6LNHp0itnfo/edit#gid=1709744959)*

<hr>

# 2. Objetivos

- Identificar patrones y tendencias en los movimientos de taxis en NYC (2010-2022).<br>
 
- Investigar la relación entre el movimiento de los taxis y la calidad del aire y la contaminación sonora en NYC, para determinar alguna  correlación existente. <br>

- Realizar un análisis de las ganancias económicas del sector. <br>

- Desarrollar un Modelo de ML para estimar comportamientos futuros del sector de transporte de taxi en NYC.<br>

<hr>

# 3. Desarrollo

<img src="src/esquema.png" width="800" height="300"/>

## 3.1 Recursos implementados

- Gestión del proyecto: Google meet, Trello.<br>
- EDA, ETL, SQL BD: Python, Beautiful Soup, Pandas, Matplotlib,  Seaborn, PySpark, SQLAlchemy , Azure SQL.<br> 
- Business Intelligence & Machine Learning: Python, Pandas, SQLAlchemy , Plotly, PowerBI, Scikit-learn, Streamlit.<br> 
- Cloud: Azure (Azure Data Factory, Azure Blob Storage, Azure Synapse Analytics) <br>

## 3.2 Obtencción de los Datos

Los datos se extraen de fuentes oficiales que proporciona  New York.  [**Taxi & Limousine Commission**](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) y de los datos abiertos de la ciudad [**Open_Data_NYC**](https://data.cityofnewyork.us/).<br> 

*El **Diccionario de los datos** puede consultarse en [data_dict](https://github.com/francomyburg/Proyecto_grupal_DS).*

<hr>

# 4. ETL/EDA

Se desarrolla un sistema que extrae datos de manera automática de [**Taxi & Limousine Commission**](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) los transforma y los carga por medio de un pipeline a una base de datos SQL en la nube de Azure..

 *Los aspectos más importantes de este proceso se pueden consultar en: [ETL](https://github.com/francomyburg/Proyecto_grupal_DS/tree/main/1.ETL) y el [EDA](https://github.com/francomyburg/Proyecto_grupal_DS/tree/main/2.EDA).*<br>

<hr>

# 5. Resultados

Se desarolla un modelo ML 
Se genera una app en Streamlit con un dashboard de PowerBi embebido. 

## 5.1 KPIs 

-  Porcentaje de la cantidad de viajes proyectada.<br>
-  Porcentaje de la cuota del mercado proyectado.<br>
-  Ingresos brutos por día/mes.<br>
-  Porcentaje de disminución de contaminante (PM 2,5) en el aire por implementar vehículos eléctricos.<br>
- Reducción porcentual de contaminación acústica por implementar vehículos eléctricos. <br>



<hr>

# 6. Conclusiones

<hr>

*Developed by*

<a href="https://www.linkedin.com/in/franco-jonas-myburg-6095b8255/"><img alt="Franco" title="Connect with Franco" src="https://img.shields.io/badge/Franco Myburg-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/ivannagvdc/"><img alt="Ivanna" title="Connect with Ivanna" src="https://img.shields.io/badge/Ivanna Villa-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ANALYST**

<a href="https://www.linkedin.com/in/jospinoponce/"><img alt="Jaime" title="Connect with Jaime" src="https://img.shields.io/badge/Jaime Ospino-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/takticflow/"><img alt="Luciano" title="Connect with Luciano" src="https://img.shields.io/badge/Luciano Larrea-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **PROJECT MANAGER & DATA SCIENTIST**

<a href="https://www.linkedin.com/in/royquillca/"><img alt="Roy" title="Connect with Roy" src="https://img.shields.io/badge/Roy Quillca-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**




