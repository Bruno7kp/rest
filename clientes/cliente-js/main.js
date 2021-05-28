// Importa bibliotecas
const http = require("http");
const fs = require('fs').promises;

// Usa a porta 5002 já que 5001 é usada para o cliente python e 5000 para o servidor
const host = 'localhost';
const port = 5002;

// Método retornará o index.html e o app.js para o cliente
const requestListener = function (req, res) {
    switch (req.url) {
        case '/app.js':
            fs.readFile(__dirname + "/app.js")
                .then(contents => {
                    res.setHeader("Content-Type", "application/javascript; charset=utf-8");
                    res.writeHead(200);
                    res.end(contents);
                })
                .catch(err => {
                    res.writeHead(500);
                    res.end(err);
                    return;
                });
            break
        default:
            fs.readFile(__dirname + "/index.html")
                .then(contents => {
                    res.setHeader("Content-Type", "text/html; charset=utf-8");
                    res.writeHead(200);
                    res.end(contents);
                })
                .catch(err => {
                    res.writeHead(500);
                    res.end(err);
                    return;
                });
            break

    }

};

// Inicia o servidor
const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});