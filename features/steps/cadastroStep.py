import time
from behave import given, then, when
from pages.cadastroPage import CadastroPage
from utils.utils import Utils as info


@given(u'que estou na pagina cadastro passo1')
def step_impl(context):
    context.cadastro = CadastroPage(context.browser)
    context.cadastro.paginaCadastroPasso1()
    try:
        context.cadastro.clicarNoBotaoEntendiPoliticaDeCookies()
        time.sleep(1)
    except:
        ...

@when(u'E preencho o campo nome com dados {nome}')
def step_impl(context, nome):
    time.sleep(20)
    context.cadastro.inserirNome(nome)


@when(u'preencho o campo cpf na pagina login com usuario novo')
def step_impl(context):
    context.cadastro.inserirCPF(info.CPF_CADASTRADO)


@when(u'preencho o campo data de nascimento com dados {dados}')
def step_impl(context, dados):
    context.cadastro.inserirData(dados)


@when(u'preencho o campo cep com {dado}')
def step_impl(context, dado):
    context.cadastro.inserirCEP(dado)
    time.sleep(1)


@when(u'preencho o campo numero com {dado}')
def step_impl(context, dado):
    context.cadastro.inserirNumeroEndereco(dado)


@when(u'preencho o campo complemento com {dado}')
def step_impl(context, dado):
    context.cadastro.inserirComplemento(dado)

    
@when(u'clico em não no botao Você é uma pessoa politicamente exposta?')
def step_impl(context):
    context.cadastro.clicarEmNaoPPE()


@when(u'verifico que o botao proximo passo esteja habilitado')
def step_impl(context):
    context.cadastro.verificarBotaoProximoPassoAtivo()


@when(u'clico no botao proximo passo')
def step_impl(context):
    context.cadastro.clicarNoBotaoProximoPasso()


@when(u'valido o direcionamento para pagina cadastro passo2')
def step_impl(context):
    context.cadastro.verificarSeEstaNaPaginaCastroPasso2()


@when(u'preencho o campo email valido')
def step_impl(context):
    context.cadastro.inserirEmail('lucas209910+' + info.CPF_CADASTRADO + '@gmail.com')


@when(u'preencho o campo confirme o seu email valido')
def step_impl(context):
    context.cadastro.inserirConfirmeEmail('lucas209910+' + info.CPF_CADASTRADO + '@gmail.com')


@when(u'preencho o DDD com dados {dado}')
def step_impl(context, dado):
    context.cadastro.inserirDDD(dado)


@when(u'preencho o telefone valido com dados {dado}')
def step_impl(context, dado):
    context.cadastro.inserirPrincipal(dado)


@when(u'preencho o campo senha com dados valido')
def step_impl(context):
    context.cadastro.inserirSenha(info.SENHA_CADASTRADO)


@when(u'preencho o campo confirme a sua senha com dados valido')
def step_impl(context):
    context.cadastro.inserirConfSenha(info.SENHA_CADASTRADO)


#@when(u'clico na opcao nao do campo autoriza o uso dos dados')
#def step_impl(context):
#    context.cadastro.clicarNoBotaoNaoAutorizoOUsoDosDados()


@when(u'clico na opcao autorizar receber as comunicações')
def step_impl(context):
    context.cadastro.clicarNoBotaoNaoAutorizoOUsoDosDados()


@when(u'valido o direcionamento para pagina cadastro passo3')
def step_impl(context):
    context.cadastro.verificarSeEstaNaPaginaCastroPasso3()

    
@when(u'clico no campo trocar e-mail e reenviar código')
def step_impl(context):
    context.cadastro.clicarNoLinkCadastrarUmNovoEmail()


@when(u'ao inserir um email novo')
def step_impl(context):
    context.cadastro.inserirUmNovoEmail(info.CPF_CADASTRADO + '@testuser.com')


@when(u'ao inserir o codigo de ativacao')
def step_impl(context):
    context.cadastro.inserirCodigoDeAtivacao(info.CPF_CADASTRADO)


@when(u'ao clicar no botao de confirmar cadastro')
def step_impl(context):
    context.cadastro.clicarNoBotaoDeConfirmarCadastro()


@then(u'verifique o modal com o texto {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemNoModal(msg)
