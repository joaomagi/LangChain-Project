from dotenv import load_dotenv # Biblioteca para utilização do dotenv
import os # Biblioteca para utilização do dotenv
from langchain_groq import ChatGroq # Biblioteca para utilização do grop

from langchain_core.runnables import RunnableLambda ## para transformar as funções em etapas para chain aceitar sem erro com |

from model import validate_question
from model import processing_questions
from model import virtual_teacher

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