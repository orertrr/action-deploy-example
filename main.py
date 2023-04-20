'''Hello world'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''Index Page'''
    return 'hello world2'
