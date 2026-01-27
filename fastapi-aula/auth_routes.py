from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=['auth', 'autenticador'])

@auth_router.get("/")
async def auth():
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """
    return {"auth_status": "Você foi autenticado"} 