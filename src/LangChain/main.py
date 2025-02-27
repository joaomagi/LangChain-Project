from dotenv import load_dotenv  # Biblioteca para utilização do dotenv
import os # Biblioteca para interação com o sistema operacional, usada nesse caso para carregar variáveis de ambiente
from langchain_groq import ChatGroq # Biblioteca para utilização do grop

from langchain_core.runnables import RunnableLambda # Permite encapsular funções como etapas reutilizáveis em pipelines do LangChain

# Importando as funçoes do módulo "model"
from model import validate_question
from model import processing_toJSON
from model import virtual_teacher

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


if __name__ == "__main__":
    while True: 
        try:
            # Solicita uma perunta matemática ao usuário
            user_input = input("Faça uma pergunta matématica: ")
            # Da a opção de sair do programa ao usuário
            if user_input.lower() == "sair":
                print("Saindo....")
                break

            # Criando funções como etapas para a Chain
            valid_question = RunnableLambda(validate_question)        
            json_question = RunnableLambda(processing_toJSON)
            teacher_awnser = RunnableLambda(virtual_teacher)

            # Criação de um Chain        
            chain = valid_question | json_question | teacher_awnser | groq

            # Obtendo resposta do modelo e imprimindo na tela
            response = chain.invoke(user_input)
            print(response.content)

            print("\nCaso queira sair digite Sair\n")

        except ValueError as e: # Tratamento do erro caso o usário nao faça uma pergunta matemática
            print(e)
            print("Tente novamente ")
