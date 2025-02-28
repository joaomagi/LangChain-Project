# LangChain-Project

## Introdução
Este documento apresenta duas abordagens para a construção de um professor virtual especializado em matemática, utilizando LangChain e LangGraph. O objetivo é demonstrar diferentes perspectivas para essa implementação, fazendo uso da API da Groq para o processamento e geração de respostas.

- [LangChain](#LangChain)  
- [LangGraph](#LangGraph)
- [Visualização do Fluxo](#visualiza%C3%A7%C3%A3o-do-fluxo)  
- [Exemplos de Entrada/Saída](#exemplos-de-entrada-sa%C3%ADda)
- [Referências](#refer%C3%AAncias)
  
## Pré Requisitos
- Python 3.12
- Git

## Dependências
Certifique-se de instalar as seguintes bibliotecas antes de executar os códigos:

```cmd
pip install -r requirements.txt
```

## Configuração do Ambiente
Crie um arquivo `.env` e adicione sua chave de API da Groq:

```ini
GROQ_API_KEY=SuaChaveAPI
```
Carregue as variáveis de ambiente no seu script utilizando `dotenv`.

# LangChain
Este capítulo serve como base para a implementação de um pipeline utilizando LangChain e Groq. O objetivo é validar perguntas matemáticas, processá-las em formato JSON e utilizar um modelo de IA para fornecer respostas explicativas de forma simples.

## Utilizando o Programa
Após instalar as dependências e configurar sua chave de API, navegue até o diretório do projeto e execute:

```cmd
python main.py
```
Exemplo de caminho de diretório:
```cmd
C:\LangChain-Project\src\LangChain>
```

## Estrutura do Código
O código é estruturado com as seguintes funções:

1. **validate_question:**
   - Verifica se a pergunta contém números ou expressões matemáticas.

2. **to_json:**
   - Converte a pergunta para um formato JSON para enviar para a IA ("Professor Virtual").

3. **virtual_teacher:**
   - Define o prompt para a IA responder de maneira didática e simples.

4. **Execução da Cadeia:**
   - Utiliza `RunnableLambda` para encadear as operações de validação, processamento e resposta.

# LangGraph
Este capítulo implementa um fluxo de trabalho utilizando LangGraph. Assim como no LangChain, cria um sistema de perguntas e respostas matemáticas, processando as perguntas do usuário, validando se são matemáticas, convertendo para JSON e utilizando um professor virtual para gerar respostas.

## Estrutura do Código
O fluxo de trabalho é definido utilizando `StateGraph` da biblioteca LangGraph. Ele possui os seguintes nós:

1. **validate_receptor:** Valida se a pergunta do usuário é matemática.

2. **to_json:** Converte a pergunta validada para JSON.

3. **virtual_teacher:** Processa a pergunta utilizando um professor virtual.

A conexão entre os nós ocorre na seguinte ordem:

- `validate_receptor` → `to_json`
- `to_json` → `virtual_teacher`
- `virtual_teacher` → `END`

O ponto de entrada do fluxo é o nó `validate_receptor`.

## Visualização do Fluxo
Para gerar uma representação visual do fluxo LangGraph, é necessário instalar a biblioteca necessária e utilizar o seguinte código:

```cmd
pip install ipython
````

```python
from IPython.display import Image, display

mermaid_code = str(app.get_graph().draw_mermaid())

with open("graph.mmd", "w") as f:
    f.write(mermaid_code)

print("Diagrama Mermaid salvo como graph.mmd")
```

<p align="center">
<img src="https://github.com/joaomagi/LangChain-Project/blob/main/Images/DiagramaWorkflow.png" width="400">
</p>

## Exemplos de Entrada/Saída
Esses exemplos servem tanto para o LangChain quanto para o LangGraph.

### Entrada 1:
Usuário digita:
```
Quanto é 2 + 2?
```
### Saída 1:
IA responde com explicação passo a passo:
```
Para resolver 2 + 2:
1. Pegamos o número 2.
2. Somamos 2 a ele.
3. O resultado final é 4.
```

### Entrada 2:
Usuário digita:
```
Uma família tem 6 filhos. Se cada filho tem 2 irmãos a mais do que irmãs, quantos meninos e quantas meninas há na família?
```
### Saída 2:
```
Vamos resolver isso passo a passo.

Se cada filho tem 2 irmãos a mais do que irmãs, isso significa que o número de irmãos de cada filho é 2 a mais do que o número de irmãs.

Vamos supor que o número de meninas seja x. Então, o número de meninos será x + 2. Como a família tem 6 filhos no total, podemos escrever a equação:

x + (x + 2) = 6

Agora, vamos resolver essa equação:

2x + 2 = 6

Subtraímos 2 de ambos os lados:

2x = 4

Dividimos ambos os lados por 2:

x = 2

Então, o número de meninas é 2 e o número de meninos é 4.
```

### Entrada 3:
Usuário digita:
```
Resolva a equação: x(x+3) = 40
```
### Saída 3:
```
Vamos resolver essa equação!

A equação é: x(x+3) = 40

Primeiro, expandimos o produto:

x² + 3x = 40

Agora, rearranjamos a equação:

x² + 3x - 40 = 0

Essa é uma equação do segundo grau. Vamos fatorar:

(x + 8)(x - 5) = 0

Encontramos as soluções:

x + 8 = 0 ou x - 5 = 0

x = -8 ou x = 5

Portanto, as soluções da equação são x = -8 e x = 5.
```

## Tecnologias Utilizadas

- Python  
- LangGraph  
- LangChain  
- ChatGroq  
- dotenv  
- JSON  

## Referências
- [Documentação Oficial do LangChain](https://python.langchain.com/)
- [Documentação Oficial do LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- [Console Groq](https://console.groq.com/docs/text-chat)
- [Curso Udemy](https://www.udemy.com/course/lanchain/?couponCode=KEEPLEARNINGBR)

