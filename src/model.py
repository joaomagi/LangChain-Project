import json # Biblioteca para conversar para json
import re # Biblioteca para validar se uma string contem um caracter


# Criação de um modelo que contenha algumas expressões matemáticas para validação
math_expressions =  r"[0-9+\-×÷=]|\b(soma|subtração|multiplicação|divisão|igual)\b"


# Validação aperenta estar correta necessita de mais alguns testes
def validate_question(question: str):
    if not re.search(math_expressions,question, re.IGNORECASE): #IGNORECASE
       raise ValueError("A pergunta não é sobre matemática")  # Envia uma exceção em vez de retornar erro
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