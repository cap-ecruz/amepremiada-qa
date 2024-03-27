import time
from selenium.webdriver.common.by import By
from pages.verificarPaginasPage import VerificarPaginas

class EsqueciMinhaSenhaElementos(object):
    CAMPO_CPF = (By.ID, 'input-flCpf')
    BOTAO_ENVIAR_CODIGO = (By.ID, 'flRenovarSenha')
    BOTAO_OK = (By.CLASS_NAME, 'swal2-confirm.swal2-styled')

class EsqueciMinhaSenhaPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = EsqueciMinhaSenhaElementos()

    def inserirCPFEsqueciMinhaSenha(self, dado):
        self._comandos.inserirDado(self.elemento.CAMPO_CPF, dado)

    def clicarNoBotaoEnviarCodigo(self):
        self._comandos.clicar(self.elemento.BOTAO_ENVIAR_CODIGO)

    def clicarNoBotaoOk(self):
        self._comandos.clicar(self.elemento.BOTAO_OK)