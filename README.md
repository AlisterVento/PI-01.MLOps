<h1 align=center> PI-01.MLOps </h1>

# **Machine Learning Operations (MLOps)**

<p align="center">
  <img src="https://github.com/AlisterVento/PI-01.MLOps/assets/129628866/728b3afa-25a2-442a-82a9-93b3d62d23e7"/>
</p>

## **Sobre el proyecto**

![image](https://github.com/AlisterVento/PI-01.MLOps/assets/129628866/9c65a280-dc60-486b-bbd2-f27a2c9e7532)

Steam es una plataforma de distribución digital de videojuegos desarrollada por Valve Corporation.
Esta plataforma actualmente tiene casi 20 años en el mercado ,y su principal objetivo es permitir unificar y distribuir videojuegos ,tanto de forma gratuita como de pago
,adicionalmente cuenta con servidores de emparejamiento, transmisiones de vídeo y servicios de redes sociales.

Steam ,la empresa donde empezaste a trabajar, en el area de proyectos de Data ,Solicito lal area de **Data Science** ,
la tarea de elaborar un sistema de recomendacion y el despliegue del servicio en una API como  MVP de su primer proyecto de Data Science  en el mundo laboral el cual pondra a prueba sus habilidades .


Todo el proceso se encuentra compilado en el siguiente [Notebook](/Proyecto%20MLOps.ipynb)

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
- Para el archivo de User_Reviews se realizo un analisis de sentimiento usando NLP con la libreria  VaderSentimient 
### Carga
- Tras realizar la transformacion correspondiente se procede a exportar en formato parquet comprimido en gzip
  los resultados se encuentran en [Data Clean](/Data_Clean/)
-El proceso realizado se encuentra en los sigueintes notebooks:
- [Notebook Steam Games](/steam_games%20Analisis.ipynb)
- [Notebook User Items](/user_items%20Analisis.ipynb)
- [Notebook User Reviews](/user_reviews%20Analisis.ipynb)
## Exploratory Data Analysis(EDA)
Tras la exportacion de la data clean se procedio a trabajar en el notebook central [Notebook](/Proyecto%20MLOps.ipynb) donde se procedio a hacer el respectivo analisis formulando preguntas correspondientes a los datos que se obtuvo y tambien presentandolos graficamente 
donde se pudo llegar a diversas conclusiones como:
- Basado en la data comprendida entre el 2000 y 2018 se observa un pico de creacion de videojuegos en el año 2015 rondando los 10000 juegos
- Mas del 90% de juegos no ofrecen una version **Early Access**
- Del total de juegos casi el 50% son producidas por compañias Indies
- Los desarrolladores en su mayoria colocan como precio a sus productos 5$ seguido de 10$
- El juego mas jugado en steam en toda su historia y en las ultimas dos semanas que presceden a la toma de datos es **Counter Strike**
- Las reseñas normalmente encontradas en la baul de comentarios de los juegos en su mayoria no son utiles
## Modelo de Aprendizaje Automático
Para la realizacion del modelo a usar en este caso fue para la elaboracion de un modelo de recomendacion se uso el modelo de coseno de similitud 
Puede ser más valioso encontrar todas aquellas juegos que son más parecidas a la que nos gusta.
Desarrollo:
-Carga de datos extrayendo nuestras columnas de interes ene ste caso los generos de cada juego y el nombre del juego
-Usando TfidfVectorizer una libreria que realiza la labor de tokenizar los documentos, aprender el vocabulario e invertir las ponderaciones de frecuencia de los documentos, y permitir codificar nuevos documentos.
-Se procede a elaborar el modelo de coseno de similud y creando una matriz entre todo los juegos 

## Implementación de la API
Para la implentacion de la API se uso como herramienta la libreria de FastAPI el cual facilito la implementacion para el deploy de la API se uso los siguietes archivos:
- [Main](/main.py),
- [Requirement](/requirements.txt)
- [Procfile](/Procfile.txt)
  
Se han creado las siguientes funciones para los endpoints de la API:
- userdata(User_id: str)
- countreviews(YYYY-MM-DD y YYYY-MM-DD: str)
- genre(género: str)
- userforgenre(género: str)
- developer(desarrollador: str)
- sentiment_analysis(año: int)

## Uso de la API
Update:Para el deploy del API se uso Railway el cual se encontraba funcional ,actualmente el servicio paso a deprecated sin embargo aun se puede hacer el deploy de manera local





