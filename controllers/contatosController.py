from flask import Blueprint, render_template, request, redirect
from models.contatosModel import Contato

contatosController = Blueprint('contatosController', __name__, template_folder='../views')

@contatosController.route('/')
def index():
    return render_template('contatos.html', resultados=Contato.obter_todos())

@contatosController.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        contato = Contato(None, nome, email, telefone)
        contato.salvar()
        return redirect('/')
    else:
        return render_template('adicionar.html')

def register(app):
    app.register_blueprint(contatosController)

