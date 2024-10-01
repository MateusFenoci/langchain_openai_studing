from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    return os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model = "gpt-3.5-turbo",
    api_key=configure(),
)

template = '''
    Traduza o texto {idioma1} para o {idioma2}:
    {texto}
'''

prompt_template = PromptTemplate.from_template(
    template=template,
)

prompt = prompt_template.format(
    idioma1='inglês',
    idioma2='português',
    texto='Hello, how are you?',
)

response = model.invoke(prompt)

print(response.content)
## Saida: Olá, como você está?