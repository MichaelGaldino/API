from fastapi import FastAPI
app = FastAPI()

from rotas_autenticacao import roteador_autenticacao
from rotas_pedidos import roteador_pedidos

app.add_api_route(roteador_autenticacao)
app.add_api_route(roteador_pedidos)