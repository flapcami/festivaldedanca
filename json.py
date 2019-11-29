from flask import Flask, json, jsonify
from flask import request
from progcami import BailarinoDoGrupo
from playhouse.shortcuts import model_to_dict


app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    return "BLA"


@app.route('/listar_apresentacoes')
def listar_apresentacao():
    # converte para pessoa para inserir em uma lista json
    apresentacao= list(map(model_to_dict, BailarinoDoGrupo.select()))
    # adiciona à lista json um nome
    response = jsonify({"apresentacao": apresentacao})
    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

app.run(debug=True, port=4999)