package main

import (
    "bufio"
    "bytes"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "net/url"
    "os"
    "strings"
)


func main() {
    fmt.Println("::: Cliente Go :::")
    reader := bufio.NewReader(os.Stdin)
    for {
        fmt.Println("CRUD :: Gerenciador de usuários || CPF :: Validador de CPF || CALC :: Cálculo entre dois números || Q :: Sair")
        fmt.Print("Escolha uma das ações acima: ")
        action, _ := reader.ReadString('\n')
        action = strings.Replace(action, "\r\n", "", -1)
        action = strings.Replace(action, "\n", "", -1)
        action = strings.ToUpper(action)
        fmt.Println(action)
        if "CRUD" == action {
            fmt.Println("::: Gerenciador de usuários :::")
            for {
                fmt.Println("GET :: Buscar || POST :: Cadastrar || PUT :: Atualizar || DELETE :: Remover || Q :: Sair do CRUD")
                fmt.Print("Digite uma das operações acima: ")
                operacao, _ := reader.ReadString('\n')
                operacao = strings.Replace(operacao, "\r\n", "", -1)
                operacao = strings.Replace(operacao, "\n", "", -1)
                operacao = strings.ToUpper(operacao)
                if operacao == "GET" {
                    fmt.Println("::: GET :::")
                    fmt.Print("Nome: ")
                    nome, _ := reader.ReadString('\n')
                    nome = strings.Replace(nome, "\r\n", "", -1)
                    nome = strings.Replace(nome, "\n", "", -1)

                    response, err := http.Get("http://localhost:5000/user/" + nome)
                    if err != nil {
                        fmt.Print(err.Error())
                        os.Exit(1)
                    }

                    responseData, err := ioutil.ReadAll(response.Body)
                    if err != nil {
                        log.Fatal(err)
                    }
                    fmt.Print("Resultado: ")
                    fmt.Println(string(responseData))
                    fmt.Print("Código HTTP: ")
                    fmt.Println(response.StatusCode)
                } else if operacao == "POST" {
                    fmt.Println("::: POST :::")
                    fmt.Print("Nome: ")
                    nome, _ := reader.ReadString('\n')
                    nome = strings.Replace(nome, "\r\n", "", -1)
                    nome = strings.Replace(nome, "\n", "", -1)
                    fmt.Print("Idade: ")
                    idade, _ := reader.ReadString('\n')
                    idade = strings.Replace(idade, "\r\n", "", -1)
                    idade = strings.Replace(idade, "\n", "", -1)
                    fmt.Print("Ocupação: ")
                    ocupacao, _ := reader.ReadString('\n')
                    ocupacao = strings.Replace(ocupacao, "\r\n", "", -1)
                    ocupacao = strings.Replace(ocupacao, "\n", "", -1)

                    response, err := http.PostForm("http://localhost:5000/user/" + nome, url.Values{
                        "idade": {idade},
                        "ocupacao": {ocupacao}})
                    if err != nil {
                        fmt.Print(err.Error())
                        os.Exit(1)
                    }

                    responseData, err := ioutil.ReadAll(response.Body)
                    if err != nil {
                        log.Fatal(err)
                    }
                    fmt.Print("Resultado: ")
                    fmt.Println(string(responseData))
                    fmt.Print("Código HTTP: ")
                    fmt.Println(response.StatusCode)
                } else if operacao == "PUT" {
                    fmt.Println("::: PUT :::")
                    fmt.Print("Nome: ")
                    nome, _ := reader.ReadString('\n')
                    nome = strings.Replace(nome, "\r\n", "", -1)
                    nome = strings.Replace(nome, "\n", "", -1)
                    fmt.Print("Idade: ")
                    idade, _ := reader.ReadString('\n')
                    idade = strings.Replace(idade, "\r\n", "", -1)
                    idade = strings.Replace(idade, "\n", "", -1)
                    fmt.Print("Ocupação: ")
                    ocupacao, _ := reader.ReadString('\n')
                    ocupacao = strings.Replace(ocupacao, "\r\n", "", -1)
                    ocupacao = strings.Replace(ocupacao, "\n", "", -1)

                    client := &http.Client{}
                    data := url.Values{
                        "idade": {idade},
                        "ocupacao": {ocupacao}}
                    b := bytes.NewBufferString(data.Encode())
                    req, err := http.NewRequest("PUT","http://localhost:5000/user/" + nome, b)
                    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
                    response, err := client.Do(req)
                    if err != nil {
                        fmt.Print(err.Error())
                        os.Exit(1)
                    }
                    responseData, err := ioutil.ReadAll(response.Body)
                    if err != nil {
                        log.Fatal(err)
                    }
                    fmt.Print("Resultado: ")
                    fmt.Println(string(responseData))
                    fmt.Print("Código HTTP: ")
                    fmt.Println(response.StatusCode)
                } else if operacao == "DELETE" {
                    fmt.Println("::: DELETE :::")
                    fmt.Print("Nome: ")
                    nome, _ := reader.ReadString('\n')
                    nome = strings.Replace(nome, "\r\n", "", -1)
                    nome = strings.Replace(nome, "\n", "", -1)
                    client := &http.Client{}
                    data := url.Values{}
                    b := bytes.NewBufferString(data.Encode())
                    req, err := http.NewRequest("DELETE","http://localhost:5000/user/" + nome, b)
                    response, err := client.Do(req)
                    if err != nil {
                        fmt.Print(err.Error())
                        os.Exit(1)
                    }
                    responseData, err := ioutil.ReadAll(response.Body)
                    if err != nil {
                        log.Fatal(err)
                    }
                    fmt.Print("Resultado: ")
                    fmt.Println(string(responseData))
                    fmt.Print("Código HTTP: ")
                    fmt.Println(response.StatusCode)
                } else if operacao == "Q" {
                    break
                }
            }
        } else if "CPF" == action {
            fmt.Println("::: Validador de CPF :::")
            fmt.Print("Digite o CPF: ")
            cpf, _ := reader.ReadString('\n')
            cpf = strings.Replace(cpf, "\r\n", "", -1)
            cpf = strings.Replace(cpf, "\n", "", -1)

            response, err := http.Get("http://localhost:5000/cpf/" + cpf)
            if err != nil {
                fmt.Print(err.Error())
                os.Exit(1)
            }

            responseData, err := ioutil.ReadAll(response.Body)
            if err != nil {
                log.Fatal(err)
            }
            fmt.Print("Resultado: ")
            fmt.Println(string(responseData))
            fmt.Print("Código HTTP: ")
            fmt.Println(response.StatusCode)
        } else if "CALC" == action {
            fmt.Println("::: Cálculo entre dois números :::")
            fmt.Print("Primeiro número: ")
            num1, _ := reader.ReadString('\n')
            num1 = strings.Replace(num1, "\r\n", "", -1)
            num1 = strings.Replace(num1, "\n", "", -1)
            fmt.Print("Segundo número: ")
            num2, _ := reader.ReadString('\n')
            num2 = strings.Replace(num2, "\r\n", "", -1)
            num2 = strings.Replace(num2, "\n", "", -1)
            fmt.Println("Escolha um dos operadores abaixo\n(+) Soma || (-) Subtração || (*) Multiplicação || (/) Divisão || (%) Resto da divisão || (**) Potenciação")
            fmt.Print("Digite o operador: ")
            operador, _ := reader.ReadString('\n')
            operador = strings.Replace(operador, "\r\n", "", -1)
            operador = strings.Replace(operador, "\n", "", -1)

            switch operador {
                case "+":
                    operador = "soma"
                break
                case "-":
                    operador = "subtracao"
                break
                case "*":
                    operador = "multiplicacao"
                break
                case "/":
                    operador = "divisao"
                break
                case "%":
                    operador = "resto"
                break
                case "**":
                    operador = "potenciacao"
                break
            }

            response, err := http.Get("http://localhost:5000/calc/" + num1 + "/" + operador + "/" + num2)
            if err != nil {
                fmt.Print(err.Error())
                os.Exit(1)
            }

            responseData, err := ioutil.ReadAll(response.Body)
            if err != nil {
                log.Fatal(err)
            }
            fmt.Print("Resultado: ")
            fmt.Println(strings.Replace(string(responseData), "\n", "", -1))
            fmt.Print("Código HTTP: ")
            fmt.Println(response.StatusCode)
        } else if "Q" == action {
            fmt.Print("::: ADEUS :( :::")
            break
        }
    }
}