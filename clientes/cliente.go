package main
// Importa bibliotecas
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

// Método principal a ser executado quando rodar o arquivo
func main() {
    // Inicia a aplicação GO
    fmt.Println("::: Cliente Go :::")
    // reader é usado para ler as mensagens digitadas no cliente
    reader := bufio.NewReader(os.Stdin)
    // O for se condições gera um loop infinito, até parar com o break
    for {
        // Mostra as opções de serviços da aplicação
        fmt.Println("CRUD :: Gerenciador de usuários || CPF :: Validador de CPF || CALC :: Cálculo entre dois números || Q :: Sair")
        fmt.Print("Escolha uma das ações acima: ")
        // Pede para usuário digitar e captura mensagem até apertar 'enter' (que gera a nova linha '\n')
        action, _ := reader.ReadString('\n')
        // Utiliza o Replace para remover as quebras de linha, no windows também tem o \r, por isso é removido duas vezes...
        // ... uma para o windows e a segunda para linux
        action = strings.Replace(action, "\r\n", "", -1)
        action = strings.Replace(action, "\n", "", -1)
        // Transforma o texto digitado em caixa ALTA
        action = strings.ToUpper(action)
        if "CRUD" == action {
            // Entra no gerenciador de usuários
            fmt.Println("::: Gerenciador de usuários :::")
            // Inicia outro loop para o gerenciador de usuários
            for {
                // Mostra as opções do gerenciador
                fmt.Println("GET :: Buscar || POST :: Cadastrar || PUT :: Atualizar || DELETE :: Remover || Q :: Sair do CRUD")
                fmt.Print("Digite uma das operações acima: ")
                // Pede a operação ao usuário
                operacao, _ := reader.ReadString('\n')
                // Remove a quebra de linha do texto
                operacao = strings.Replace(operacao, "\r\n", "", -1)
                operacao = strings.Replace(operacao, "\n", "", -1)
                // Transforma em caixa ALTA
                operacao = strings.ToUpper(operacao)
                if operacao == "GET" {
                    // Se operação for de busca...
                    fmt.Println("::: GET :::")
                    // Pede o nome do usuário
                    fmt.Print("Nome: ")
                    nome, _ := reader.ReadString('\n')
                    // Remove quebras de linha do texto
                    nome = strings.Replace(nome, "\r\n", "", -1)
                    nome = strings.Replace(nome, "\n", "", -1)
                    // Faz a requisição GET para /user/nome
                    response, err := http.Get("http://localhost:5000/user/" + nome)
                    // Se gerar erro mostra o erro no prompt
                    if err != nil {
                        fmt.Print(err.Error())
                        os.Exit(1)
                    }
                    // Pega a resposta do servidor
                    responseData, err := ioutil.ReadAll(response.Body)
                    // Se gerar erro mostra no prompt
                    if err != nil {
                        log.Fatal(err)
                    }
                    // Se não tiver problemas, mostra o resultado e o status http
                    fmt.Print("Resultado: ")
                    fmt.Println(string(responseData))
                    fmt.Print("Código HTTP: ")
                    fmt.Println(response.StatusCode)
                } else if operacao == "POST" {
                    // Se operação for de cadastro...
                    fmt.Println("::: POST :::")
                    // Pede o nome do usuário
                    fmt.Print("Nome: ")
                    nome, _ := reader.ReadString('\n')
                    // Remove quebras de linha do texto
                    nome = strings.Replace(nome, "\r\n", "", -1)
                    nome = strings.Replace(nome, "\n", "", -1)
                    // Pede a idade do usuário
                    fmt.Print("Idade: ")
                    idade, _ := reader.ReadString('\n')
                    // Remove quebras de linha do texto
                    idade = strings.Replace(idade, "\r\n", "", -1)
                    idade = strings.Replace(idade, "\n", "", -1)
                    // Pede a idade do usuário
                    fmt.Print("Ocupação: ")
                    ocupacao, _ := reader.ReadString('\n')
                    // Remove quebras de linha do texto
                    ocupacao = strings.Replace(ocupacao, "\r\n", "", -1)
                    ocupacao = strings.Replace(ocupacao, "\n", "", -1)
                    // Faz a requisição via post para /user/nome
                    // utiliza o url.Values para criar um objeto que será convertido pelo Go como valores da requisição POST
                    response, err := http.PostForm("http://localhost:5000/user/" + nome, url.Values{
                        "idade": {idade},
                        "ocupacao": {ocupacao}})
                    // Se gerar erro na requisição mostra no prompt
                    if err != nil {
                        fmt.Print(err.Error())
                        os.Exit(1)
                    }
                    // Pega a resposta do servidor
                    responseData, err := ioutil.ReadAll(response.Body)
                    // Se gerar erro mostra no prompt
                    if err != nil {
                        log.Fatal(err)
                    }
                    // Se não tiver problemas, mostra o resultado e o status http
                    fmt.Print("Resultado: ")
                    fmt.Println(string(responseData))
                    fmt.Print("Código HTTP: ")
                    fmt.Println(response.StatusCode)
                } else if operacao == "PUT" {
                    // Se operação for de atualização...
                    fmt.Println("::: PUT :::")
                    // Pede o nome do usuário
                    fmt.Print("Nome: ")
                    nome, _ := reader.ReadString('\n')
                    // Remove quebras de linha do texto
                    nome = strings.Replace(nome, "\r\n", "", -1)
                    nome = strings.Replace(nome, "\n", "", -1)
                    // Pede a idade do usuário
                    fmt.Print("Idade: ")
                    idade, _ := reader.ReadString('\n')
                    // Remove quebras de linha do texto
                    idade = strings.Replace(idade, "\r\n", "", -1)
                    idade = strings.Replace(idade, "\n", "", -1)
                    // Pede a ocupação do usuário
                    fmt.Print("Ocupação: ")
                    ocupacao, _ := reader.ReadString('\n')
                    // Remove quebras de linha do texto
                    ocupacao = strings.Replace(ocupacao, "\r\n", "", -1)
                    ocupacao = strings.Replace(ocupacao, "\n", "", -1)
                    // Para utilizar o PUT, é preciso criar uma requisição diferente
                    // Cria-se o cliente primeiro;
                    client := &http.Client{}
                    // Crias-se os valores a serem enviados na requisição:
                    data := url.Values{
                        "idade": {idade},
                        "ocupacao": {ocupacao}}
                    // Transforma os dados para o formato de envio
                    b := bytes.NewBufferString(data.Encode())
                    // Inicia a requisição PUT para /user/nome com os dados convertidos
                    req, err := http.NewRequest("PUT","http://localhost:5000/user/" + nome, b)
                    // Precisa indicador que está sendo passado no formato de formulário
                    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
                    // O cliente executa a requisição
                    response, err := client.Do(req)
                    // Se gerar erro, mostra no prompt
                    if err != nil {
                        fmt.Print(err.Error())
                        os.Exit(1)
                    }
                    // Lê o corpo da resposta do servidor
                    responseData, err := ioutil.ReadAll(response.Body)
                    // Se gerar erro, mostra no prompt
                    if err != nil {
                        log.Fatal(err)
                    }
                    // Se não tiver problemas, mostra o resultado e o status http
                    fmt.Print("Resultado: ")
                    fmt.Println(string(responseData))
                    fmt.Print("Código HTTP: ")
                    fmt.Println(response.StatusCode)
                } else if operacao == "DELETE" {
                    // Se operação for de remoção...
                    fmt.Println("::: DELETE :::")
                    // Pede o nome do usuário
                    fmt.Print("Nome: ")
                    nome, _ := reader.ReadString('\n')
                    // Remove quebras de linha do texto
                    nome = strings.Replace(nome, "\r\n", "", -1)
                    nome = strings.Replace(nome, "\n", "", -1)
                    // Para utilizar o DELETE, é preciso criar uma requisição diferente
                    // Cria-se o cliente primeiro;
                    client := &http.Client{}
                    // Crias-se os valores a serem enviados na requisição, no caso do DELETE, é vazio mesmo
                    data := url.Values{}
                    b := bytes.NewBufferString(data.Encode())
                    // Inicia a requisição DELETE para /user/nome
                    req, err := http.NewRequest("DELETE","http://localhost:5000/user/" + nome, b)
                    // O cliente executa a requisição
                    response, err := client.Do(req)
                    // Se gerar erro, mostra no prompt
                    if err != nil {
                        fmt.Print(err.Error())
                        os.Exit(1)
                    }
                    // Lê o corpo da resposta do servidor
                    responseData, err := ioutil.ReadAll(response.Body)
                    // Se gerar erro, mostra no prompt
                    if err != nil {
                        log.Fatal(err)
                    }
                    // Se não tiver problemas, mostra o resultado e o status http
                    fmt.Print("Resultado: ")
                    fmt.Println(string(responseData))
                    fmt.Print("Código HTTP: ")
                    fmt.Println(response.StatusCode)
                } else if operacao == "Q" {
                    // Sai do gerenciamento de usuários e volta para a seleção de serviços
                    break
                }
            }
        } else if "CPF" == action {
            // Inicia o validador de CPF
            fmt.Println("::: Validador de CPF :::")
            // Pede o CPF, pode ser formatado ou não
            fmt.Print("Digite o CPF: ")
            cpf, _ := reader.ReadString('\n')
            // Remove quebras de linha do texto
            cpf = strings.Replace(cpf, "\r\n", "", -1)
            cpf = strings.Replace(cpf, "\n", "", -1)
            // Faz a requisição GET para /cpf/valor
            response, err := http.Get("http://localhost:5000/cpf/" + cpf)
            // Se gerar erro, mostra no prompt
            if err != nil {
                fmt.Print(err.Error())
                os.Exit(1)
            }
            // Lê o corpo da resposta do servidor
            responseData, err := ioutil.ReadAll(response.Body)
            // Se gerar erro, mostra no prompt
            if err != nil {
                log.Fatal(err)
            }
            // Se não tiver problemas, mostra o resultado e o status http
            fmt.Print("Resultado: ")
            fmt.Println(string(responseData))
            fmt.Print("Código HTTP: ")
            fmt.Println(response.StatusCode)
        } else if "CALC" == action {
            // Inicia o cálculo
            fmt.Println("::: Cálculo entre dois números :::")
            // Pede o primeiro número
            fmt.Print("Primeiro número: ")
            num1, _ := reader.ReadString('\n')
            // Remove quebras de linha do texto
            num1 = strings.Replace(num1, "\r\n", "", -1)
            num1 = strings.Replace(num1, "\n", "", -1)
            // Pede o segundo número
            fmt.Print("Segundo número: ")
            num2, _ := reader.ReadString('\n')
            // Remove quebras de linha do texto
            num2 = strings.Replace(num2, "\r\n", "", -1)
            num2 = strings.Replace(num2, "\n", "", -1)
            // Mostra as opções de operadores
            fmt.Println("Escolha um dos operadores abaixo\n(+) Soma || (-) Subtração || (*) Multiplicação || (/) Divisão || (%) Resto da divisão || (**) Potenciação")
            // Pede o operador
            fmt.Print("Digite o operador: ")
            operador, _ := reader.ReadString('\n')
            // Remove quebras de linha do texto
            operador = strings.Replace(operador, "\r\n", "", -1)
            operador = strings.Replace(operador, "\n", "", -1)
            // Transforma o sinal operador em texto conforme está no servidor
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
            // Faz a requisição GET para /calc/num1/operacao/num2
            response, err := http.Get("http://localhost:5000/calc/" + num1 + "/" + operador + "/" + num2)
            // Se gerar erro, mostra no prompt
            if err != nil {
                fmt.Print(err.Error())
                os.Exit(1)
            }
            // Lê o corpo da resposta do servidor
            responseData, err := ioutil.ReadAll(response.Body)
            // Se gerar erro, mostra no prompt
            if err != nil {
                log.Fatal(err)
            }
            // Se não tiver problemas, mostra o resultado e o status http
            fmt.Print("Resultado: ")
            fmt.Println(strings.Replace(string(responseData), "\n", "", -1))
            fmt.Print("Código HTTP: ")
            fmt.Println(response.StatusCode)
        } else if "Q" == action {
            // Mostra mensagem ao sair da aplicação
            fmt.Print("::: ADEUS :( :::")
            break
        }
    }
}