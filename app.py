from flask import Flask

app = Flask(__name__)
app.secret_key = "AJfgYDcZwdw3A4xSAYU9"

@app.route('/')
def index():
    return '''
        <h1>Bienvenue sur notre E-commerce</h1>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000)
