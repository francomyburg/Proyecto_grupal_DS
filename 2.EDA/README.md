# <h1> Análisis Exploratorio de datos (EDA)</h1> 

## 1. Movimientos de taxis en New York

Se realiza un web scrapring para disponibilizar la data histórica de los viajes realizados por taxis en NYC [1.disponibilizar.ipynb](1.disponibilizar_taxis.ipynb).<br> 


Se analizan dos datasets.<br> 

- **Viajes de Taxis diarios Dic 2022** <br>
[EDA_taxis_viajes_diarios_Dic_22](2.EDA_taxis_viajes_diarios2.ipynbb)<br>

- **Viajes mensuales de Taxis New York en 2010-2022** <br>
[EDA_taxis_viajes_mes](3.EDA_taxis_viajes_mes.ipynb)<br>


Se analiza el mes de diciembre 2022.

Se calcula el valor promedio (USD) que tiene cada viaje realizado en taxis amarillos para cada borough.

<img src="source/costo_borough.png" width="800" height="300"/>

Se analiza la demanda de viajes y la facturación para cada dia de la semana.

<img src="source/viajes_semana.png" width="800" height="200"/>

<img src="source/factura_semna.png" width="800" height="200"/>

Se valida la correlación entre las variables.

<img src="source/m_corr_taxi1.png" width="400" height="400"/>


Las correlaciones más altas  corresponden a:<br>
   - Costo total del viaje (total_amount) vs. peajes (tolls_amount).
   - Recargo de congestion (congestion_surcharge) vs. Impuesto MTA.
   - Tasa por aeropuerto (airport_fee) vs. peajes (tolls_amount).
   - Costo total del viaje (total_amount) vs. Tasa por aeropuerto (airport_fee).

## 2. Componentes Medioambientales

### 2.1 **Contaminacón al aire**   [EDA_Air_Quality.ipynb](EDA_Air_Quality.ipynb)

Se analizan las mediciones de los distintos contaminantes presentes en los Boroughs de la ciudad de New York desde el año 2008 hasta el 2020.<br>

Se establece el promedio anual de las cargas contaminantes **Material Particulado de 2.5 micras, Dióxido de Nitrógeno, Ozono** & **Dióxido de Azufre.** <br>

<img src= "source/air_quality1.png" width="800" height="370"/>

Se utilizan los datos de PM 2.5 para establecer el **índice de calidad de aire**. Clasificación generada por IQAIR basado en los NAAQS (National Ambient Air Quality Standards) de la EPA (Environmental Protection Agency) de EE. UU. <br>

La EPA establece un índice de aire bueno cuando el PM 2.5 es inferior a 12 µg/cm3. <br>

<img src= "source/air_quality2.png" width="800" height="370"/>

### 2.2  **Densidad Vehicular**  [EDA_Air_Quality.ipynb](EDA_Air_Quality.ipynb)

Se calcula el **volumen vehicular** presente en cada Borough. Esta variable representa la cantidad de vehículos que pasan por determinado punto en un lapso de 15 minutos .<br>

<img src= "source/vehicular_density.png" width="650" height="250"/>

Se obtiene una correlación del 35% entre el **volumen vehicular** con la generación de material particulado **PM2.5.**

<img src= "source/correlation_air_density.png" width="200" height="200"/>

### 2.3  **Contaminación Acustica**  [EDA]()

Se analiza los datos de [data]. Este dataset registra las mediciones de presencia de sonidos que generan contaminación por ruido en los tres Boroughs más ruidosos de NYC en el año 2016 hasta el 2019. Los ruidos generados por los vehículos corresponden a los sonidos generados por el motor y los sonidos provenientes del sistema de alarma de los carros (sonidos de parqueo, claxon, alarma anti-robo etc). <br>

<img src= "source/generacion_ruido_nyc.png" width="650" height="200"/>

Se identifica el borough más ruidoso. (mayor cantidad de sonidos registrados)<br>

<img src= "source/generacion_ruido_total.png" width="650" height="200"/>



<hr>

*Developed by*

<a href="https://www.linkedin.com/in/franco-jonas-myburg-6095b8255/"><img alt="Franco" title="Connect with Franco" src="https://img.shields.io/badge/Franco Myburg-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/ivannagvdc/"><img alt="Ivanna" title="Connect with Ivanna" src="https://img.shields.io/badge/Ivanna Villa-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ANALYST**

<a href="https://www.linkedin.com/in/jospinoponce/"><img alt="Jaime" title="Connect with Jaime" src="https://img.shields.io/badge/Jaime Ospino-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/takticflow/"><img alt="Luciano" title="Connect with Luciano" src="https://img.shields.io/badge/Luciano Larrea-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **PROJECT MANAGER & DATA SCIENTIST**

<a href="https://www.linkedin.com/in/royquillca/"><img alt="Roy" title="Connect with Roy" src="https://img.shields.io/badge/Roy Quillca-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**




