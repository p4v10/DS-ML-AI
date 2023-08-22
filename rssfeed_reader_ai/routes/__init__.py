from flask import redirect, requests
from app import app

@app.route('/test', method=['GET'])

def test_get():
    return 'Hello from Flask!'

