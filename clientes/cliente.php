<?php
$base_url = "http://localhost:5000/user/";

while (true):
    $operacao = readline("Escolha uma operação (GET, POST, PUT, DELETE): ");
    if (strtoupper($operacao) == "GET"):
        echo ">>> GET <<<";
        echo PHP_EOL;
        $nome = readline("Nome: ");

        $curl = curl_init();
        curl_setopt_array($curl, [
            CURLOPT_RETURNTRANSFER => 1,
            CURLOPT_URL => $base_url.$nome
        ]);
        $response = curl_exec($curl);
        curl_close($curl);

        echo $response;
        echo PHP_EOL;
    elseif (strtoupper($operacao) == "POST"):
        echo ">>> POST <<<";
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

        echo $body;
        echo PHP_EOL;
        echo "HTTP Code: " . $httpcode;
        echo PHP_EOL;
    elseif (strtoupper($operacao) == "PUT"):
        echo ">>> PUT <<<";
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

        echo $body;
        echo PHP_EOL;
        echo "HTTP Code: " . $httpcode;
        echo PHP_EOL;

    elseif (strtoupper($operacao) == "DELETE"):
        echo ">>> DELETE <<<";
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

        echo $body;
        echo PHP_EOL;
        echo "HTTP Code: " . $httpcode;
        echo PHP_EOL;
    else:
        break;
    endif;
endwhile;
