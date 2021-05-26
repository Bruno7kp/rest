from flask import Flask
from flask_restful import Api
from src.calc import Calc
from src.cpf import Cpf
from src.user import User

app = Flask(__name__)
api = Api(app)
api.add_resource(User, "/user/<string:nome>")
api.add_resource(Calc, "/calc/<int:num1>/<string:operador>/<int:num2>")
api.add_resource(Cpf, "/cpf/<string:cpf>")

app.run(debug=True)
