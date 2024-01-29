import time
from behave import given, then, when
from pages.homePage import HomePage


@given(u'que eu estou na pagina home')
def step_impl(context):
    time.sleep(0.5)
    context.home = HomePage(context.browser)
    context.home.paginaHome()


@then(u'verifico a exibicao da mensagem de cookie {msg}')
def step_impl(context, msg):
    context.home.verificarMensagemCookie(msg)


@when(u'ao clicar no link Politica de privacidade')
def step_impl(context):
    context.home.clicarNoLinkPoliticaDePrivacidade()

@then(u'verifica o direcionamento para pagina Politica de Privacidade')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaPoliticaDePrivacidade()


@when(u'ao clicar no botao do banner principal')
def step_impl(context):
    context.home.clicarNoBotaoDoBannerPrincipalHome()


#  clicar no banner vantagens do ame premiada
@when(u'ao clicar no banner vantagens do ame premiada')
def step_impl(context):
    context.home.clicarNoBannerVantagensDoBemDaSorte()


# premiacao sem complicacao - pagina premiacoes logado
@when(u'ao clicar no botao clique aqui e confira seus resultados')
def step_impl(context):
    context.home.clicarNoBotaoCliqueAquiEConfiraSeusResultados()


@then(u'valido o direcionamento para pagina minhas premiacoes')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaMinhasPremiacoes()


# meus atalhos logado- <opcaoatalho>
@when(u'ao clicar no card conferir sorteios')
def step_impl(context):
    context.home.clicarNoCardConferirSorteio()


@when(u'ao clicar no card meus titulos')
def step_impl(context):
    context.home.clicarNoCardMeusTitulos()


# clicar o botao veja mais sobre a fundacao abrinq
@when(u'ao clicar no botao veja mais sobre a fundacao abrinq')
def step_impl(context):
    context.home.clicarNoBotaoVejaMaisSobreAFundacaoAbrinq()


@then(u'valido o direcionamento para pagina como comprar')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaComoComprar()


@then(u'valido o direcionamento para pagina resultados')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaResultados()


@then(u'valido o direcionamento para pagina Instituicao beneficiada')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaInstituicaoBeneficiada()


@then(u'valido o direcionamento para pagina login')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaLogin()


# ----- faq home
@when(u'ao clicar no link da faq {link}')
def step_impl(context, link):
    context.home.clicarNoLinkDaFaq(link)


@then(u'valido o direcionamento para pagina da duvida frequentes faq')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaFaq()
    
@then(u'valido o direcionamento para pagina da duvida frequentes faq1')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaDuvidasFrequentesFaq1()

@then(u'valido o direcionamento para pagina da duvida frequentes faq2')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaDuvidasFrequentesFaq2()


@when(u'ao clicar ler mais 1')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaFaq()

@then(u'valido o direcionamento para pagina faq1')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaFaq1()


@when(u'ao clicar ler mais 2')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaFaq2()

@then(u'valido o direcionamento para pagina faq2')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaFaq2()


@when(u'ao clicar ver mais duvidas frequentes')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaDuvidasFrequentes()



