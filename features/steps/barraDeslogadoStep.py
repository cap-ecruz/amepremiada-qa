import time
from behave import given, then, when
from pages.barraDeNavegacaoPage import BarraDeNavegacaoPage
from selenium import webdriver


@given(u'que estou na home')
def step_impl(context):
    context.barraDeNavegacao = BarraDeNavegacaoPage(context.browser)
    context.barraDeNavegacao.paginaHome()


@when(u'clico no menu logo')
def step_impl(context):
    context.barraDeNavegacao.clicarNaLogo()

@then(u'valido o direcionamento para a pagina home')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaHome()


@when(u'clico no menu resultados')
def step_impl(context):
    context.barraDeNavegacao.clicarNaResultados()

@then(u'valido o direcionamento para a pagina resultados')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaResultados()


@when(u'clico no menu instituicao')
def step_impl(context):
    context.barraDeNavegacao.clicarNoMenuInstituicaoBeneficiada()

@then(u'valido o direcionamento para a pagina instituicao')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaInstituicaoBeneficiada()


@when(u'clico no menu comprar titulo')
def step_impl(context):
    context.barraDeNavegacao.clicarNoMenuComprarTitulo()

@then(u'valido o direcionamento para a pagina comprar titulo')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaComoComprar()


@when(u'clico no menu user login')
def step_impl(context):
    context.barraDeNavegacao.clicarNoBotaoLogin()

@then(u'valido o direcionamento para a pagina login')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaLogin()

