from dataclasses import dataclass # Biblioteca para facilitar a criação de classes, gerando automaticamente métodos como __init__, __repr__,
import re # Biblioteca para validar se uma string contem um caracter específico 


# Criação de uma variável que contenha algumas expressões matemáticas para validação
math_expressions = r"[0-9+\-×÷=]|\b(soma|subtração|multiplicação|divisão|igual|pi)\b"

# Define uma classe para armazenar o estado da pergunta e resposta matemáticas
@dataclass # O decorador @dataclass simplifica a criação de classes
class MathState:
    question: str
    response: str = ""

    # Validar se a pergunta contém termos matématicos
    def validate_question(self):
        if not re.search(math_expressions, self.question, re.IGNORECASE):
            raise ValueError("A pergunta não é sobre matemática")
        return self.question

# Nó de validação
def validate_node(state: MathState):
    from LangGraph.Utils.JSONState import JSONState
    state.validate_question()  
    return JSONState(state.question)
