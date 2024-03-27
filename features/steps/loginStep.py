from behave import given, then, when
from pages.loginPage import LoginPage
from utils.utils import Utils as info


@given(u'que estou na pagina login')
def step_impl(context):
    context.login = LoginPage(context.browser)
    context.login.paginaLogin()
    try:
        context.login.clicarNoBotaoEntendiPoliticaDeCookies()
    except:
        ...


@when(u'ao inseir o cpf')
def step_impl(context):
    context.login.inserirCPFLogin(info.CPF_CADASTRADO)


@when(u'ao inserir a senha')
def step_impl(context):
    context.login.inserirSenhaLogin(info.SENHA_CADASTRADO)


@when(u'ao clicar no botao fazer login')
def step_impl(context):
    context.login.clicarNoBotaoFazerLogin()


@then(u'verifique o direcionamento para pagina minha conta')
def step_impl(context):
    context.login.verificarSeEstaNaMinhaConta()
