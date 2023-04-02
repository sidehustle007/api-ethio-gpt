from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
from dotenv import dotenv_values
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None)

main_api_key = dotenv_values('.env')

openai.api_key = main_api_key['api_key']


origins = [
    'https://ethiogpt.vercel.app'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins='https://ethiogpt.vercel.app',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*'],
)


@app.get('/', tags=['get'])
def main():
    return 'hello'


pcode_code = main_api_key['pcode_code']


@app.get('/pcode', tags=['get'])
def pcode():
    return {
        'code': 'do you really checked this end point to get the code 😂😂😂😂',
        'tip': "i don't tell you, but its near u ur home"
    }


@app.post('/pcode', tags=['post'])
def pcode():
    return pcode_code


class Data(BaseModel):
    code: str
    text: str


@app.post('/post', tags=['post'])
def post(data: Data):
    if data.code == pcode_code:
        res = openai.Completion.create(
            engine='text-davinci-003',
            prompt=data.text,
            max_tokens=250,
            temperature=0.9,
            top_p=1.0
        )
        return res
    else:
        res2 = openai.Completion.create(
            engine='text-davinci-003',
            prompt=data.text,
            max_tokens=150,
            temperature=0.5,
            top_p=1.0
        )
        return res2


@app.get('/ip', tags=['get'])
def ip(req: Request):
    return req.client.host
