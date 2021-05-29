# Classes do framework Flask
from flask import Flask, Response, render_template, request, redirect
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
            # Formata o valor para mostrar os números e a operação selecionada pelo usuário
            replaceable = {'soma': '+', 'subtracao': '-', 'multiplicacao': '*', 'divisao': '/', 'resto': '%', 'potenciacao': '**'}
            # Assim mostra a conta completa ao invés de apenas o resultado (ex: 1 + 1 = 2)
            value = value1 + " " + replaceable[operator] + " " + value2 + " = " + response.text.replace('.', ',')
    return render_template('calc.html', status=status, result=value)


# Rota para a página inicial do gerenciador
@app.route("/gerenciador")
def gerenciador():
    # Na página inicial do gerenciador, faz a busca de todos os usuários
    base_url = "http://localhost:5000/users"
    # Faz a requisição para o servidor
    response = requests.get(base_url)
    status = response.status_code
    users = response.json()
    # Verifica se há parâmetro sen enviados pela query (ex: ?removido=200)
    # Esses parâmetros são usados para mostrar mensagem na tela, caso esteja sendo redirecionada de outra página
    removido = request.args.get('removido')
    removido_status = request.args.get('removido_status')
    adicionado = request.args.get('adicionado')
    if removido_status:
        removido_status = int(removido_status)
    return render_template('gerenciador.html', users=users, status=status, removido=removido,
                           removido_status=removido_status, adicionado=adicionado)


# Rota para remover o usuário, como não foi usado JS para as requisições, e não é possível fazer uma requisição...
# ... com o método DELETE e nem o método PUT, foi preciso criar uma url recebendo via GET para utilizar o REST
@app.route("/gerenciador/remover/<string:nome>")
def remover(nome):
    # Faz a requisição para remover
    base_url = "http://localhost:5000/user/" + nome
    response = requests.delete(base_url)
    # Redireciona para a lista de usuário com os dados de resposta
    return redirect("/gerenciador?removido=" + response.text + "&removido_status=" + str(response.status_code))


# Rota para adicionar usuário
@app.route("/gerenciador/adicionar", methods=['GET', 'POST'])
def adicionar():
    status = None
    message = None
    # Se o método for POST, significa que o formulário da página foi enviado pelo usuário
    if request.method == 'POST':
        # Pega os valores do formulário
        nome = request.form['nome']
        idade = request.form['idade']
        ocupacao = request.form['ocupacao']
        base_url = "http://localhost:5000/user/" + nome
        # Faz a requisição ao servidor
        payload = {"idade": idade, "ocupacao": ocupacao}
        response = requests.post(base_url, payload)
        status = response.status_code
        message = response.text
        if status == 201:
            # Se cadastrou, redireciona para a lista de usuário com mensagem de sucesso
            text = nome + ' adicionado(a).'
            return redirect("/gerenciador?adicionado=" + text)
    # Se o método for POST, passa o status de erro e a mensagem para mostrar na página de cadastro
    return render_template('adicionar.html', status=status, message=message)


# Rota para adicionar usuário
@app.route("/gerenciador/editar/<string:nome>", methods=['GET', 'POST'])
def editar(nome):
    base_url = "http://localhost:5000/user/" + nome
    status = None
    message = None
    response = requests.get(base_url)
    # Se o usuário não for encontrado, mostra erro 404
    if response.status_code == 404:
        return response.text, 404
    user = response.json()
    # Se o método for POST, significa que o formulário da página foi enviado pelo usuário
    if request.method == 'POST':
        # Pega os valores do formulário
        nome = request.form['nome']
        idade = request.form['idade']
        ocupacao = request.form['ocupacao']
        # Faz a requisição ao servidor
        base_url = "http://localhost:5000/user/" + nome
        payload = {"idade": idade, "ocupacao": ocupacao}
        response = requests.put(base_url, payload)
        status = response.status_code
        message = response.text
        if status == 201:
            # Se cadastrou, redireciona para a lista de usuário com mensagem de sucesso
            text = nome + ' adicionado(a).'
            return redirect("/gerenciador?adicionado=" + text)
        elif status == 200:
            user['idade'] = idade
            user['ocupacao'] = ocupacao
            message = nome + ' editado(a).'
    # Se o método for POST, passa o status de erro e a mensagem para mostrar na página de cadastro
    return render_template('editar.html', user=user, status=status, message=message)


# Roda o cliente na porta 5001 para não gerar conflito com o servidor que está na porta 5000
if __name__ == '__main__':
    app.run(debug=True, port=5001)


