from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List, Dict, Any


from core_astro.engine import AstroEngine
from core_ai.generator import gerar_analise_ia, responder_pergunta_ia
from utils.converters import get_coords_from_city

# --- Modelos de Dados (Pydantic) ---
class BirthData(BaseModel):
    data_nasc: str  # Espera "AAAA-MM-DD"
    hora_nasc: str
    cidade_nasc: str
    fuso_horario: Any

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatData(BaseModel):
    mapa_astral: Dict[str, Any]
    pergunta: str
    historico: List[ChatMessage]

# --- Aplicação FastAPI ---
app = FastAPI()

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Endpoints da API ---
@app.post("/analisar")
def handle_analise(birth_data: BirthData):
    print(f"Recebido pedido para analisar: {birth_data}")
    coords = get_coords_from_city(birth_data.cidade_nasc)
    if not coords:
        return {"error": "Cidade não encontrada"}
    lat, lon = coords
    
    try:
        ano, mes, dia = map(int, birth_data.data_nasc.split('-'))

        
        motor = AstroEngine(
            ano, mes, dia,
            birth_data.hora_nasc, 
            lat, 
            lon, 
            birth_data.fuso_horario
        )
        mapa = motor.gerar_mapa_completo()
        analise = gerar_analise_ia(mapa)
        
        return {"analise": analise, "mapa": mapa}

    except Exception as e:
        print(f"ERRO NO BACKEND: {e}")
        return {"error": f"Ocorreu um erro interno no servidor: {e}"}


@app.post("/chat")
def handle_chat(chat_data: ChatData):
    print(f"Recebida pergunta no chat: {chat_data.pergunta}")
    try:
        historico_dict = [msg.dict() for msg in chat_data.historico]
        resposta = responder_pergunta_ia(
            chat_data.mapa_astral, 
            chat_data.pergunta,
            historico_dict
        )
        return {"resposta": resposta}
    except Exception as e:
        print(f"ERRO NO CHATBOT: {e}")
        return {"error": f"Ocorreu um erro na IA do chat: {e}"}