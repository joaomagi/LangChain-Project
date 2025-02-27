from langgraph.graph import StateGraph, END

from model import MathState, validate_node
from model import to_json_node
from model import virtual_teacher_node

workflow = StateGraph(MathState)

workflow.add_node("validate_question", validate_node)
workflow.add_node("to_json", to_json_node)
workflow.add_node("virtual_teacher", virtual_teacher_node)

workflow.add_edge("validate_question", "to_json")
workflow.add_edge("to_json", "virtual_teacher")
workflow.add_edge("virtual_teacher", END)

workflow.set_entry_point("validate_question")

app = workflow.compile()

question = input("Digite sua pergunta matemática: ")
result = app.invoke(MathState(question))
print("Resultado:", result.get("response"))
