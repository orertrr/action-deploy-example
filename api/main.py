'''api hello world'''
from fastapi import FastAPI, Request

app = FastAPI(root_path="/api")

@app.get('/')
async def index():
    '''index'''
    return {"Hello": "World"}
