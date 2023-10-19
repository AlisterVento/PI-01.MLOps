# **PI-01.MLOps**
<p align="center">
  <img src="https://github.com/AlisterVento/PI-01.MLOps/assets/129628866/671a9101-a8c4-49de-9419-6fe9ff1fdc05"/>
</p>

## **Machine Learning Operations (MLOps)**

<p align="center">
  <img src="https://github.com/AlisterVento/PI-01.MLOps/assets/129628866/728b3afa-25a2-442a-82a9-93b3d62d23e7"/>
</p>

## **Sobre el proyecto**

![image](https://github.com/AlisterVento/PI-01.MLOps/assets/129628866/9c65a280-dc60-486b-bbd2-f27a2c9e7532)

Steam es una plataforma de distribución digital de videojuegos desarrollada por Valve Corporation.
Esta plataforma actualmente tiene casi 20 años en el mercado ,y su principal objetivo es permitir unificar y distribuir videojuegos ,tanto de forma gratuita como de pago
,adicionalmente cuenta con servidores de emparejamiento, transmisiones de vídeo y servicios de redes sociales.

Steam el cual es la empresa donde empezaste a trabajar en el area de proyectos de Data ,Solicito la labor al area de **Data Science** al cual usted pertence,
como  tarea elaborar un MVP de su primer  proyecto de Data Science  en el mundo laboral el cual pondra a prueba sus habilidades ,Steam requiere que elabores
un sistema de recomendacion de videojuegos para usuarios.
Todo el proceso se encuentra compilado en [Notebook](Proyecto-MLOps.ipynb)

## Contenido

- [Introduccion](#Introduccion)
- [Contexto analítico](#Contexto-analítico)
- [Descripción del Problema](#Descripción-del-Problema)
- [Proceso de ETL](#Proceso-de-ETL)
- [Exploratory Data Analysis(EDA)](#Exploratory-Data-Analysis(EDA))
- [Modelo de Aprendizaje Automático](#modelo-de-aprendizaje-automático)
- [Implementación de la API](#implementación-de-la-api)
- [Uso de la API](#Uso-de-la-API)


## **Introduccion**
![image](https://github.com/AlisterVento/PI-01.MLOps/assets/129628866/35a1d882-8a1f-4e05-9a48-e809d40ae928)

Siguiendo el esquema como referencia se solicito elaborar un sistema de recomendacion de videojuegos para usuarios,realizar las transformaciones correspondientes , feature engineering ,
desarrolloar un API y unas funciones que se consumiran en el API y se realizara el deploy correspondiente .

## Contexto analítico 
Como parte del proyecto de Data Science se brindo los siguientes datos :
En esta ocasion se uso un dataset sobre la informacion de juegos de Steam en la comunidad australiana.
los 3 set de datos se encuentran almancenados en la carpeta [Data](/Data/) que se nos muestra acontinuacion :
- •steam_games.json
- •user_review.json
- •user_items.json
- Este notebook resume los resultados del desarrollo de mi primer proyecto enfocado en **Data Engineering y MLOps**.

## **Descripción del Problema**
Steam necesitaba un sistema de recomendación de videojuegos para sus usuarios. Los datos iniciales eran desafiantes, con datos crudos y poco limpios. Como MLOps Engineer, tuve que realizar tareas de Data Engineering y crear un MVP para abordar este problema, ademas de otras funciones.

## Proceso de ETL
En esta parte del parte se preprocesara la data que se obtuvo para poder transformarla y posteriormente cargarla para realizar el EDA respectivo
### Extraccion
- La carga de datos se realizo a travez del repositorio brindado [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)
- Tras una rapida observacion de los datasets en el formato JSON.
- Se procedio a convertirlos en DataFrames para su posterior transformacion asi como tambien se desanido algunas columnas .
### Transformacion
- Se transforma cada dataframe por separado .
- Se elimina las columnas 
- Se procesa los datos realizando transformacion de datos, limpieza y aplicando imputacion de datos para los faltantos
- Se dropea las filas que poseen muchos datos faltaste los cuales no se pueden imputar
### Carga
- Tras realizar la transformacion correspondiente se procede a exportar en formato parquet comprimido en gzip
  los resultados se encuentran en [Data Clean](/Data_Clean/)
-El proceso realizado se encuentra en los sigueintes notebooks:
- [Notebook Steam Games](steam_games-Analisis.ipynb)
- [Notebook User Items](user_items-Analisis.ipynb)
- [Notebook User Reviews](user_reviews-Analisis.ipynb)
### Exploratory Data Analysis(EDA)

## Modelo de Aprendizaje Automático

## Implementación de la API

## Uso de la API





