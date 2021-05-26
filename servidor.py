from flask import Flask
from flask_restful import Api
from src.calc import Calc
from src.cpf import Cpf
from src.user import User

app = Flask(__name__)
api = Api(app)
api.add_resource(User, "/user/<string:nome>")
api.add_resource(Calc, "/calc/<string:num1>/<string:operador>/<string:num2>")
api.add_resource(Cpf, "/cpf/<string:cpf>")

app.run(debug=True)
