import time
from selenium.webdriver.common.by import By
from pages.verificarPaginasPage import VerificarPaginas
from nose.tools import assert_equal

class MeusTitulosElementos(object):
   
    MEUS_TITULOS = (By.CSS_SELECTOR, '.fl-h2.ng-tns-c48-10')
    # SELECT_ANO = 
    NOME_CAMPANHA = (By.CSS_SELECTOR, '.card-title')
    # CONDICOES_GERAIS = 
    BOTAO_VER_TITULOS = (By.CSS_SELECTOR, '.btn-outline-primary')

    
class MeusTitulosPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = MeusTitulosElementos()

    def verificarNomeCampanha(self):
       assert_equal(self._comandos.obterTexto(self.elemento.MEUS_TITULOS), 'Meus Títulos')
       assert_equal(self._comandos.obterTexto(self.elemento.NOME_CAMPANHA), 'Ame Premiada Série1')
       
    def clicarEmVerTitulos(self):
        self._comandos.clicar(self.elemento.BOTAO_VER_TITULOS)