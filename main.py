from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import Optional
app=FastAPI()  #http://127.0.0.1:8000

class Libro(BaseModel):
    titulo:str
    autor:str
    paginas:int
    editorial:str

@app.get("/")
def root():
    return {"message":"Hello World"}


@app.get("/mostrar_libro/{id}")
def mostrar_libro(id:int):
    return {"data":id}


@app.post("/insertar_libro/{libro}")
def insertar_libro(libro,titulo:Libro):
    return {"message":f"libro {libro,titulo} insertado"}