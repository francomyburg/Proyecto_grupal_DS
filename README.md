# <h1> Analisís de datos para observar viabilidad de vehículos Eléctricos en el Servicio de Transporte de Pasajeros con Automóviles en la ciudad de New York </h1> 
## **HENRY BOOTCAMP | Proyecto Final**
<hr>

## 1. Introducción

Se lleva a cabo un análisis del sector de transporte público en automóviles en la ciudad de Nueva York con el fin de evaluar la viabilidad de invertir en tecnologías más sostenibles, como la implementación de flotas de vehículos eléctricos.<br>

El proyecto se ejecuta bajo metodologia agil Scrum y se desarrolla en cuatro etapas. Se analizan los niveles de ruido presentes en la ciudad, la calidad del aire, el movimiento de vehiculos desde el año 2009 hasta el 2023 en los 5 distritos en NY: Manhattan (New York County), Brooklyn (Kings County), Queens (Queens County), The Bronx (Bronx County) & Staten Island (Richmond County) entre otros.

**Etapa 1: Recopilación de los datos**<br>
Se realizan procesos de recopilación y limpieza de la información. Se desarrolla un EDA.  <br>

**Etapa 2: Creación de base de datos (DW)** <br>

Se crea un DataWarehouse con una carga inicial automatizada de manera incremental en el servicio cloud AWS.<br>

**Etapa 3: Análisis Económico del sector & KPIs** <br>

Se analiza el perfil económico del sector de transporte de pasajeros en vehiculos en NYC para generar 5 KPI's: <br>

**Etapa 4: Modelo ML** 



La gestión del proyecto se desarrolla en:<br>
*Actividades [Task:](https://trello.com/b/BBq6OTiJ/proyecto-final) Cronograma [Gant:](https://docs.google.com/spreadsheets/d/10gupD91IRV9KfblHfoy6fAw1rV6vu_gw6LNHp0itnfo/edit#gid=1709744959)*

<hr>

## 2. Objetivos

- Identificar patrones y tendencias en los movimientos de taxis en la ciudad de Nueva York a lo largo del tiempo (establecer tiempo)

  -- Mayores promedios de distancias según origen/destino 

  -- Cantidad de viajes según origen/destino 

  -- Montos de viajes según origen/destino

  -- Días y horarios con mayor demanda <br>

- Explorar y analizar la calidad del aire y la contaminación sonora en la ciudad de Nueva York en relación con el movimiento de los taxis, utilizando técnicas de visualización de datos y análisis estadísticos.<br>

- Evaluar la relación entre el movimiento de los taxis y la calidad del aire y la contaminación sonora en la ciudad de Nueva York, para determinar si existe alguna correlación significativa. <br>

- Análisis de las ganancias económicas del sector. <br>
  -- Ingreso bruto promedio hora/día/mes <br>
  -- Proporcion de ingresos por tarifa cliente/empresa<br>

- Desarrollar un Modelo de ML de clasificación de usuarios de taxis en la ciudad de Nueva York  para  plantear  estrategias de marketing por microsegmentación.
  -- Modelo de estimación de tarifa según borough y horario <br>

- Identificar los desafíos y oportunidades relacionados con la implementación de vehículos eléctricos en la flota de la empresa de servicios de transporte de pasajeros, y evaluar los posibles beneficios ambientales y económicos.


<br><h2 align="center">KPIs asociados a los objetivos(planteo)</h2><br>

- 1-Distancia por vehiculo (ganancia por kilometro)

    Mayores promedios de distancias según origen/destino 

    Cantidad de viajes según origen/destino 

    Montos de viajes según origen/destino

    Dias y horarios con mayor demanda

- 2-Indice de calidad del aire

- 3-Decibeles por metro cuadrado

- 4-Ingresos brutos/netos cliente/empresa por dia/mes 

    Tarifa/distancia (correlacion)

- 5-Cuota del mercado proyectado
<hr>

## 3. Recursos implementados

- Gestión de proyectos: Google meet, Trello.<br>

- Ingenieria de datos (EDA, ETL, DATAWAREHOUSE): Python, Pandas, Matplotlib,  Seaborn , SQLAlchemy , PostgreSQL.<br> 

- Análisis de datos (Business Intelligence & Machine Learning): Python, Pandas, SQLAlchemy , Plotly, PowerBI.<br> 

- Para el aprendizaje automático se utilizó Scikit-learn y se hizo el deployment mediante Streamlit.<br>

- Escalabilidad On Cloud: Azure.<br>
La integración se realizara con Azure Data Factory, el almacenamiento con Azure Blob Storage, el Data Lake con Azure Data Lake, el RDB con Azure Synapse Analytics.<br>

<center><img src="franco/diagrama.png" width="500" height="400"/></center>
<hr>

## 4. Recopilación de los datos
El origen de los datos:

Se ingestan y se normalizan los datos.<br>

<hr>

*Developed by*

<a href="https://www.linkedin.com/in/julio-cesar-postigo-1a5707219/"><img alt="Franco" title="Connect with Franco" src="https://img.shields.io/badge/Franco Myburg-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ANALYST**

<a href="https://www.linkedin.com/in/ivannagvdc/"><img alt="Ivanna" title="Connect with Ivanna" src="https://img.shields.io/badge/Ivanna Villa-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/jospinoponce/"><img alt="Jaime" title="Connect with Jaime" src="https://img.shields.io/badge/Jaime Ospino-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/takticflow/"><img alt="Luciano" title="Connect with Luciano" src="https://img.shields.io/badge/Luciano Larrea-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **PROJECT MANAGER & DATA SCIENTIST**

<a href="https://www.linkedin.com/in/nicolas-angel-lazarte/"><img alt="Roy" title="Connect with Roy" src="https://img.shields.io/badge/Roy Quillca-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA SCIENTIST**



