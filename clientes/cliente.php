<?php
# URLs usadas para fazer as requisições ao servidor
$base_url = "http://localhost:5000/user/";
$base_url_calc = "http://localhost:5000/calc/";
$base_url_cpf = "http://localhost:5000/cpf/";

# Método utilizado para adicionar cores no terminal, precisa enviar o texto a ser colorido, e o código para definir a cor
function colorLog($str, $code = null){
    $str = trim($str, "\n");
    switch ($code) {
        case 400:
        case 404:
        case "error":
            return "\033[31m$str \033[0m";
        break;
        case 200:
        case 201:
        case "success":
            return "\033[32m$str \033[0m";
        break;
        case "info":
            return "\033[34m$str \033[0m";
        break;
        default: //warning
            return "\033[33m$str \033[0m";
        break;
    }
}

# Inicio do cliente mostrando a mensagem no terminal
echo colorLog("::: Cliente PHP :::");
# PHP_EOL é usado para pular a linha no terminal
echo PHP_EOL;

# Inicia o loop que vai perguntar o serviço que o usuário quer utilizar
while (true):
    # O echo mostra o texto com os possíveis serviços e o que deve ser digitado para acessar
    echo colorLog("CRUD").":: Gerenciador de usuários || ".
        colorLog("CPF").":: Validador de CPF || ".
        colorLog("CALC").":: Cálculo entre dois números || ".
        colorLog("Q").":: Sair".PHP_EOL;
    # Aguarda o usuário digitar no terminal
    $servico = readline("Escolha uma das ações acima: ");

    if (strtoupper($servico) == "CRUD"):
        # Inicia o gerenciador de usuários
        echo colorLog("::: Gerenciador de usuários :::", "info");
        echo PHP_EOL;
        # Também usa um loop para perguntar a ação dentro do gerenciador
        while(true):
            # O echo mostra o texto com as possíveis ações e o que deve ser digitado para realizá-las
            echo colorLog("GET", "info").":: Buscar || ".
                colorLog("POST", "info").":: Cadastrar || ".
                colorLog("PUT", "info").":: Atualizar || ".
                colorLog("DELETE", "info").":: Remover || ".
                colorLog("Q", "info").":: Sair do CRUD".PHP_EOL;
            # Aguarda o usuário digitar no terminal
            $operacao = readline("Digite uma das operações acima: ");

            if (strtoupper($operacao) == "GET"):
                # Se escolheu a busca...
                echo colorLog("::: GET :::", "info");
                echo PHP_EOL;
                # ... pede pelo nome a ser buscado
                $nome = readline("Nome: ");

                # Utiliza o cURL para montar a requisição ao servidor
                $curl = curl_init();
                curl_setopt_array($curl, [
                    CURLOPT_RETURNTRANSFER => 1, # Indica que deve ter um retorno do servidor
                    CURLOPT_HEADER => true, # Indica que deve retornar o header (com o status HTTP por exemplo)
                    CURLOPT_URL => $base_url.$nome # A url que vai ser acessada /user/nome
                ]);
                # Executa a requisição
                $response = curl_exec($curl);
                # Pega o tamanho do header
                $header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
                # Remove o header, deixando apenas o body (a resposta em texto ou json do servidor)
                $body = substr($response, $header_size);
                # Pega o status HTTP da requisição
                $httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
                # Fecha a conexão
                curl_close($curl);

                # Mostra o resultado, utilizando o colorLog, para mostrar cores diferentes se for sucesso ou erro
                echo "Resultado: " . colorLog($body, $httpcode);
                echo PHP_EOL;
                echo "Código HTTP: " . colorLog($httpcode, $httpcode);
                echo PHP_EOL;
            elseif (strtoupper($operacao) == "POST"):
                echo colorLog("::: POST :::", "info");
                echo PHP_EOL;
                $nome = readline("Nome: ");
                $idade = readline("Idade: ");
                $ocupacao = readline("Ocupação: ");
                $payload = ["idade" => $idade, "ocupacao" => $ocupacao];

                $curl = curl_init();
                curl_setopt_array($curl, [
                    CURLOPT_RETURNTRANSFER => 1,
                    CURLOPT_HEADER => true,
                    CURLOPT_URL => $base_url.$nome,
                    CURLOPT_POST => 1,
                    CURLOPT_POSTFIELDS => $payload
                ]);
                $response = curl_exec($curl);
                $header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
                $body = substr($response, $header_size);
                $httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
                curl_close($curl);

                echo "Resultado: " . colorLog($body, $httpcode);
                echo PHP_EOL;
                echo "Código HTTP: " . colorLog($httpcode, $httpcode);
                echo PHP_EOL;
            elseif (strtoupper($operacao) == "PUT"):
                echo colorLog("::: PUT :::", "info");
                echo PHP_EOL;
                $nome = readline("Nome: ");
                $idade = readline("Idade: ");
                $ocupacao = readline("Ocupação: ");
                $payload = ["idade" => $idade, "ocupacao" => $ocupacao];

                $curl = curl_init();
                curl_setopt_array($curl, [
                    CURLOPT_RETURNTRANSFER => 1,
                    CURLOPT_HEADER => true,
                    CURLOPT_URL => $base_url.$nome,
                    CURLOPT_CUSTOMREQUEST => 'PUT',
                    CURLOPT_POSTFIELDS => $payload
                ]);
                $response = curl_exec($curl);
                $header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
                $body = substr($response, $header_size);
                $httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
                curl_close($curl);

                echo "Resultado: " . colorLog($body, $httpcode);
                echo PHP_EOL;
                echo "Código HTTP: " . colorLog($httpcode, $httpcode);
                echo PHP_EOL;

            elseif (strtoupper($operacao) == "DELETE"):
                echo colorLog("::: DELETE :::", "info");
                echo PHP_EOL;
                $nome = readline("Nome: ");

                $curl = curl_init();
                curl_setopt_array($curl, [
                    CURLOPT_RETURNTRANSFER => 1,
                    CURLOPT_HEADER => true,
                    CURLOPT_URL => $base_url.$nome,
                    CURLOPT_CUSTOMREQUEST => 'DELETE'
                ]);
                $response = curl_exec($curl);
                $header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
                $body = substr($response, $header_size);
                $httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
                curl_close($curl);

                echo "Resultado: " . colorLog($body, $httpcode);
                echo PHP_EOL;
                echo "Código HTTP: " . colorLog($httpcode, $httpcode);
                echo PHP_EOL;
            elseif(strtoupper($operacao) == "Q"):
                break;
            endif;
        endwhile;
    elseif (strtoupper($servico) == "CPF"):
        echo colorLog("::: Validador de CPF :::");
        echo PHP_EOL;
        $cpf = readline("Digite o CPF: ");

        $curl = curl_init();
        curl_setopt_array($curl, [
            CURLOPT_RETURNTRANSFER => 1,
            CURLOPT_HEADER => true,
            CURLOPT_URL => $base_url_cpf.$cpf,
        ]);
        $response = curl_exec($curl);
        $header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
        $body = substr($response, $header_size);
        $httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
        curl_close($curl);

        echo "Resultado: " . colorLog($body, $httpcode);
        echo PHP_EOL;
        echo "Código HTTP: " . colorLog($httpcode, $httpcode);
        echo PHP_EOL;

    elseif (strtoupper($servico) == "CALC"):
        echo colorLog("::: Cálculo entre dois números :::");
        echo PHP_EOL;
        $num1 = readline("Primeiro número: ");
        $num2 = readline("Segundo número: ");

        echo "Escolha um dos operadores abaixo".PHP_EOL.
            "(+) Soma || ".
            "(-) Subtração || ".
            "(*) Multiplicação || ".
            "(/) Divisão || ".
            "(%) Resto da divisão || ".
            "(**) Potenciação".PHP_EOL;
        $operador = readline("Digite o operador: ");

        switch ($operador):
            case "+":
                $operador = "soma";
                break;
            case "-":
                $operador = "subtracao";
                break;
            case "*":
                $operador = "multiplicacao";
                break;
            case "/":
                $operador = "divisao";
                break;
            case "%":
                $operador = "resto";
                break;
            case "**":
                $operador = "potenciacao";
                break;
        endswitch;

        $curl = curl_init();
        curl_setopt_array($curl, [
            CURLOPT_RETURNTRANSFER => 1,
            CURLOPT_HEADER => true,
            CURLOPT_URL => $base_url_calc.$num1."/".$operador."/".$num2,
        ]);
        $response = curl_exec($curl);
        $header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
        $body = substr($response, $header_size);
        $httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
        curl_close($curl);

        echo "Resultado: " . colorLog($body, $httpcode);
        echo PHP_EOL;
        echo "Código HTTP: " . colorLog($httpcode, $httpcode);
        echo PHP_EOL;
    elseif(strtoupper($servico) == "Q"):
        echo colorLog("::: ADEUS :( :::", "error");
        break;
    endif;
endwhile;
