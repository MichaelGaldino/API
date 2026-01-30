from fastapi import APIRouter
roteador_autenticacao = APIRouter(prefix="/auth", tags=["autenticacao"])

@roteador_autenticacao.get("/")
async def autenticar():
    """
    Essa é a rota de autenticação
    """
    return {"mensagem": "Você acessou a rota de autenticação", "autenticar": False}