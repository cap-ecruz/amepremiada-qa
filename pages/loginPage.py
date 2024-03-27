import time
from selenium.webdriver.common.by import By
from pages.verificarPaginasPage import VerificarPaginas

class LoginElementos(object):
    BOTAO_ENTENDI_POLITICA_COOKIES = (By.CLASS_NAME, 'cc-btn')

    CAMPO_CPF = (By.ID, 'input-username')
    CAMPO_SENHA = (By.ID, 'flSenha')
    BOTAO_FAZER_LOGIN = (By.ID, 'flLogin')
    BOTAO_FAZER_ESQUECI_MINHA_SENHA = (By.CLASS_NAME, 'text-third')

class LoginPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = LoginElementos()

    def paginaLogin(self):
        self._comandos.navegar(self.PAGINA_LOGIN)
        time.sleep(0.8)

    def clicarNoBotaoEntendiPoliticaDeCookies(self):
        self._comandos.clicar(self.elemento.BOTAO_ENTENDI_POLITICA_COOKIES)
        time.sleep(0.8)

    def inserirCPFLogin(self, dado):
        self._comandos.inserirDado(self.elemento.CAMPO_CPF, dado)

    def inserirSenhaLogin(self, dado):
        self._comandos.inserirDado(self.elemento.CAMPO_SENHA, dado)

    def clicarNoBotaoFazerLogin(self):
        self._comandos.clicar(self.elemento.BOTAO_FAZER_LOGIN)

    def clicarNoBotaoEsqueciMinhaSenha(self):
        self._comandos.clicar(self.elemento.BOTAO_FAZER_ESQUECI_MINHA_SENHA)
