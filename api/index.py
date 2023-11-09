from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return f'The current URL is: {request.url}'
