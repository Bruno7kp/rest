import json
import re
from flask import Response
from flask_restful import Resource


# Classe que irá receber os dados a partir da URL /cpf/valor
class Cpf(Resource):
    def get(self, cpf):
        # Essa classe necessita apenas do GET, já que não precisa cadastrar nem remover nada, apenas validar o CPF
        # Se for válido retorna status 200 (sucesso), se não retorna status 400 (erro)
        if validate(cpf):
            response = Response(response=json.dumps(True), mimetype="application/json", status=200)
            # Header necessário para poder usar requisição via navegador/JavaScript
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        response = Response(response=json.dumps(False), mimetype="application/json", status=400)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response


# Método que valida o cpf
def validate(cpf: str) -> bool:
    # Se passar apenas números sem formatação, adiciona a formatação
    if len(cpf) == 11:
        cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True
