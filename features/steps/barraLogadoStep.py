import time
from behave import given, then, when
from pages.barraDeNavegacaoPage import BarraDeNavegacaoPage


@given(u'que eu estou na pagina Login')
def step_impl(context):
    context.barraDeNavegacao = BarraDeNavegacaoPage(context.browser)
    context.barraDeNavegacao.paginaLogin()


@given(u'que efetue o login')
def step_impl(context):
    context.barraDeNavegacao.efetuarLogin()


@then(u'valido o direcionamento para a pagina minha conta')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMinhaConta()

@when(u'clico no submenu minha conta toggler')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMinhaContaToggler()


@then(u'verifico o submenu toggler')
def step_impl(context):
    context.barraDeNavegacao.validarSubmenuToggler()

@when(u'clico no submenu minha conta')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMinhaConta()


@when(u'clico no submenu meus titulos')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMeusTitulos()

@then(u'valido o direcionamento para a pagina meus titulos')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMeusTitulos()


@when(u'clico no submenu minhas premiacaoes')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMinhasPremiacaoes()

@then(u'valido o direcionamento para a pagina minhas premiacaoes')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMinhasPremiacoes()


@when(u'clico no submenu meus dados')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMeusDados()

@then(u'valido o direcionamento para a pagina meus dados')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMeusDados()


@when(u'clico no submenu sair')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuSair()

@then(u'valido o direcionamento para pagina home')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaHome()
