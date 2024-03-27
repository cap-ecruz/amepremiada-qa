from behave import given, then, when
from utils.utils import Utils as info


#@given(u'que esteja na pagina meus titulos')
#def step_impl(context, visualizarTituloPage=None):
    #context.meusTitulos = visualizarTituloPage(context.browser)
    #context.meusTitulos.paginaMeusTitulos()
    #try:
        #context.minhasTeleSenas.clicarNoBotaoEntendiPoliticaDeCookies()
    #except:
        #...


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

@given(u'que esteja na pagina meus titulos')
def step_impl(context):
    context.visualizarTitulo.verificarSeEstaNaPaginaMeusTitulos()


@given(u'verifique que o usuario tenha titulos da campanha atual')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given verifique que o usuario tenha titulos da campanha atual')


@when(u'ao clicar no botao ver titulos')
def step_impl(context):
    raise NotImplementedError(u'STEP: When ao clicar no botao ver titulos')


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