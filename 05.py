from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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
    Me fale sobre o {carro}.
'''

prompt_template = PromptTemplate.from_template(
    template=template,
)

chain = (
    prompt_template
    | model 
    | StrOutputParser()
)

result = chain.invoke(
    {'carro': 'Marea 20v 199'},
)

print(result)