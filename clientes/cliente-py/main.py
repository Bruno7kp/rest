# Classes do framework Flask
from flask import Flask, Response, render_template, request
import requests

# Inicia uma nova aplicação Flask
app = Flask(__name__)


# Adiciona rota para a página inicial
@app.route("/")
def index():
    return render_template('index.html')


# Rota para a página do validador de CPF, aceita GET e POST
@app.route("/cpf", methods=['GET', 'POST'])
def cpf():
    status = None
    value = None
    # Se o método for POST, significa que o formulário da página foi enviado pelo usuário
    if request.method == 'POST':
        # Faz a requisição para validar o CPF no servidor
        base_url = "http://localhost:5000/cpf/%s"
        value = request.form['cpf']
        response = requests.get(base_url % value)
        status = response.status_code
    # Retorna a página HTML com o status e o CPF digitado pelo usuário (se foi enviado o formulário)
    return render_template('cpf.html', status=status, cpf=value)


# Rota para a página do cálculo, aceita GET e POST
@app.route("/calculo", methods=['GET', 'POST'])
def calc():
    status = None
    value = None
    # Se o método for POST, significa que o formulário da página foi enviado pelo usuário
    if request.method == 'POST':
        # Pega os valores do formulário
        base_url = "http://localhost:5000/calc/"
        value1 = request.form['num1']
        value2 = request.form['num2']
        operator = request.form['operador']
        # Faz a requisição para o servidor
        response = requests.get(base_url + value1 + "/" + operator + "/" + value2)
        status = response.status_code
        value = response.text
        # Se retornou sucesso...
        if status == 200:
            # Formata o valor para adicionar os números e a operação selecionada pelo usuário
            replaceable = {'soma': '+', 'subtracao': '-', 'multiplicacao': '*', 'divisao': '/', 'resto': '%', 'potenciacao': '**'}
            # Assim mostra a conta completa ao invés de apenas o resultado (ex: 1 + 1 = 2)
            value = value1 + " " + replaceable[operator] + " " + value2 + " = " + response.text
    return render_template('calc.html', status=status, result=value)


# Roda o cliente na porta 5001 para não gerar conflito com o servidor que está na porta 5000
if __name__ == '__main__':
    app.run(debug=True, port=5001)


