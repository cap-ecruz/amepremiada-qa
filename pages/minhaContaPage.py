import time
from selenium.webdriver.common.by import By
from pages.verificarPaginasPage import VerificarPaginas
from nose.tools import assert_equal

class MinhaContaElementos(object):
   
    MEUS_TITULOS = (By.XPATH, '(//*[@class="card-title"])[1]')
    MINHAS_PREMIACOES = (By.XPATH, '(//*[@class="card-title"])[2]')
    HISTORICO_DE_PREMIACAO = (By.XPATH, '(//*[@class="card-title"])[3]')
    MEUS_DADOS = (By.XPATH, '(//*[@class="card-title"])[4]')

    
class MinhaContaPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = MinhaContaElementos()

    def acessarMeusTitulos(self):
        assert_equal(self._comandos.obterTexto(self.elemento.MEUS_TITULOS), 'Meus Títulos')
        self._comandos.clicar(self.elemento.MEUS_TITULOS)