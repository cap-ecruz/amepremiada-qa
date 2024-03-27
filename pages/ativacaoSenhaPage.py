import time
from selenium.webdriver.common.by import By
from pages.verificarPaginasPage import VerificarPaginas

class AtivacaoSenhaElementos(object):
    CAMPO_CODIGO = (By.ID, 'flCode1')
    BOTAO_CONFIRMAR_CODIGO = (By.ID, 'flConfirmar')
class AtivacaoSenhaPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = AtivacaoSenhaElementos()

    def inserirCodigoDeAtivacao(self, dado):
        self._comandos.inserirDado(self.elemento.CAMPO_CODIGO, dado)

    def clicarNoBotaoConfirmarCodigo(self):
        self._comandos.clicar(self.elemento.BOTAO_CONFIRMAR_CODIGO)

