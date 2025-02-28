from dataclasses import dataclass # Biblioteca para facilitar a criação de classes, gerando automaticamente métodos como __init__, __repr__,

from typing import Annotated # Permite adicionar informações extras aos tipos
from typing_extensions import TypedDict # Define dicionários tipados com chaves específicas

from langgraph.graph.message import add_messages # Representa uma lista de mensagens na conversa

# Define o estado da conversa com uma lista de mensagens
class State(TypedDict):
    messages: Annotated[list, add_messages]