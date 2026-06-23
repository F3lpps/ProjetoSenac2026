from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from ViajeiAPI.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message)
def read_root():
    return {"message": "(͠≖ ͜ʖ͠≖)👌"}


@app.get('/teste', response_class=HTMLResponse)
def Ola_mundo():
    return """
<html>
      <head>
        <title> Fala, mundo </title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
