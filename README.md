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

## Utilizando o Programa
Após realizar a instalação das dependencias e configuração da sua chave API pasta realizar esse comando no CMD (É necessário arrumar o caminho para a pasta corretamente usando cd "NomeDoDiretorio"
```cmd
C:\LangChain-Project\src> python main.py
```

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

## Exemplos de Entrada/Saída
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
Uma família tem 6 filhos, se cada filho tem 2 irmãos a mais do que irmãs, quantos meninos e quantas meninas há na família?
```
### Saída 2:
```
Vamos resolver isso passo a passo.

Se cada filho tem 2 irmãos a mais do que irmãs, isso significa que o número de irmãos de cada filho é 2 a mais do que o número de irmãs.

Vamos supor que o número de meninas seja x. Então, o número de meninos será x + 2, pois cada menino tem 2 irmãos a mais do que irmãs. 

Como a família tem 6 filhos no total, podemos escrever a equação:

x + (x + 2) = 6

Agora, vamos resolver essa equação:

2x + 2 = 6

Subtraimos 2 de ambos os lados:

2x = 4

Dividimos ambos os lados por 2:

x = 2

Então, o número de meninas é 2. E o número de meninos é 2 + 2 = 4.

Portanto, há 2 meninas e 4 meninos na família.

```
### Entrada 3:
Usuário digita:
```
Resolva a equação : x(x+3) = 40
```
### Saída 3:
```
Vamos resolver essa equação!

A equação é: x(x+3) = 40

Primeiro, vamos expandir o produto:

x² + 3x = 40

Agora, vamos rearranjar a equação para que todos os termos fiquem do mesmo lado:

x² + 3x - 40 = 0

Essa é uma equação do segundo grau. Vamos fatorar:

(x + 8)(x - 5) = 0

Agora, podemos encontrar os valores de x que fazem a equação ser verdadeira:

x + 8 = 0 ou x - 5 = 0

Resolvendo as duas equações, encontramos:

x = -8 ou x = 5

Portanto, as soluções da equação são x = -8 e x = 5.

```

## Referências
- [Documentação Oficial do LangChain](https://python.langchain.com/)
- [Console Groq](https://console.groq.com/docs/text-chat)
- [Curso Udemy](https://www.udemy.com/course/lanchain/?couponCode=KEEPLEARNINGBR)
