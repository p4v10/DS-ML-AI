from flask import redirect, request
from app import app

# create a basic get request to allow user input the username
@app.route('/test', methods=['GET'])
def test_get():
    return '<form method="POST"><input name="username"></form>'

# post request that returns username
@app.route('/test', methods=['POST'])
def test_post():
    username = request.form.get('username', 'no username')
    return 'Hello ' + username