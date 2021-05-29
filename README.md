# REST

## Requisitos

- [x] CRUD de usuários
- [x] Validação de CPF
- [x] Operação matemática simples
- [x] 4 clientes em linguagens diferentes
- [x] 2 cliente com interface gráfica (em deles em Python)
- [x] 1 cliente em GO


## Instalação

1. Clone ou baixe o repositório.
2. Crie um ambiente virtual:

Usando o terminal na pasta raiz do projeto, execute o comando:

```
python -m venv venv
```

Ative o ambiente executando o seguinte comando:

```
venv/Scripts/activate
```

3. Instale os pacotes necessários para rodar a aplicação (como o Flask):

```
pip install -r requirements.txt
```

## Servidor

Para iniciar a servidor, execute:

```
python servidor.py
```

## Clientes

### Sem interface gráfica

**PHP**

Versão utilizada: 7.3

Dependências: Precisa estar com o cURL habilitado (já vem habilitado por padrão)

```
php clientes/cliente.php
```

---

**GO**

Versão utilizada: 1.16.4

```
go run clientes/cliente.go
```


### Com interface gráfica

**Python**

Versão utilizada: 3.9.5

Bibliotecas: Flask 2.0.1, Bootstrap 5

```
python clientes/cliente-py/main.py
```

---

**JavaScript / Node.js**

Versão utilizada: 14.15.0

Bibliotecas: Vue.js 2, Bootstrap 5

```
node clientes/cliente-js/main.js
```