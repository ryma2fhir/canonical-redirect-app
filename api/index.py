from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return f'Welcome to our URL redirector!'

@app.route('/')
@app.route('/<first>')
@app.route('/<first>/<path:rest>')
def fallback(first=None, rest=None):
    return f'The current URL is: {request.url}'