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
    
@contatosController.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    contato = Contato(id, '', '', '')
    contato.excluir()
    return redirect('/')

@contatosController.route('/excluir/<int:id>', methods=['GET'])
def confirmar_exclusao(id):
    contato = Contato.obter_por_id(id)
    return render_template('excluir.html', id=id, contato=contato)

@contatosController.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        contato = Contato(id, nome, email, telefone)
        contato.atualizar()
        return redirect('/')
    else:
        contato = Contato.obter_por_id(id)
        return render_template('atualizar.html', contato=contato)


def register(app):
    app.register_blueprint(contatosController)

