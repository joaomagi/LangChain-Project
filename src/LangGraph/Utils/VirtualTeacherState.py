from dataclasses import dataclass # Biblioteca para facilitar a criação de classes, gerando automaticamente métodos como __init__, __repr__,
import json # Biblioteca para converter dicionários para json

import os # Biblioteca para interação com o sistema operacional, usada nesse caso para carregar variáveis de ambiente
from dotenv import load_dotenv # Biblioteca para utilização do dotenv

from langchain_groq import ChatGroq # Biblioteca para utilização do grop


# Salva a chave API em uma variavel, carregando ela e verificar se está válida
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("A chave de API da Groq não foi encontrada. Verifique se o arquivo .env está configurado corretamente.")

# Criação do modelo Groq, com definição do modelo, temperatura que define o nível de criatividade e limite máximo de tentativas caso falhe as requisições
groq = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.5,
    max_retries=2,
)

# Define uma classe para armazenar o estado do professor virtual, contendo a pergunta em JSON
@dataclass
class VirtualTeacherState:
    json_question: str

    # Gera o prompt para a IA
    def generate_prompt(self):
        return [
            {"role": "system", "content": "You are a math-focused AI. Your goal is to answer math problems, in a simple way, with step-by-step resolutions, clear explanations, in Brazilian Portuguese."},
            {"role": "human", "content": self.json_question},
        ]

# Nó do professor virtual
def virtual_teacher_node(state: VirtualTeacherState):
    from LangGraph.Utils.MathState import MathState # Importa a Classe MathState
    prompt = state.generate_prompt()
    response_groq = groq.invoke(prompt)  
    response = response_groq.content
    return MathState(question=json.loads(state.json_question)["question"], response=response)
