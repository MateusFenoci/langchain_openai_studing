from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    return os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model = "gpt-3.5-turbo",
    api_key=configure(),
)

chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="Você deve responder baseado em dados geográficos de regiões do Brasil."),
    HumanMessagePromptTemplate.from_template('Por favor, me fale sobre a região {regiao}.'),
    AIMessage(content="Claro, vou começar coletando informações sobre a região e analisar os dados disponíveis."),
    HumanMessage(content='Certifique-se de incluir dados demográficos.'),
    AIMessage(content='Entendido, vou incluir dados demográficos. Aqui estão os dados:'),
])

prompt = chat_template.format_messages(regiao='Nordeste')

response = model.invoke(prompt)

print(response.content)