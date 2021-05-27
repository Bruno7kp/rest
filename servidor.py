# Classes do framework Flask
from flask import Flask, Response
from flask_restful import Api
# Classes criadas para rodar os serviços de validação de CPF, cadastro de usuário, etc.
from src.calc import Calc
from src.cpf import Cpf
from src.user import User, UserSearchAll

# Inicia a aplicação em python
app = Flask(__name__)
api = Api(app)

# Define as rotas utilizadas para acessar os serviços
# Rota para o gerenciamento do usuário
api.add_resource(User, "/user/<string:nome>")
# Rota para listar todos os usuários
api.add_resource(UserSearchAll, "/users")
# Rota para o cálculo de dois números
api.add_resource(Calc, "/calc/<string:num1>/<string:operador>/<string:num2>")
# Rota para validar o cpf
api.add_resource(Cpf, "/cpf/<string:cpf>")


# Caso seja acessada alguma rota que não esteja definida acima, mostra essa resposta por padrão
@app.errorhandler(404)
def page_not_found(e):
    # Retorna uma resposta padrão com o status 404
    return Response(response="Recurso não encontrado", mimetype="text/plain", status=404)


# Inicia o servidor
app.run(debug=True)
