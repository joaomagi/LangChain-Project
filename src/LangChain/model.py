import json # Biblioteca para converter dicionários para json
import re # Biblioteca para validar se uma string contem um caracter específico 


# Criação de um modelo que contenha algumas expressões matemáticas para validação
math_expressions =  r"[0-9+\-×÷=]|\b(soma|subtração|multiplicação|divisão|igual|Pi)\b"


# Função para validar se a pergunta contém termos matématicos
def validate_question(question: str):
    if not re.search(math_expressions,question, re.IGNORECASE):
       raise ValueError("A pergunta não é sobre matemática")  # Retorna uma exceção caso a pergunta não seja válida
    return question

# Função para processar e converter a perunta para o formato JSON
def processing_questions(question: str):    
    return json.dumps({"question": question, "category":"math"}) # Formata a pergunta como JSON, incluindo a categoria 'math'
  


# Função que estrutura o prompt para um assistente virtual de matemática (Professor virtual)
def virtual_teacher(json_question: str):
    prompt = [
        ("system", "You are a math-focused AI. Your goal is to answer math problems, in a simple way, with step-by-step resolutions, clear explanations, in Brazilian Portuguese."),
        ("human", json_question), # Adiciona a pergunta formatada no prompt
    ]
    return prompt