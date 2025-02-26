from dotenv import load_dotenv # Biblioteca para utilização do dotenv
import os # Biblioteca para utilização do dotenv
import re # Biblioteca para validar se uma string contem um caracter
from langchain_groq import ChatGroq # Biblioteca para utilização do grop
import json # Biblioteca para conversar para json
from langchain_core.runnables import RunnableLambda ## para transformar as funções em etapas para chain aceitar sem erro com |

# Salva a chave api em uma variavel e carrega ela e verificar se está valida
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("A chave de API da Groq não foi encontrada. Verifique se o arquivo .env está configurado corretamente.")

# Modelo Groq
groq = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.5,
    max_retries=2,
)



# Criação de um modelo que contenha algumas expressões matemáticas para validação
math_expressions =  r"[0-9+\-×÷=]|\b(soma|subtração|multiplicação|divisão|igual|)\b"


# Validação aperenta estar correta necessita de mais alguns testes
def validate_question(question: str):
        while True:
            if not re.search(math_expressions,question, re.IGNORECASE): #IGNORECASE
               print("Tente uma pergunta que contenha números ou expressões matemáticas")
               # Tratar o "erro"
            else:
                return question
        
def processing_questions(question):    
    question_dict = {
        "question" : question,
        "category" : "math",
    }

    question_json = json.dumps(question_dict)
    return question_json


def virtual_teacher(json_question):
    prompt = [
    ("system", "You are a math-focused AI. Your goal is to answer math problems, in a simple way, with step-by-step resolutions, clear explanations, in Brazilian Portuguese."),
    ("human", json_question),
    ]
    return prompt

if __name__ == "__main__":

    question = input("Faça uma pergunta matemática: ")

    # Tornando as funçoes 
    valid_question = RunnableLambda(validate_question)
    json_question = RunnableLambda(processing_questions)
    teacher_awnser = RunnableLambda(virtual_teacher)

    # Criação de um Chain
    chain = valid_question | json_question | teacher_awnser | groq

    response = chain.invoke(question)

    print(response.content)