import json
from flask import Response
from flask_restful import Resource, reqparse


class Calc(Resource):
    def get(self, num1, operador, num2):
        return calc(num1, num2, operador)


def calc(in0: int, in1: int, in2: str):
    if in2 == 'somar':
        return in0 + in1
    if in2 == 'subtrair':
        return in0 - in1
    if in2 == 'multiplicar':
        return in0 * in1
    if in2 == 'dividir':
        return in0 / in1
    if in2 == 'resto':
        return in0 % in1
    if in2 == 'poteciacao':
        return in0 ** in1
    return None
