import time
from selenium.webdriver.common.by import By
from pages.verificarPaginasPage import VerificarPaginas
from utils.utils import Utils as info
from nose.tools import assert_equal, assert_false


class VisualizarOTituloElementos(object):
    BOTAO_ENTENDI_POLITICA_COOKIES = (By.XPATH, '/html/body/div[1]/div/a')

    PRIMEIRO_NOME_CAMPANHA_DA_LISTA = (By.XPATH, '/html/body/app-root/ng-component/main/div[2]/ul/li[1]/div/div['
                                                 '1]/app-campanha-nome/div/div/h4')
    NUMERO_SUSEP_PAGINA_MINHAS_TELE_SENA = (By.XPATH, '/html/body/app-root/ng-component/main/div[2]/ul/li[1]/div/div['
                                                      '1]/app-campanha-nome/div/div/div[1]')

    BOTAO_VER_TODAS_TELE_SENAS_PRIMEIRO_DA_LISTA = (By.XPATH, '/html/body/app-root/ng-component/main/div[2]/ul/li['
                                                              '1]/div/div[3]/a')

    PRIMEIRO_NUMERO_TITULO_DA_LISTA = (By.XPATH, '/html/body/app-root/ng-component/main/div/div/div[3]/div/div['
                                                 '1]/app-minhas-telesenas-titulos-lista/ol/li[1]/a/div/span')

    PRIMEIRO_TITULO_DA_LISTA = (By.XPATH, '/html/body/app-root/ng-component/main/div/div/div[3]/div/div['
                                          '1]/app-minhas-telesenas-titulos-lista/ol/li[1]/a/div/span')

    # pagina do titulo S
    BREADCRUMB_NUMERO_TITULO = (By.XPATH, '/html/body/app-root/ng-component/main/app-breadcrumb/nav/ol/li[5]/span')

    FILTRO_TITULOS = (By.XPATH, '/html/body/app-root/ng-component/main/div/div/app-minha-telesena-header/div/div['
                                '2]/div[1]/div[1]/div')

    NOME_CAMPANHA_HEADER_TITULO = (By.XPATH, '/html/body/app-root/ng-component/main/div/div/app-minha-telesena-header'
                                             '/div/div[1]/app-campanha-nome/div/div/h4')

    NUMERO_SUSEP_HEADER_TITULO = (By.XPATH, '/html/body/app-root/ng-component/main/div/div/app-minha-telesena-header'
                                            '/div/div[1]/app-campanha-nome/div/div/div[1]')

    BOTAO_RASPAR_AUTOMATICAMENTE = (By.XPATH, '/html/body/app-root/ng-component/main/div/div/app-minha-telesena-area'
                                              '-interacao/div/div/app-premiacao-instantanea/app-minha-telesena-premiacao-raspadinha-v2/div/div[2]/button')


class VisualizarOTituloPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = VisualizarOTituloElementos()

    def paginaMinhasTeleSenas(self):
        self._comandos.navegar(self.PAGINA_MINHAS_TELE_SENAS)

    def clicarNoBotaoEntendiPoliticaDeCookies(self):
        self._comandos.clicar(self.elemento.BOTAO_ENTENDI_POLITICA_COOKIES)
        time.sleep(0.5)

    def verificarSeOUsuarioTemTitulosDaCampanhaAtual(self, nomeCamapanhaAtual):
        assert_equal(self._comandos.obterTexto(self.elemento.PRIMEIRO_NOME_CAMPANHA_DA_LISTA), nomeCamapanhaAtual)

    def verificarNumeroDaSusep(self, numeroDaSusep):
        assert_equal(self._comandos.obterTexto(self.elemento.NUMERO_SUSEP_PAGINA_MINHAS_TELE_SENA), numeroDaSusep)

    def clicarNoBotaoVerTodosOsTitulos(self):
        self._comandos.clicar(self.elemento.BOTAO_VER_TODAS_TELE_SENAS_PRIMEIRO_DA_LISTA)

    def clicarNoTitulo(self, numeroTitulo):
        assert_equal((self._comandos.obterTexto(self.elemento.PRIMEIRO_NUMERO_TITULO_DA_LISTA)), numeroTitulo)
        # self._comandos.esperarTexto(self.elemento.PRIMEIRO_NUMERO_TITULO_DA_LISTA, numeroTitulo)
        self._comandos.clicar(self.elemento.PRIMEIRO_NUMERO_TITULO_DA_LISTA)

    def verificarBreadCrumbTitulo(self, numeroTitulo):
        time.sleep(1)
        assert_equal((self._comandos.obterTexto(self.elemento.BREADCRUMB_NUMERO_TITULO)), numeroTitulo)

    def VerificarTitulosFiltro(self, numeroTitulo):
        assert_equal((self._comandos.obterTexto(self.elemento.FILTRO_TITULOS)), numeroTitulo)

    def verificarNomeCampanhaHeaderDoTitulo(self, nomeDaCampanha):
        assert_equal((self._comandos.obterTexto(self.elemento.NOME_CAMPANHA_HEADER_TITULO)), nomeDaCampanha)

    def verificarNumeroDaSusepHeaderDoTitulo(self, numeroSusep):
        assert_equal((self._comandos.obterTexto(self.elemento.NUMERO_SUSEP_HEADER_TITULO)), numeroSusep)

    def clicarNoBotaoRasparAutomaticamente(self):
        self._comandos.clicar(self.elemento.BOTAO_RASPAR_AUTOMATICAMENTE)

    def verificarSeOBotaoRasparAutomaticamenteFoiDesabilitado(self):
        assert_equal((self._comandos.obterTexto(self.elemento.BOTAO_RASPAR_AUTOMATICAMENTE)), 'RASPADO')
        assert_false(self._comandos.elementoAtivo(self.elemento.BOTAO_RASPAR_AUTOMATICAMENTE))

