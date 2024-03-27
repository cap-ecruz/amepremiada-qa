import time
from behave import given, then, when
from pages.homePage import HomePage


@given(u'que eu estou na pagina home')
def step_impl(context):
    context.home = HomePage(context.browser)
    context.home.paginaHome()

@when(u'verifico se esta na página home')
def step_impl(context, msg):
    context.home.verificarSeEstaNaPaginaHome()

@then(u'valido o direcionamento para a pagina de login')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaLogin()

@then(u'verifico a exibicao da mensagem de cookie {msg}')
def step_impl(context, msg):
    context.home.verificarMensagemCookie(msg)


@when(u'ao clicar no link Politica de privacidade')
def step_impl(context):
    context.home.clicarNoLinkPoliticaDePrivacidade()

@then(u'verifica o direcionamento para pagina Politica de Privacidade')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaPoliticaDePrivacidade()


@when(u'ao clicar no botao comprar titulo')
def step_impl(context):
    context.home.clicarNoBotaoDoBannerPrincipalHome()

@then(u'valido o direcionamento para a pagina como comprar')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaComoComprar()



@when(u'ao clicar no botao conferir resultados')
def step_impl(context):
    context.home.clicarNoBotaoCliqueAquiEConfiraSeusResultados()

@then(u'valido o direcionamento para pagina resultados')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaResultados()


@when(u'ao clicar no botao veja instituicao')
def step_impl(context):
    context.home.clicarNoBotaoVejaMaisSobreAFundacao()

@then(u'valido o direcionamento para a pagina da instituicao')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaInstituicaoBeneficiada()


# ----- login home
@when(u'ao clicar no botao login')
def step_impl(context):
    context.home.clicarNoBotaoLogin()

@then(u'valido o direcionamento para pagina login')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaLogin()


# ----- faq home
@when(u'ao clicar no botao ver mais duvidas frequentes')
def step_impl(context):
    context.home.clicarNoLinkVerDuvidasFrequentes()

@then(u'valido o direcionamento para pagina faq')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaFaq()

@when(u'ao clicar no botao leia mais 1')
def step_impl(context):
    context.home.clicarNoLinkDaFaq1()

@then(u'valido o direcionamento para pagina faq1')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaFaq1()

@when(u'ao clicar no botao leia mais 2')
def step_impl(context):
    context.home.clicarNoLinkDaFaq2()

@then(u'valido o direcionamento para pagina faq2')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaFaq2()



@when(u'ao clicar no botao loja mobile android')
def step_impl(context):
    context.home.clicarNoBotaoLojaAndorid()

@then(u'valido o direcionamento para pagina google play')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaGooglePlay()


@when(u'ao clicar no botao loja mobile ios')
def step_impl(context):
    context.home.clicarNoBotaoLojaIos()

@then(u'valido o direcionamento para pagina app store')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaAppStore()















