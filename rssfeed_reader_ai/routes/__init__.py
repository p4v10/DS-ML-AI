from flask import redirect, request
from app import app

@app.route('/test', methods=['GET'])

def test_get():
    return 'Hello from Flask!'

