from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
from typing import Optional
app=FastAPI()  #http://127.0.0.1:8000

df_user_reviews = pd.read_parquet(r'Data_Clean/clean_user_reviews.parquet.gzip')
df_steam_games = pd.read_parquet(r'Data_Clean/clean_steam_games.parquet.gzip')
df_user_items = pd.read_parquet(r'Data_Clean/clean__user_items.parquet.gzip')

@app.get("/userdata/User_id")
def userdata(User_id: str):

  """
  La función recibirá un id de usuario y aplicándolo devolverá la cantidad de
  dinero gastado junto al porcentaje de recomendaciones: siguiendo los siguientes
  pasos:

  - Primero con el user_id buscamos en la tabla df_user_items los juegos del
  usuario los cuales serán guardados en la variable "games"
    games = df_user_items[df_user_items['user_id'] == User_id]['item_id']
    games = games.tolist()
    spend_money = 0.0

  - Segundo se convertimos a una lista para poder calcular la cantidad de dinero
   gastado basado en la columna price de los juegos
    for game in games:
      price_games = df_steam_games.loc[df_steam_games['id'] == game, 'price']
      if not price_games.empty:
        price = price_games.values[0]
        spend_money += float(price)

  serán extraídos de la df_steam_games el cual sumara a nuestra variable llamada
   "spend_money".

  - Tercero contamos la cantidad de juegos totales de nuestro usuario.
    cant_games = df_user_items[df_user_items['user_id'] == User_id].shape[0]

  - Cuarto sumamos las recomendaciones totales de nuestro usuario.
    recomendations = df_user_reviews['recommend'][df_user_reviews['user_id']==user].sum()

  - Quinto calculamos el porcentaje
  ratio = recomendations/cant_games
  """

  #Paso 1
  games = df_user_items[df_user_items['user_id'] == User_id]['item_id']
  games = games.tolist()
  spend_money = 0.0

  #Paso 2
  for game in games:
      price_games = df_steam_games.loc[df_steam_games['id'] == game, 'price']
      if not price_games.empty:
        price = price_games.values[0]
        spend_money += float(price)

  #Paso 3
  cant_games = df_user_items[df_user_items['user_id'] == User_id].shape[0]

  #Paso 4
  recomendations = df_user_reviews['recommend'][df_user_reviews['user_id']==User_id].sum()

  #Paso 5
  ratio = recomendations/cant_games
  return f'{spend_money}:{round(ratio*100,2)}'

@app.get("/countreviews/{id}/{fecha_inicio},{fecha_fin}")
def countreviews(fecha_inicio:str, fecha_fin:str):

  """

  La función recibirá 2 datos tipo fecha de los cuales 1el primer de ellos significa
  el fecha de inicio y el segundo el de fin el retorno es la cantidad de usuarios
  que realizaron reviews entre las fechas dadas y, el porcentaje de recomendación
  de los mismos en base a la columna reviews.recommend.

  En esta función se seguirán los siguientes pasos:

  - Primero obtenemos los usuarios entre las fechas dadas, se usará una máscara
  en la tabla df_user_reviews y se extraerá los registros únicos es decir los id
  de los jugadores

  users = df_user_reviewss[(df_user_reviews['Posted Date'] >= fecha_inicio) &
                      (df_user_reviews['Posted Date'] <= fecha_fin)]['user_id'].unique()

  - Segundo obtenemos las recomendaciones positivas en este caso se usará la columna
  recommend de la tabla df_user_reviews para nuestra función manejaremos la función
  sum porque nuestros valores oscilan entre 1 para positivos y 0 para negativos
  entonces sería un filtro menos a usar
    positive = df_user_reviews[(df_user_reviews['Posted Date'] >= fecha_inicio) &
                    (df_user_reviews['Posted Date'] <= fecha_fin)] ['recommend'].sum(

  - Tercero calcularemos el total de recomendaciones tanto negativas como positivas
  por tanto usaremos la función count en la columna recomend de la tabla
  df_user_reviews.

  total_recommend = df_user_reviews[(df_user_reviews['Posted Date'] >= fecha_inicio) &
                    (df_user_reviews['Posted Date'] <= fecha_fin)]['recommend'].count()

  -Finalmente procederemos a calcular el porcentaje de recomendaciones positivas
  sobre el total de recomendaciones
  if total_recommend == 0:
    percentage = 0
  else:
    percentage = positive/total_recommend

  """

  #Paso 0
  fecha_inicio=datetime.datetime.strptime(fecha_inicio,'%Y-%m-%d')
  fecha_fin=datetime.datetime.strptime(fecha_fin,'%Y-%m-%d')

  #Paso 1
  users = df_user_reviews[(df_user_reviews['Posted Date'] >= fecha_inicio) &
                      (df_user_reviews['Posted Date'] <= fecha_fin)]['user_id'].unique()

  #Paso 2
  positive = df_user_reviews[(df_user_reviews['Posted Date'] >= fecha_inicio) &
                    (df_user_reviews['Posted Date'] <= fecha_fin)] ['recommend'].sum()

  #Paso 3
  total_recommend = df_user_reviews[(df_user_reviews['Posted Date'] >= fecha_inicio) &
                    (df_user_reviews['Posted Date'] <= fecha_fin)]['recommend'].count()

  #Paso 4
  if total_recommend == 0:
    percentage = 0
  else:
    percentage = positive/total_recommend

  return f'{len(users)} : {round(percentage,2)*100}%'


