from flask import Flask
from controllers.contatosController import contatosController, register

app = Flask(__name__)

register(app)

if __name__ == '__main__':
    app.run(debug=True)
