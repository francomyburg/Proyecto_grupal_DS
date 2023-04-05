# <h1> Analisís de datos para observar viabilidad de vehículos Eléctricos en el Servicio de Transporte de Pasajeros con Automóviles en la ciudad de New York </h1> 
## **HENRY BOOTCAMP | Proyecto Final**
<hr>

## 1. Introducción

El presente proyecto colaborativo busca analizar la situación actual del sector de transporte público en automóviles de la ciudad de New York  para determinar la conveniencia de inversión en este sector con tecnologías más sostenibles como la implementación de flotas de vehículos eléctricos.<br>

Se analiza el movimiento de vehiculos desde el año 2009 hasta el 2023 en los 5 distritos en NY: Manhattan (New York County), Brooklyn (Kings County), Queens (Queens County), The Bronx (Bronx County) & Staten Island (Richmond County). Se observa los datos coorespondientes a los niveles de ruido presentes en la ciudad y la calidad del aire.<br>


El proyecto tiene cuatro etapas:

**Etapa 1: Recopilación de los datos**<br>
Se realizan procesos de recopilación y limpieza de la información del movimientos de los taxis en NYC, emisiones CO2, API´s de las condiciones climáticas de la ciudad, datos de transporte público y niveles de ruido. <br>

Se desarrolla un EDA de los datos.<br>

**Etapa 2: Creación de base de datos (DW)** <br>

Se crea un DataWarehouse con una carga inicial automatizada de manera incremental en un servicio cloud.<br>

**Etapa 3: Análisis Económicos KPIs** <br>

Se genera el perfil económico del sector de transporte de taxis en NYC <br>

**Etapa 2: Creación de base de datos (DW)** 

<hr>

## 2. Desarrollo

**2.1. ETL Limpieza de datos:**

**2.2. EDA** 

**2.3. Dashboard**

<hr>

## 3. Recursos implementados

Python Version: 3.9<br>
Packages:  Pandas, Matplotlib, Seaborn<br>
Yahoo Finance API<br>
Microsoft PowerBi <hr>

### 2.1. ETL Limpieza de datos

El proceso de ETL se realiza con la ingesta de datos desde el origen: <br>

**Lista compañías S&P 500:** *(data extraída de website)*[ Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).<br>
**Historial de precio de acciones compañías S&P 500:** *(data extraída )* [Yahoo Finance](https://finance.yahoo.com/) e [Investing.com](https://www.investing.com/) .<br>

- Se cargan los datos para su normalización (Tratamiento de nulos, valores duplicados, formateo de variables, entre otros..).<br>

- Se relaciona el conjunto de datos.<br>

- Se crean dos datasets para realizar el EDA: ( [**df.csv** ](https://github.com/jospinoponce/AnalisisDeMercadoSP500/blob/main/datasets/df.csv) tiene los datos de todas las empresas del S&P 500 agrupado por año y precio final ajustado de la acción. ) & ([**df_day.csv** ](https://github.com/jospinoponce/AnalisisDeMercadoSP500/blob/main/datasets/df_day.csv): almacena también los datos de las compañías pero las agrupa por día.)<br>

*Los procesos realizados para el ETL están en el notebook:* [**1.ETL**](https://github.com/jospinoponce/AnalisisDeMercadoSP500/blob/main/Notebooks/1.ETL_report.ipynb)<hr>

### 2.2. Análisis Exploratorio de datos EDA



*Los procesos realizados para el EDA están en el notebook:* [**2.EDA**](https://github.com/jospinoponce/AnalisisDeMercadoSP500/blob/main/Notebooks/2.EDA_report.ipynb)<hr>

**2.3. Dashboard**



*Los procesos realizados para el desarrollo del dashboard están en:* [**3.dashboard.pbix**](https://github.com/jospinoponce/AnalisisDeMercadoSP500/blob/main/Dashboard/3.dashboard.pbixb)
<hr>

*Developed by*

<a href="https://www.linkedin.com/in/julio-cesar-postigo-1a5707219/"><img alt="Franco" title="Connect with Franco" src="https://img.shields.io/badge/Franco Myburg-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ANALYST**

<a href="https://www.linkedin.com/in/isaac-junior-pe%C3%B1a-cueva-320562264/"><img alt="Ivanna" title="Connect with Ivanna" src="https://img.shields.io/badge/Ivanna Villa-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/jospinoponce/"><img alt="Jaime" title="Connect with Jaime" src="https://img.shields.io/badge/Jaime Ospino-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/takticflow/"><img alt="Luciano" title="Connect with Luciano" src="https://img.shields.io/badge/Luciano Larrea-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **PROJECT MANAGER & DATA SCIENTIST**

<a href="https://www.linkedin.com/in/nicolas-angel-lazarte/"><img alt="Roy" title="Connect with Roy" src="https://img.shields.io/badge/Roy Quillca-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA SCIENTIST**



