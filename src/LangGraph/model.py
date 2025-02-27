from dataclasses import dataclass # Biblioteca para facilitar a criação de classes, gerando automaticamente métodos como __init__, __repr__,
import re # Biblioteca para validar se uma string contem um caracter específico 
import json # Biblioteca para converter dicionários para json

import os # Biblioteca para interação com o sistema operacional, usada nesse caso para carregar variáveis de ambiente
from dotenv import load_dotenv # Biblioteca para utilização do dotenv

from langchain_groq import ChatGroq # Biblioteca para utilização do grop

from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages

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

# Define o estado da conversa com uma lista de mensagens
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Criação de uma variável que contenha algumas expressões matemáticas para validação
math_expressions = r"[0-9+\-×÷=]|\b(soma|subtração|multiplicação|divisão|igual|pi)\b"

# Define uma classe para armazenar o estado da pergunta e resposta matemáticas
@dataclass # O decorador @dataclass simplifica a criação de classes
class MathState:
    question: str
    response: str = ""

# Validar se a pergunta contém termos matématicos
def validate_question(question: str):
    if not re.search(math_expressions, question, re.IGNORECASE):
        raise ValueError("A pergunta não é sobre matemática")
    return question

# Nó de validação
def validate_node(state: MathState):
    validate_question(state.question)
    return JSONState(state.question)

# Define uma classe para representar o estado JSON da pergunta
@dataclass
class JSONState:
    text: str
    category: str = "math"

    # Converter a perunta para o formato JSON
    def to_json(self):
        return json.dumps({"question": self.text, "category": self.category})

# Nó de conversão para JSON
def to_json_node(state: JSONState):
    return VirtualTeacherState(json_question=state.to_json())

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
    prompt = state.generate_prompt()
    response_groq = groq.invoke(prompt)  
    response = response_groq.content
    return MathState(question=json.loads(state.json_question)["question"], response=response)
