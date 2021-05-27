from flask import Response
from flask_restful import Resource


# Classe que irá receber os dados a partir da URL /calc/numero1/operador/numero2
class Calc(Resource):
    def get(self, num1, operador, num2):
        # Tenta transformar o valor enviado para os números para o tipo float
        # Se ocorrer erro durante a transformação (ou seja, foi enviado um valor que não seja número), retorna como
        # "Números inválidos"
        try:
            num1 = float(num1.replace(',', '.'))
            num2 = float(num2.replace(',', '.'))
            res = calc(num1, num2, operador)
            # Se o resultado do cálculo for nulo (None), significa que foi enviado um operador inválido
            if res is not None:
                # Se o resultado não for nulo, devolve o valor da conta com o status 200 de sucesso
                return res, 200
            return Response(response="Operador inválido", mimetype="text/plain", status=400)
        except ValueError:
            return Response(response="Números inválidos", mimetype="text/plain", status=400)


# Método que faz a conta de dois números
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
