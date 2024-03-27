import time
from behave import given, then, when
from pages.barraDeNavegacaoPage import BarraDeNavegacaoPage

#contexto
@given(u'que eu estou na pagina Login')
def step_impl(context):
    context.barraDeNavegacao = BarraDeNavegacaoPage(context.browser)
    context.barraDeNavegacao.paginaLogin()

@given(u'que efetue o login')
def step_impl(context):
    context.barraDeNavegacao.efetuarLogin()

#navegação submenu
@when(u'clico em abrir menu de usuario')
def step_impl(context):
    context.barraDeNavegacao.clicarAbrirMenuDeUsuario()

@when(u'clico no submenu minha conta toggler')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMinhaContaToggler()

@then(u'valido o direcionamento para a pagina minha conta')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMinhaConta()

@when(u'clico no submenu meus titulos toggler')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMeusTitulosToggler()

@then(u'valido o direcionamento para a pagina meus titulos')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaSubMenuMeusTitulos()

@when(u'clico no submenu minhas premiacoes toggler')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMinhasPremiacoesToggler()

@then(u'valido o direcionamento para a pagina minhas premiacoes')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMinhasPremiacoes()

@when(u'clico no submenu meus dados toggler')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuMeusDados()

@then(u'valido o direcionamento para a pagina meus dados')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMeusDados()

@when(u'clico no submenu sair toggler')
def step_impl(context):
    context.barraDeNavegacao.clicarSubMenuSair()

@then(u'valido o direcionamento para a pagina inicial')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaHome()

#dashboard
#@when(u'acesso a pagina minha conta')
#def step_impl(context):
#    context.barraDeNavegacao.verificarSeEstaNaPaginaMinhaConta()

@when(u'clico no dashboard meus titulos')
def step_impl(context):
    context.barraDeNavegacao.clicarDashboardMeusTitulos()

@then(u'valido o direcionamento para a pagina minhas titulos')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMeusTitulos()

@when(u'clico no dashboard premiacoes')
def step_impl(context):
    context.barraDeNavegacao.clicarDashboardPremiacoes()

@then(u'valido o direcionamento para a pagina premiacoes')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMinhasPremiacoes()

@when(u'clico no dashboard historico de premiacoes')
def step_impl(context):
    context.barraDeNavegacao.clicarDashboardHistoricoDePremiacoes()

@then(u'valido o direcionamento para a pagina historico de premiacoes')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaHistoricoDePremiacoes()

@when(u'clico no dashboard meus dados')
def step_impl(context):
    context.barraDeNavegacao.clicarDashboardMeusDados()

@then(u'valido o direcionamento para meus dados')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaMeusDados()