from flask import Flask
from flask_restful import Api, Resource, reqparse

usuarios = [{
    "nome": "Abc",
    "idade": 42,
    "ocupacao": "oreia"
}, {
    "nome": "Bolinhas",
    "idade": 32,
    "ocupacao": "seca"
}, {
    "nome": "Uniplac",
    "idade": 22,
    "ocupacao": "estagiário"}]

class User(Resource):
    def get(self, nome):
        for user in usuarios:
            if nome == user["nome"]:
                return user, 200
        return "Usuário não encontrado", 404

    def post(self, nome):
        parser = reqparse.RequestParser()

        parser.add_argument("idade")
        parser.add_argument("ocupacao")
        args = parser.parse_args()
        for user in usuarios:
            if nome == user["nome"]:
                return "Usuário com nome {} já existe".format(nome), 400

        user = {
            "nome": nome,
            "idade": args["idade"],
            "ocupacao": args["ocupacao"]
        }
        usuarios.append(user)
        return user, 201

    def put(self, nome):
        parser = reqparse.RequestParser()
        parser.add_argument("idade")
        parser.add_argument("ocupacao")
        args = parser.parse_args()
        for user in usuarios:
            if nome == user["nome"]:
                user["idade"] = args["idade"]
                user["ocupacao"] = args["ocupacao"]
                return user, 200

        user = {
            "nome": nome,
            "idade": args["idade"],
            "ocupacao": args["ocupacao"]
        }
        usuarios.append(user)
        return user, 201

    def delete(self, nome):
        global usuarios
        usuarios = [user for user in usuarios if user["nome"] != nome]
        return "{} deletado.".format(nome), 200


app = Flask(__name__)
api = Api(app)
api.add_resource(User, "/user/<string:nome>")

app.run(debug=True)
