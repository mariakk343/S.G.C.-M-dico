from app import app
from flask import render_template, request, redirect, url_for

from app.models.atendimento_model import AtendimentoModel
from app.service.atendimento_service import AtendimentoService
from app.models.cliente_model import ClienteModel
from app.service.cliente_service import ClienteService

atendimento_service = AtendimentoService()
cliente_service = ClienteService()

@app.route('/')
def index():
    return redirect(url_for('listar_clientes'))

# --------------------
# CLIENTES
# --------------------
@app.route('/clientes')
def listar_clientes():
    clientes = cliente_service.get_all_clientes()
    return render_template('clientes/list.html', clientes=clientes)

@app.route('/clientes/novo', methods=['GET', 'POST'])
def criar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        data_nascimento = request.form['data_nascimento']
        cliente_service.create_cliente(ClienteModel(
            id=None,
            nome=nome,
            telefone=telefone,
            data_nascimento=data_nascimento))
        return redirect(url_for('listar_clientes'))
    return render_template('clientes/form.html')

@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = cliente_service.get_cliente_by_id(id)
    if request.method == 'POST':
        cliente_service.update_cliente(
            ClienteModel(
                id,
                request.form['nome'],
                request.form.get('telefone'),
                request.form.get('data_nascimento')
            )
        )
        return redirect(url_for('listar_clientes'))
    return render_template('clientes/form.html', cliente=cliente)

@app.route('/clientes/excluir/<int:id>')
def excluir_cliente(id):
    cliente_service.delete_cliente(id)
    return redirect(url_for('listar_clientes'))

# --------------------
# ATENDIMENTOS
# --------------------
@app.route('/atendimentos')
def listar_atendimentos():
    atendimentos = atendimento_service.get_all_atendimentos()
    return render_template('atendimentos/list.html', atendimentos=atendimentos)

@app.route('/atendimentos/novo', methods=['GET', 'POST'])
def criar_atendimento():
    clientes = cliente_service.get_all_clientes()
    if request.method == 'POST':
        data = request.form['data']
        hora = request.form['hora']
        motivo = request.form['motivo']
        cliente_id = request.form['cliente_id']
        atendimento_service.create_atendimento(AtendimentoModel(
            id=None,
            data=data,
            hora=hora,
            motivo=motivo,
            cliente_id=cliente_id
        ))
        return redirect(url_for('listar_atendimentos'))
    return render_template('atendimentos/form.html', clientes=clientes)

@app.route('/atendimentos/editar/<int:id>', methods=['GET', 'POST'])
def editar_atendimento(id):
    atendimento = atendimento_service.get_atendimento_by_id(id)
    clientes = cliente_service.get_all_clientes()
    if request.method == 'POST':
        atendimento_service.update_atendimento(AtendimentoModel(
            id=id,
            cliente_id=request.form['cliente_id'],
            data=request.form['data'],
            descricao=request.form.get('descricao')
        ))
        return redirect(url_for('listar_atendimentos'))
    return render_template('atendimentos/form.html', atendimento=atendimento, clientes=clientes)

@app.route('/atendimentos/excluir/<int:id>')
def excluir_atendimento(id):
    atendimento_service.delete_atendimento(id)
    return redirect(url_for('listar_atendimentos'))
