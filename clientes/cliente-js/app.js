// Adiciona plugin de máscara para o preenchimento do CPF
Vue.use(VueTheMask)
// Componente da página inicial
const Index = {
    template: `
    <div class="container">
        <div class="row">
            <div class="col">
                <div class="card mt-5">
                    <div class="card-body">
                        <h5 class="card-title">Cliente JavaScript</h5>
                        <p class="card-text">
                            Utilizando <strong>Node.js 14.15.0</strong>.
                            No frontend, utilizando <strong>Bootstrap 5</strong> e <strong>Vue.js 2.6.12</strong>.
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="card mt-5">
                    <div class="card-body">
                        <h5 class="card-title">Gerenciador de usuários</h5>
                        <p class="card-text">Acesse o gerenciador para cadastrar, ver, editar e remover usuários!</p>
                        <router-link class="btn btn-primary" to="/gerenciador">Gerenciar usuários</router-link>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card mt-5">
                    <div class="card-body">
                        <h5 class="card-title">Validador de CPF</h5>
                        <p class="card-text">Acesse a página para validar algum CPF!</p>
                        <router-link class="btn btn-primary" to="/cpf">Validar CPF</router-link>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card mt-5">
                    <div class="card-body">
                        <h5 class="card-title">Cálculo</h5>
                        <p class="card-text">Faça um cálculo simples entre dois números escolhendo um dos operadores!</p>
                        <router-link class="btn btn-primary" to="/calculo">Calcular</router-link>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="card mt-5">
                    <div class="card-body">
                        <h5 class="card-title">Trabalho de Sistemas Distribuídos</h5>
                        <p class="card-text">Bruno Varela, Elias e Ricardo<br/>
                            Sistemas de Informação<br/>
                            UNIPLAC - 7º Semestre</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `
}

// Componente do validador de cpf
const Cpf = {
    data() {
        // Valores iniciais são vazios
        return {
            cpf: null,
            valido: null,
        }
    },
    // Sempre que trocar o valor do cpf, limpa o alerta de sucesso/erro
    watch: {
        cpf(v) {
            this.valido = null;
        },
    },
    methods: {
        send() {
            // Faz a requisição para validar o cpf
            fetch('http://localhost:5000/cpf/' + this.cpf)
            .then((response) => {
                this.valido = response.status == 200;
            });
        },
    },
    template: `
    <div class="container">
        <div class="row">
            <div class="col-sm-12 col-md-6">
                <div class="card mt-5">
                    <div class="card-body">
                        <h5 class="card-title">Validador de CPF</h5>
                        <p class="card-text">Digite o CPF abaixo para validá-lo!</p>
                        <form method="post">
                            <label>
                                Digite o CPF
                                <the-mask class="form-control" :mask="['###.###.###-##']" masked="true" name="cpf" v-model="cpf" required />
                            </label>
                            <button class="btn btn-success" type="button" @click="send">Validar</button>
                        </form>
                        <div class="alert alert-danger" role="alert" v-if="valido === false">
                          {{ cpf }} é um CPF inválido!
                        </div>
                        <div class="alert alert-success" role="alert" v-if="valido === true">
                          {{ cpf }} é um CPF válido!
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `
}

