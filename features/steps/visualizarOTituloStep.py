from behave import given, then, when
from utils.utils import Utils as info


@given(u'que esteja na pagina minhas Tele Sena')
def step_impl(context):
    context.minhasTeleSenas = VisualizarOTituloPage(context.browser)
    context.minhasTeleSenas.paginaMinhasTeleSenas()
    try:
        context.minhasTeleSenas.clicarNoBotaoEntendiPoliticaDeCookies()
    except:
        ...


@then(u'verifique que o usuario tenha titulos da campanha atual')
def step_impl(context):
    context.minhasTeleSenas.verificarSeOUsuarioTemTitulosDaCampanhaAtual(info.CAMPANHA_ATUAL)

@then(u'que o numero da susep esta de acordo com a campanha')
def step_impl(context):
    context.minhasTeleSenas.verificarNumeroDaSusep('SUSEP: ' + info.NUMERO_SUSEP)

@when(u'ao clicar no botao ver todos os titulos')
def step_impl(context):
    context.minhasTeleSenas.clicarNoBotaoVerTodosOsTitulos()


@when(u'ao clicar no titulo')
def step_impl(context):
    context.minhasTeleSenas.clicarNoTitulo(info.NUMERO_DO_TITULO)
    # teste de falha de procura de titulo
    # context.minhasTeleSenas.clicarNoTitulo('2.023.982')

@then(u'verifique o breadcrumb e o mesmo titulo selecionado')
def step_impl(context):
    context.minhasTeleSenas.verificarBreadCrumbTitulo(info.NUMERO_DO_TITULO)

@then(u'verifique o filtro de titulos e o mesmo titulo selecionado')
def step_impl(context):
    context.minhasTeleSenas.VerificarTitulosFiltro(info.NUMERO_DO_TITULO)

@then(u'verifique o nome da campanha no header do titulo')
def step_impl(context):
    context.minhasTeleSenas.verificarNomeCampanhaHeaderDoTitulo(info.CAMPANHA_ATUAL)

@then(u'verifique o numero da susep no header do titulo')
def step_impl(context):
    context.minhasTeleSenas.verificarNumeroDaSusepHeaderDoTitulo('SUSEP: ' + info.NUMERO_SUSEP)


@when(u'ao clicar no botao raspar automaticamente')
def step_impl(context):
    context.minhasTeleSenas.clicarNoBotaoRasparAutomaticamente()

@then(u'verifique que o botao foi desabilitado')
def step_impl(context):
    context.minhasTeleSenas.verificarSeOBotaoRasparAutomaticamenteFoiDesabilitado()
