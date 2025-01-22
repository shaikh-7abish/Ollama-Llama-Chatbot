from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title='Langchain Server',
    version='1.0',
    description='A simple API Server'
)

add_routes(

    app,
    ChatOpenAI(),
    path='/openai'

)

model = ChatOpenAI()
llm = Ollama(model='llama3.2')

prompt1 = ChatPromptTemplate.from_template('Write me and Essay about {topic} with 100 words')
prompt2 = ChatPromptTemplate.from_template('Write me and Poem about {topic} with 100 words')

add_routes(

    app,
    prompt1 | model,
    path='/essay'

)

add_routes(

    app,
    prompt2 | llm,
    path='/poem'

)

if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8000)

# run this file to and go to localhost:8000 
# goto localhost:8000/docs for background process, it is known as Swagger UI documentation