// Componente da calculadora
const Calc = {
    data() {
        return {
            num1: null,
            num2: null,
            operador: null,
            resultado: null,
            valido: null,
        }
    },
    methods: {
        send() {
            // Faz a requisição para o servidor
            fetch('http://localhost:5000/calc/' + this.num1 + '/' + this.operador + '/' + this.num2)
            .then((response) => {
                this.valido = response.status == 200;
                if (this.valido) {
                    response.text().then((txt) => {
                        // Formata o valor para mostrar os números e a operação selecionada pelo usuário
                        let replaceable = {'soma': '+', 'subtracao': '-', 'multiplicacao': '*', 'divisao': '/', 'resto': '%', 'potenciacao': '**'}
                        // Assim mostra a conta completa ao invés de apenas o resultado (ex: 1 + 1 = 2)
                        txt = this.num1 + " " + replaceable[this.operador] + " " + this.num2 + " = " + txt.replace('.', ',')
                        this.resultado = txt;
                    });
                } else {
                    response.text().then((txt) => {
                        // Mostra mensagem de erro
                        this.resultado = txt;
                    });
                }
            });
        },
    },
    template: `
    <div class="container">
        <div class="row">
            <div class="col">
                <div class="card mt-5">
                    <div class="card-body">
                        <h5 class="card-title">Cálculo</h5>
                        <p class="card-text">Digite dois número e selecione o operador para realizar a conta!</p>
                        <form method="post">
                            <label>
                                Digite o primeiro número
                                <input type="text" class="form-control" name="num1" v-model="num1" required>
                            </label>
                            <label>
                                Selecione o operador
                                <select name="operador" class="form-select" v-model="operador" required>
                                    <option :value="null" selected>Selecione o operador</option>
                                    <option value="soma">(+) Soma</option>
                                    <option value="subtracao">(-) Subtração</option>
                                    <option value="multiplicacao">(*) Multiplicação</option>
                                    <option value="divisao">(/) Divisão</option>
                                    <option value="resto">(%) Resto da divisão</option>
                                    <option value="potenciacao">(**) Potenciação</option>
                                </select>
                            </label>
                            <label>
                                Digite o segundo número
                                <input type="text" class="form-control" name="num2" v-model="num2" required>
                            </label>

                            <button type="button" @click="send" class="btn btn-success">Calcular</button>
                        </form>
                        <div class="alert alert-danger" role="alert" v-if="valido === false">
                          {{ resultado }}
                        </div>
                        <div class="alert alert-success" role="alert" v-if="valido === true">
                          Resultado: {{ resultado }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `
}

const UserList = {
    data() {
        return {
            adicionado: null,
            removido: null,
            usuarios: null,
        }
    },
    methods: {
        load() {
            fetch('http://localhost:5000/users').then((usuarios) => {
                usuarios.json().then((users) => {
                    this.usuarios = users;
                });
            });
        },
        remover(nome) {
            fetch('http://localhost:5000/user/' + nome, {method:'DELETE'}).then((response) => {
                response.text().then((txt) => {
                    this.removido = txt;
                    this.load();
                    setTimeout(() => {
                        this.removido = null;
                    }, 3000);
                });
            });
        }
    },
    created() {
        this.load();
    },
    template: `
    <div class="container">
        <div class="row">
            <div class="col">
                <div class="card mt-5">
                    <div class="card-body">
                        <div class="row">
                            <div class="col">
                                <h5 class="card-title float-start">Gerenciador de usuários</h5>
                                <router-link class="btn btn-success btn-sm float-end" to="/gerenciador/adicionar">Adicionar usuário</router-link>
                            </div>
                        </div>
                        <div class="card-text">
                            <div class="row" v-if="adicionado">
                                <div class="col">
                                    <div class="alert alert-success fade show" role="alert">
                                        {{ adicionado }}
                                    </div>
                                </div>
                            </div>
                            <div class="row" v-if="removido">
                                <div class="col">
                                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                                        {{ removido }}
                                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Fechar"></button>
                                    </div>
                                </div>
                            </div>
                            <div class="row" v-if="usuarios && usuarios.length === 0">
                                <div class="col">
                                    <div class="alert alert-danger" role="alert">
                                        Nenhum usuário cadastrado
                                    </div>
                                </div>
                            </div>
                            <table class="table table-bordered table-striped" v-if="usuarios && usuarios.length > 0">
                                <thead>
                                <tr>
                                    <th>Usuário</th>
                                    <th>Idade</th>
                                    <th>Ocupação</th>
                                    <th>Ações</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="user in usuarios">
                                    <td class="w-25">{{ user.nome }}</td>
                                    <td class="w-25">{{ user.idade }}</td>
                                    <td class="w-40">{{ user.ocupacao }}</td>
                                    <td class="w-auto">
                                        <router-link class="btn btn-primary btn-sm" :to="'/gerenciador/editar/' + user.nome">Editar</router-link>
                                        <button class="btn btn-danger btn-sm" @click="remover(user.nome)">Remover</button>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `
}

// Rotas do Vue.js
const routes = [
  { path: '/', component: Index },
  { path: '/cpf', component: Cpf },
  { path: '/calculo', component: Calc },
  { path: '/gerenciador', component: UserList },
]

const router = new VueRouter({
  routes,
  linkExactActiveClass: 'active',
})

// Inicia o Vue
const app = new Vue({
  router
}).$mount('#app')