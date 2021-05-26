import json
from flask import Response
from flask_restful import Resource, reqparse


class Calc(Resource):
    def get(self, num1, operador, num2):
        try:
            num1 = float(num1.replace(',', '.'))
            num2 = float(num2.replace(',', '.'))
            res = calc(num1, num2, operador)
            if res is not None:
                return res, 200
            return Response(response="Operador inválido", mimetype="text/plain", status=400)
        except ValueError:
            return Response(response="Números inválidos", mimetype="text/plain", status=400)


def calc(in0: float, in1: float, in2: str):
    if in2 == 'soma':
        return in0 + in1
    if in2 == 'subtracao':
        return in0 - in1
    if in2 == 'multiplicacao':
        return in0 * in1
    if in2 == 'divisao':
        return in0 / in1
    if in2 == 'resto':
        return in0 % in1
    if in2 == 'potenciacao':
        return in0 ** in1
    return None
