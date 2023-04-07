'''api hello world'''
from fastapi import FastAPI, Request

app = FastAPI(root_path="/api")

@app.get('/')
async def index():
    '''index'''
    return {"Hello": "World"}

@app.get('/checkpath')
async def get_path(request: Request):
    '''Get path'''
    return f'{request.scope.get("root_path")}'
