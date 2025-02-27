from langgraph.graph import StateGraph, END
from dataclasses import dataclass
import re
import json
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    raise ValueError("A chave de API da Groq não foi encontrada. Verifique se o arquivo .env está configurado corretamente.")

groq = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.5,
    max_retries=2,
)

math_expressions = r"[0-9+\-×÷=]|\b(soma|subtração|multiplicação|divisão|igual|Pi)\b"

@dataclass
class MathState:
    question: str
    response: str = ""

def validate_question(question: str):
    if not re.search(math_expressions, question, re.IGNORECASE):
        raise ValueError("A pergunta não é sobre matemática")
    return question

def validate_node(state: MathState):
    validate_question(state.question)
    return JSONState(text=state.question)

@dataclass
class JSONState:
    text: str
    category: str = "math"

    def to_json(self):
        return json.dumps({"question": self.text, "category": self.category})

def to_json_node(state: JSONState):
    return VirtualTeacherState(json_question=state.to_json())

@dataclass
class VirtualTeacherState:
    json_question: str

    def generate_prompt(self):
        return [
            {"role": "system", "content": "You are a math-focused AI. Your goal is to answer math problems, in a simple way, with step-by-step resolutions, clear explanations, in Brazilian Portuguese."},
            {"role": "user", "content": self.json_question},
        ]

def virtual_teacher_node(state: VirtualTeacherState):
    prompt = state.generate_prompt()
    response_obj = groq.invoke(prompt)  
    response = response_obj.content
    return MathState(question=json.loads(state.json_question)["question"], response=response)

workflow = StateGraph(MathState)

workflow.add_node("validate_question", validate_node)
workflow.add_node("to_json", to_json_node)
workflow.add_node("virtual_teacher", virtual_teacher_node)

workflow.add_edge("validate_question", "to_json")
workflow.add_edge("to_json", "virtual_teacher")
workflow.add_edge("virtual_teacher", END)

workflow.set_entry_point("validate_question")

app = workflow.compile()

result = app.invoke(MathState(question="2 + 2"))
print("Resultado:", result.get("response"))
