from fastapi import APIRouter
roteador_pedidos = APIRouter(prefix="/orders", tags=["pedidos"])

@roteador_pedidos.get("/")
async def pedidos():
    """
    Essa é a rota de pedidos
    """
    return {"mensagem": "Você acessou a rota de pedidos"}

@roteador_pedidos.get("/lista")
async def ListaPedidos():
    """
    Essa é a rota de lista de pedidos
    """
    return {"lista_msg": "Está é a lista de pedidos"}