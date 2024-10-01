from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    return os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model = "gpt-3.5-turbo",
    api_key=configure(),
)


## loader = TextLoader('base_conhecimentos/base_conhecimento.pdf')
## documents = loader.load()

## loader = PyPDFLoader('base_conhecimentos/base_conhecimento.pdf')
## documents = loader.load()

loader = CSVLoader('base_conhecimentos/base_conhecimento.csv')
documents = loader.load()

prompt_base_conhecimento = PromptTemplate(
    input_variables=['contexto', 'pergunta'],
    template='''
        Use o seguinte contexto para responder à pergunta.
        Responda apenas com base nas informações fornecidas.
        Não utilize informações externas ao contexto:
        Contexto: {contexto}
        Pergunta: {pergunta}
    '''
)

chain = (
    prompt_base_conhecimento
    | model
    | StrOutputParser()
)

respose = chain.invoke(
    {
        'contexto': '\n'.join(doc.page_content for doc in documents),
        'pergunta': 'Qual carro é mais novo?'
    }
)

print(respose)