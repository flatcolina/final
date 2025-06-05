from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.econdo_bot import criar_liberacao_econdo
from app.firebase_util import atualizar_link_hospede

app = FastAPI()

class HospedeInput(BaseModel):
    nome: str
    data_checkin: str
    data_checkout: str
    document_id: str  # ID do hóspede no Firebase

@app.post("/gerar-link")
async def gerar_link(hospede: HospedeInput):
    try:
        link = criar_liberacao_econdo(
            nome=hospede.nome,
            data_checkin=hospede.data_checkin,
            data_checkout=hospede.data_checkout
        )
        if not link:
            raise HTTPException(status_code=500, detail="Não foi possível capturar o link de liberação.")
        sucesso = atualizar_link_hospede(hospede.document_id, link)
        if not sucesso:
            raise HTTPException(status_code=500, detail="Cadastro no Firebase não foi atualizado.")
        return {"success": True, "link": link}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no robô: {str(e)}")
