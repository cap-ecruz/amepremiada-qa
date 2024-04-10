import time
from behave import given, then, when
from pages.loginPage import LoginPage
from pages.esqueciMinhaSenhaPage import EsqueciMinhaSenhaPage 
from pages.ativacaoSenhaPage import AtivacaoSenhaPage
from utils.utils import Utils as info
from pages.cadastroPage import CadastroPage


@when(u'clicar no botao esqueci minha senha')
def step_impl(context):
    context.login = LoginPage(context.browser)
    context.login.clicarNoBotaoEsqueciMinhaSenha()

@when(u'verificar o redirecionamento para a pagina esqueci minha senha')
def step_impl(context):
    context.esqueciMinhaSenha = EsqueciMinhaSenhaPage(context.browser)

@when(u'inserir um CPF valido')
def step_impl(context):
    context.esqueciMinhaSenha.inserirCPFEsqueciMinhaSenha('52510942050')

@when(u'clicar no botao enviar codigo')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoBotaoEnviarCodigo()
    time.sleep(1)

@when(u'clicar no botão ok da mensagem')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoBotaoOk()

@when(u'verifique o direcionamento para pagina de ativacao')
def step_impl(context):
    context.ativacaoSenha = AtivacaoSenhaPage(context.browser)

@when(u'inserir codigo de ativacao')
def step_impl(context):
    context.ativacaoSenha.inserirCodigoDeAtivacao(1234)

@then(u'clicar no botao confirmar codigo')
def step_impl(context):
    context.ativacaoSenha.clicarNoBotaoConfirmarCodigo()

@when(u'verifique o modal com o texto O seu cadastro foi completado com sucesso!')
def step_impl(context):
    CadastroPage(context.browser).validaModalSucesso()