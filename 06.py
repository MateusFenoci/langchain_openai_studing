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


classification_chain = (
    PromptTemplate.from_template(
    '''
        Classifique a pergunta do usuario em um dos seguintes tópicos:
        - Financeiro
        - Suporte Técnico
        - Outras informações

        Pergunta: {pergunta}
    '''
    )
    | model
    | StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
    '''
        Você é um especialista financeiro.
        Sempre responda às perguntas começando com "Bem-vindo ao Setor Financeiro".
        
        Pergunta: {pergunta}
    '''
    )
    | model
    | StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
    '''
        Você é um especialista financeiro.
        Sempre responda às perguntas começando com "Bem-vindo ao Suporte Técnico".
        
        Pergunta: {pergunta}
    '''
    )
    | model
    | StrOutputParser()
)

other_info_chain = (
    PromptTemplate.from_template(
    '''
        Você é um especialista financeiro.
        Sempre responda às perguntas começando com "Bem-vindo ao Setor de Informações".
        
        Pergunta: {pergunta}
    '''
    )
    | model
    | StrOutputParser()
)

def route(classification):
    classification = classification.lower()
    
    if 'financeiro' in classification:
        return financial_chain
    
    elif 'suporte técnico' in classification:
        return tech_support_chain
    
    else:
        return other_info_chain
    
pergunta = input('Digite sua pergunta: ')

classification = classification_chain.invoke(
    {'pergunta': pergunta}
)

response_chain = route(classification=classification)

response = response_chain.invoke(
    {'pergunta': pergunta}
)

print(response)