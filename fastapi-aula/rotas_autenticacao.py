from fastapi import APIRouter
roteador_autenticacao = APIRouter(prefix="/auth", tags=["autenticacao"])

@roteador_autenticacao.get("/")
def funcao_qualquer():
    return {"mensagem": "Você acessou a rota de autenticação"}