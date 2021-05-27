import json
from flask import Response
from flask_restful import Resource, reqparse
from tinydb import TinyDB, Query, where

# No gerenciamento de usuário está sendo utilizado uma biblioteca que simula um banco de dados
# Os dados de banco ficam salvos no arquivo db.json, no formato de json mesmo
db = TinyDB('db.json')
# Essa biblioteca utiliza o Query() para criar as condições para buscar algum usuário (ex: search.nome == "João")
search = Query()


# Classe que irá receber os dados a partir da URL /user/nome
class User(Resource):
    def get(self, nome):
        # Realiza a busca no banco de dados TinyDB
        user = db.search(search.nome == nome)
        if user:
            # Se encontrar, retorna os dados do usuário em json com status 200
            # A biblioteca retorna uma lista de usuários nas buscas, por isso o user[0]
            # O método json.dumps transforma o objeto em json
            # O parâmetro ensure_ascii como False garante que o json será retornado com suporte a acentuação em PT-BR
            return Response(response=json.dumps(user[0], ensure_ascii=False), mimetype='application/json', status=200)
        # Se não encontrar nenhum usuário, retorna o status 404 (não encontrado)
        return Response(response="Usuário não encontrado", mimetype="text/plain", status=404)

    def post(self, nome):
        # Pega os valores enviados no corpo da requisição POST (ex: os dados de um formulário)
        parser = reqparse.RequestParser()
        parser.add_argument("idade")
        parser.add_argument("ocupacao")
        # Os valores enviados ficam armazenados nesse array
        args = parser.parse_args()

        # Faz a busca pelo nome do usuário para identificar se o mesmo já foi cadastrado
        user = db.search(search.nome == nome)
        if user:
            # Se encontrar um usuário com o mesmo nome, retorna como erro
            return Response(response="Usuário com nome {} já existe".format(nome), mimetype="text/plain", status=400)

        # Se não encontrar usuário repetido, organiza os dados do mesmo em um objeto para inserir no banco de dados
        user = {
            "nome": nome,
            "idade": args["idade"],
            "ocupacao": args["ocupacao"]
        }
        db.insert(user)
        # Retorna com status 201 (criado) e com os dados do usuário cadastrado em json
        return Response(response=json.dumps(user, ensure_ascii=False), mimetype='application/json', status=201)

    def put(self, nome):
        # Pega os valores enviados no corpo da requisição PUT (ex: os dados de um formulário)
        parser = reqparse.RequestParser()
        parser.add_argument("idade")
        parser.add_argument("ocupacao")
        # Os valores enviados ficam armazenados nesse array
        args = parser.parse_args()

        # Os dados são organizados dentro de um novo objeto
        user = {
            "nome": nome,
            "idade": args["idade"],
            "ocupacao": args["ocupacao"]
        }

        # Busca se já existe usuário com esse mesmo nome
        if db.search(search.nome == nome):
            # Se já existir, atualiza os dados do mesmo com os novos valores
            db.update(user, search.nome == nome)
            # Retorna com mensagem de sucesso
            return Response(response=json.dumps(user, ensure_ascii=False), mimetype='application/json', status=200)

        # Se não existir o usuário, insere o mesmo no banco
        db.insert(user)
        # Retorna com o status de criado (201)
        return Response(response=json.dumps(user, ensure_ascii=False), mimetype='application/json', status=201)

    def delete(self, nome):
        # Remove o usuário pelo seu nome
        db.remove(where('nome') == nome)
        # Retorna sucesso na remoção
        return Response(response="{} removido(a).".format(nome), mimetype="text/plain", status=200)


# Classe utilizada para buscar todos os usuários
class UserSearchAll(Resource):
    def get(self):
        users = db.all()
        return Response(response=json.dumps(users, ensure_ascii=False), mimetype='application/json', status=200)

