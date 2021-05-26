import json
from flask import Response
from flask_restful import Resource, reqparse
from tinydb import TinyDB, Query, where

db = TinyDB('db.json')
search = Query()


class User(Resource):
    def get(self, nome):
        user = db.search(search.nome == nome)
        if user:
            return Response(response=json.dumps(user[0], ensure_ascii=False), mimetype='application/json', status=200)
        return Response(response="Usuário não encontrado", mimetype="text/plain", status=404)

    def post(self, nome):
        parser = reqparse.RequestParser()
        parser.add_argument("idade")
        parser.add_argument("ocupacao")
        args = parser.parse_args()

        user = db.search(search.nome == nome)
        if user:
            return Response(response="Usuário com nome {} já existe".format(nome), mimetype="text/plain", status=400)

        user = {
            "nome": nome,
            "idade": args["idade"],
            "ocupacao": args["ocupacao"]
        }

        db.insert(user)
        return Response(response=json.dumps(user, ensure_ascii=False), mimetype='application/json', status=201)

    def put(self, nome):
        parser = reqparse.RequestParser()
        parser.add_argument("idade")
        parser.add_argument("ocupacao")
        args = parser.parse_args()

        user = {
            "nome": nome,
            "idade": args["idade"],
            "ocupacao": args["ocupacao"]
        }

        if db.search(search.nome == nome):
            db.update(user, search.nome == nome)
            return Response(response=json.dumps(user, ensure_ascii=False), mimetype='application/json', status=200)

        db.insert(user)
        return Response(response=json.dumps(user, ensure_ascii=False), mimetype='application/json', status=201)

    def delete(self, nome):
        db.remove(where('nome') == nome)
        return Response(response="{} deletado.".format(nome), mimetype="text/plain", status=200)

