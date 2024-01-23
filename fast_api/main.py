from fastapi import FastAPI
import pydantic


app = FastAPI()


@app.get('/')
def menu():
    return {'test': 'test'}

