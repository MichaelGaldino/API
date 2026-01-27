from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=['order'])

@order_router.get("/lista")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema
    """
    return {"mensagem": "Você acessou a rota de pedidos"}