@app.get('/genre/{genero}')
def genre(genero: str):

  """

  La función recibirá 1 datos tipo str de genero el returno de esta funcion es
  el puesto en el que se encuentra un género sobre el ranking de los mismos
  analizado bajo la columna PlayTimeForever.


  En esta función se seguirán los siguientes pasos:

  - Primero obtenemos una serie con todos los generos presentes en la tabla df_steam_games
  y lo guardamos en **unique_genres** e instanciamosla variable **genre_sum** lo
  creamos como diccionario

  unique_genres = df_steam_games['genres'].unique()
  genre_sum = {}

  - Segundo iteraremos  cada genero de unique_genres y obtenemos los juegos de este
  genero los cuales los guardaremos en una lista a continuación procederemos a buscar
  en la tabla df_user_items los juegos del usuario los cuales serán guardados en
  la variable "list_games" y obtenemos el playtime_forever y finalmente guardarlo
   en el diccionario genre_sum

  for genre in unique_genres:
    list_games = df_steam_games[df_steam_games['genres'] == genre]['id'].drop_duplicates().tolist()
    playtime_genre = df_user_items.loc[df_user_items['item_id'].isin(list_games)]['playtime_forever'].sum()
    genre_sum[genre] = playtime_genre

  - Tercero procederemos a guardar el ranking de generos en la variable sorted_genres_sum
  teniendo como referencia la cantidad de horas jugadas

  sorted_genres_sum = dict(sorted(genre_sum.items(), key=lambda item: item[1], reverse=True))
  ranking = list(sorted_genres_sum.keys()).index(genero) + 1

  """

  #Paso 1
  unique_genres = df_steam_games['genres'].unique()
  genre_sum = {}

  #Paso 2
  for genre in unique_genres:
    list_games = df_steam_games[df_steam_games['genres'] == genre]['id'].drop_duplicates().tolist()
    playtime_genre = df_user_items.loc[df_user_items['item_id'].isin(list_games)]['playtime_forever'].sum()
    genre_sum[genre] = playtime_genre

  #Paso 3
  sorted_genres_sum = dict(sorted(genre_sum.items(), key=lambda item: item[1], reverse=True))
  ranking = list(sorted_genres_sum.keys()).index(genero) + 1

  return f'{genero} : {ranking}' # Retornamos
@app.get('/userforgenre/{genero}')
def userforgenre( género : str ):
  """
  La función recibirá 1 datos tipo str con el nombre de una compañia el retorno
  es la cantidad de items y porcentaje de contenido Free por año según empresa
  desarrolladora. Ejemplo de salida:
  """
  return 0
    
@app.get('/developer/{company_name}')
def developer(company_name: str):

  """
  La función recibirá 1 datos tipo str con el nombre de una compañia el retorno
  es la cantidad de items y porcentaje de contenido Free por año según empresa
  desarrolladora. Ejemplo de salida:

  -El paso 1 extraeremos los juegos que son gratis de la compañia dada y los guardaremos
  en una variable llamada 'free_games' .posteriormente la agruparemos por año

  free_games = df_steam_games[(df_steam_games['publisher'] == company_name) & (df_steam_games['price'] == 0) ].drop_duplicates(subset=['id'])
  free_games = free_games.groupby('year')['app_name'].nunique()

  -El paso 2 extraeremos el total de juegos de esa compañia y los guardaremos en
  una variable llamada 'all_games' .posteriormente la agruparemos por año

  all_games = df_steam_games[df_steam_games.publisher == company_name].groupby('year')['app_name'].nunique()

  -El paso 3 Crearemos la variable ratio_matrix que contendrqa la relacion entre
  el total de juegos gratis y el total de juegos de esa compañia

  -El paso 4 Creamos la variable answer que contendra la tabla para esta ocasion
  nos facilitamos de html para su visualización


  """

  # Paso 1
  free_games = df_steam_games[(df_steam_games['publisher'] == company_name) & (df_steam_games['price'] == 0) ].drop_duplicates(subset=['id'])
  free_games = free_games.groupby('year')['app_name'].nunique()

  # Paso 2
  all_games = df_steam_games[df_steam_games.publisher == company_name].groupby('year')['app_name'].nunique()

  #Paso 3
  ratio_matrix = (free_games/all_games)

  # Paso 4
  answer = f'<p>| {company_name} | | |</p><p>|-----|---------------------|</p><p>| Año | Contenido Free |</p>'
  for year, percentage in ratio_matrix.items():
      answer += f"<p>| {year} | {percentage*100:.0f}% |</p>"
  return answer


@app.get('/sentiment_analysis/{year}')
def sentiment_analysis( año : int ):

  """

  La función recibirá 1 datos tipo int correspondiente al año  el retorno
  devuelve una lista con la cantidad de registros de reseñas de usuarios que se
  encuentren categorizados con un análisis de sentimiento.
  - Primero obtenemos los datos de nuestro año

  reviews_per_year = df_user_reviews[df_user_reviews['year'] == año]

  -Segundo intercambiamos los valores asignados anteriomente como resultado del
  analisis de sentimiento

  replace_values = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}

  -Tercero contamos la cantidad de calificacion de sentimiento de las opiniones

  sentiment_resume = reviews_per_year['sentiment_analysis'].map(replace_values).value_counts().to_dict()

  """
  reviews_per_year = df_user_reviews[df_user_reviews['year'] == año]
    # Coseguimos los datos de nuestro año
  replace_values = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
    # Mapeamos los sentimientos con su respectiva palabra
  sentiment_resume = reviews_per_year['sentiment_analysis'].map(replace_values).value_counts().to_dict()
    # Contamos esos sentimientos
  return f'{sentiment_resume}'
