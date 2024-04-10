from behave import given, then, when
from utils.utils import Utils as info
from pages.minhaContaPage import MinhaContaPage
from pages.meusTitulosPage import MeusTitulosPage

@given(u'clique em acessar meus titulos')
def step_impl(context):
    context.minhaConta = MinhaContaPage(context.browser)
    context.minhaConta.acessarMeusTitulos()


@given(u'verifique que o usuario tenha titulos da campanha atual')
def step_impl(context):
    context.meusTitulos = MeusTitulosPage(context.browser)
    context.meusTitulos.verificarNomeCampanha()


@when(u'ao clicar no botao ver titulos')
def step_impl(context):
    context.meusTitulos.clicarEmVerTitulos()


@when(u'ao clicar no botao abrir titulo')
def step_impl(context):
    raise NotImplementedError(u'STEP: When ao clicar no botao abrir titulo')


@when(u'verifique o breadcrumb e o mesmo titulo selecionado')
def step_impl(context):
    raise NotImplementedError(u'STEP: When verifique o breadcrumb e o mesmo titulo selecionado')


@when(u'verifique o nome da campanha no header do titulo')
def step_impl(context):
    raise NotImplementedError(u'STEP: When verifique o nome da campanha no header do titulo')


@when(u'verifique se o documento Condições gerais é exibido')
def step_impl(context):
    raise NotImplementedError(u'STEP: When verifique se o documento Condições gerais é exibido')


@when(u'ao clicar no botao raspar automaticamente')
def step_impl(context):
    raise NotImplementedError(u'STEP: When ao clicar no botao raspar automaticamente')


@when(u'verifique que o botao foi desabilitado')
def step_impl(context):
    raise NotImplementedError(u'STEP: When verifique que o botao foi desabilitado')


@when(u'ao clicar no botão Numeros da sorte')
def step_impl(context):
    raise NotImplementedError(u'STEP: When ao clicar no botão Numeros da sorte')


@then(u'verifique que é exibido os numeros das rodadas')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verifique que é exibido os numeros das rodadas')


@then(u'ao clicar no conferir sorteio')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then ao clicar no conferir sorteio')


@then(u'verifique que o redirecionamento para seção de sorteios')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verifique que o redirecionamento para seção de sorteios')


@then(u'verifique que é exibido os numeros dos sorteios')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verifique que é exibido os numeros dos sorteios')
