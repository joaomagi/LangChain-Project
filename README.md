# LangChain-Project

## Introdução
Este documento serve como base para a implementação de um pipeline utilizando LangChain e Groq. O objetivo é validar perguntas matemáticas, processá-las em formato JSON e utilizar um modelo de IA para fornecer respostas explicativas de forma simples.

## Dependências
Certifique-se de instalar as seguintes bibliotecas antes de executar o código:

```bash
pip install -r requirements.txt
```

## Configuração do Ambiente
Crie um arquivo `.env` e adicione sua chave de API da Groq:

```ini
GROQ_API_KEY=SuaChaveAPI
```

Carregue as variáveis de ambiente no seu script utilizando `dotenv`.

## Estrutura do Código
O código é estruturado em funções que desempenham as seguintes tarefas:

1. **Validação de Perguntas:**
   - Verifica se a pergunta contém números ou expressões matemáticas.

2. **Processamento da Pergunta:**
   - Converte a pergunta para um formato JSON para enviar para a IA ("Professor Virtual")

3. **Interação com a IA:**
   - Define o prompt para a IA ("Professor Virtual") responder de maneira didática e simples.

4. **Execução da Cadeia:**
   - Utiliza `RunnableLambda` para encadear as operações de validação, processamento e resposta.

## Exemplo de Entrada/Saída
### Entrada:
Usuário digita:
```
Quanto é 2 + 2?
```
### Saída:
IA responde com explicação passo a passo:
```
Para resolver 2 + 2:
1. Pegamos o número 2.
2. Somamos 2 a ele.
3. O resultado final é 4.
```

## Referências
- [Documentação Oficial do LangChain](https://python.langchain.com/)
- [Console Groq](https://console.groq.com/docs/text-chat)

