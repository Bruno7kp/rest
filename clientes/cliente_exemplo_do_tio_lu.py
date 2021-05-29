import requests


base_url = "http://localhost:5000/user/%s"
while True:
    operacao = input("Escolha uma operação (GET, POST, PUT, DELETE): ")
    if operacao.upper() == "GET":
        print(">>> GET <<<")
        nome = input("Nome: ")
        response = requests.get(base_url % nome)
        data = response.json()
        print(data)
        print("HTTP Code: %s" % response.status_code)
    elif operacao.upper() == "POST":
        print(">>> POST <<<")
        nome = input("Nome: ")
        idade = input("Idade: ")
        ocupacao = input("Ocupação: ")
        payload = {"idade": idade, "ocupacao": ocupacao}
        response = requests.post(base_url % nome, payload)
        data = response.json()
        print(data)
        print("HTTP Code: %s" % response.status_code)
    elif operacao.upper() == "PUT":
        print(">>> PUT <<<")
        nome = input("Nome: ")
        idade = input("Idade: ")
        ocupacao = input("Ocupação: ")
        payload = {"idade": idade, "ocupacao": ocupacao}
        response = requests.put(base_url % nome, payload)
        data = response.json()
        print(data)
        print("HTTP Code: %s" % response.status_code)
    elif operacao.upper() == "DELETE":
        print(">>> DELETE <<<")
        nome = input("Nome: ")
        response = requests.delete(base_url % nome)
        data = response.json()
        print(data)
        print("HTTP Code: %s" % response.status_code)
    else:
        break

