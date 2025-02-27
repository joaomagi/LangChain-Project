from langgraph.graph import StateGraph, END

from model import MathState, validate_node
from model import to_json_node
from model import virtual_teacher_node
from model import State

from IPython.display import Image, display

workflow = StateGraph(MathState)

workflow.add_node("validate_receptor", validate_node)
workflow.add_node("to_json", to_json_node)
workflow.add_node("virtual_teacher", virtual_teacher_node)

workflow.add_edge("validate_receptor", "to_json")
workflow.add_edge("to_json", "virtual_teacher")
workflow.add_edge("virtual_teacher", END)

workflow.set_entry_point("validate_receptor")

app = workflow.compile()

state = State(menssages=[])
if __name__ == "__main__":
    while True:
        try: 
            # Solicita uma perunta matemática ao usuário
            user_input = input("Faça uma pergunta matématica: ")
            # Da a opção de sair do programa ao usuário
            if user_input.lower() == "sair":
                print("Saindo....")
                break
            result = app.invoke(MathState(user_input))
            print("Resultado:", result.get("response"))
            print('\nCaso queira sair digite "Sair"\n')
        
        except ValueError as e: # Tratamento do erro caso o usário nao faça uma pergunta matemática
            print(e)
            print("Tente novamente ")
    

""""
mermaid_code = str(app.get_graph().draw_mermaid())

with open("graph.mmd", "w") as f:
    f.write(mermaid_code)

print("Diagrama Mermaid salvo como graph.mmd")
"""