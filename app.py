from fastapi import FastAPI
import json
import pandas as pd

app = FastAPI(
    title="LangPlus Vocabulary API",
    description="API para fornecer recursos para um sistema de controle pedagógico e também geração de exercícios de aprendizado de Inglês",
    version="1.0.0"
)

with open("verbos.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

df = pd.DataFrame(dados)

@app.get("/")
def home():
    return {"mensagem": "Minha API está funcionando!"}

@app.get("/en/{word}")
def get_word(word: str):
    result = df[df['root_verb'] == word].to_dict(orient='records')
    if result:
        return result[0]
    else:
        return {"message" : "word not found"}


@app.get("/sobre")
def sobre():
    return {
        "framework": "FastAPI",
        "linguagem": "Python",
        "tipo": "API REST"
    }
