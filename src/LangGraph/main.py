from langgraph.graph import StateGraph, END # Biblioteca para criação dos grafos

# Importando classes e funções responsáveis pelo fluxo de trabalho
from LangGraph.Utils.State import State
from LangGraph.Utils.MathState import MathState, validate_node
from LangGraph.Utils.JSONState import to_json_node
from LangGraph.Utils.VirtualTeacherState import virtual_teacher_node


# Inicializa o fluxo de trabalho com a classe MathState
workflow = StateGraph(MathState)

# Adiciona os nós ao fluxo de trabalho
workflow.add_node("validate_receptor", validate_node)  # Valida a entrada do usuário
workflow.add_node("to_json", to_json_node)  # Converte a entrada para JSON
workflow.add_node("virtual_teacher", virtual_teacher_node)  # Processa a pergunta com o professor virtual

# Define as conexões entre os nós
workflow.add_edge("validate_receptor", "to_json")
workflow.add_edge("to_json", "virtual_teacher")
workflow.add_edge("virtual_teacher", END)

# Define o ponto de entrada do fluxo
workflow.set_entry_point("validate_receptor")

# Compila o fluxo de trabalho
app = workflow.compile()

# Inicializa o estado do sistema
state = State(menssages=[])

def main():
    while True:
        try: 
            # Solicita uma perunta matemática ao usuário
            user_input = input("Faça uma pergunta matemática: ")
            
            # Dá a opção de sair do programa ao usuário
            if user_input.lower() == "sair":
                print("Saindo....")
                break
            
            # Processa a pergunta no fluxo de trabalho
            result = app.invoke(MathState(user_input))
            print("Resultado:", result.get("response"))

            print('\nCaso queira sair digite "Sair"\n')
        
        except ValueError as e:  # Tratamento do erro caso o usário nao faça uma pergunta matemática
            print(e)
            print("Tente novamente ")

if __name__ == "__main__": # Verifica se o nome atual é main
    main()
    
    
    
    