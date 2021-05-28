Vue.use(VueTheMask)

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
                            No frontend, utilizando <strong>Bootstrap 5</strong>.
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

const Cpf = {
    data() {
        return {
            cpf: null,
            valido: null,
        }
    },
    watch: {
        cpf(v) {
            this.valido = null;
        },
    },
    methods: {
        send() {
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


const routes = [
  { path: '/', component: Index },
  { path: '/cpf', component: Cpf }
]

//
const router = new VueRouter({
  routes // short for `routes: routes`
})

//
const app = new Vue({
  router
}).$mount('#app')