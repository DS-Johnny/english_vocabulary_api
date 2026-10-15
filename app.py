from fastapi import FastAPI
import json
import os
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(
SUPABASE_URL,
SUPABASE_KEY
)



app = FastAPI(
    title="LangPlus Vocabulary API",
    description="API para fornecer recursos para um sistema de controle pedagógico e também geração de exercícios de aprendizado de Inglês",
    version="1.0.0"
)

with open("verbos.json", "r", encoding="utf-8") as f:
    dados = json.load(f)



@app.get("/")
def home():
    return {"mensagem": "Minha API está funcionando!"}

@app.get("/en/{word}")
def get_word(word: str):
    response = supabase.table('verbs').select("*").eq('root_verb', word).execute()
    print(response.data)
    dados_consulta  = response.data
    return dados_consulta


@app.get("/sobre")
def sobre():
    return {
        "framework": "FastAPI",
        "linguagem": "Python",
        "tipo": "API REST"
    }
