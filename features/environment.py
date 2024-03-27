from utils.setup import Setup as setup


def before_all(context):
     setup.dadosDoUsuario(context)
     setup.desejaTirarPrint(context)
     setup.escolherDimensaoTela(context)
     setup.escolherBrowser(context)


def before_scenario(context, scenario):
     setup.abrirBrowser(context)


def after_scenario(context, scenario):
     try:
         setup.gerarPrint(context, scenario, scenario.status)
     except:
        context.browser.quit()
     context.browser.quit()
