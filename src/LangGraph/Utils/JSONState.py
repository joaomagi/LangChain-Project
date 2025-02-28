from dataclasses import dataclass # Biblioteca para facilitar a criação de classes, gerando automaticamente métodos como __init__, __repr__,
import json # Biblioteca para converter dicionários para json




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
    from LangGraph.Utils.VirtualTeacherState import VirtualTeacherState # Importa a Classe VirtualTeacherState
    return VirtualTeacherState(json_question=state.to_json())