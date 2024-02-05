import time
from selenium.webdriver.common.by import By
from nose.tools import assert_equal, assert_false, assert_true
from selenium.webdriver.support.select import Select
from pages.verificarPaginasPage import VerificarPaginas

class HomeElementos(object):
    MENSAGEM_COOKIE = (By.ID, 'cookieconsent:desc')
    LINK_POLITICA_DE_PRIVACIDADE_COOKIE = (By.XPATH, '/html/body/div/span/a')
    
    BANNER_VANTAGENS_DO_BEM_DA_SORTE = (By.XPATH,
                                        '/html/body/app-root/div/ng-component/main/div[2]/div/app-banners-campanha/section/div/div/div/div/app-banners-campanha-banner/a/figure/picture/img')
    BOTAO_CLIQUE_AQUI_E_CONFIRA_SEUS_RESULTADOS = (
    By.XPATH, '/html/body/app-root/div/ng-component/main/app-como-receber-premio/section/div/div[2]/a')

    BOTAO_VEJA_MAIS_SOBRE_A_FUNDACAO_ABRINQ = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-home-instituicao-beneficiada/section/div/div/div[1]/a')

    LINK_FAQ1 = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-home-duvidas-frequentes/section/div/ul/li[1]/app-home-faq/div/div[3]/a')
    LINK_FAQ2 = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-home-duvidas-frequentes/section/div/ul/li[2]/app-home-faq/div/div[3]/a')
    LINK_VER_DUVIDAS_FREQUENTES = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-home-duvidas-frequentes/section/div/div/a')

class HomePage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = HomeElementos()
        # self.elementoPaginaCheckout = PaginaCheckoutElementos()

    def paginaHome(self):
        self._comandos.navegar(self.PAGINA_HOME)

    def verificarMensagemCookie(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.MENSAGEM_COOKIE), msg)

    def clicarNoLinkPoliticaDePrivacidade(self):
        self._comandos.clicar(self.elemento.LINK_POLITICA_DE_PRIVACIDADE_COOKIE)

    def clicarNoBotaoDoBannerPrincipalHome(self):
        self._comandos.clicar(self.elemento.BANNER_PRINCIPAL_HOME_COMPRAR_TITULO)

    def clicarNoBannerVantagensDoamepremiada(self):
        self._comandos.clicar(self.elemento.BANNER_VANTAGENS_DO_BEM_DA_SORTE)

    def clicarNoBotaoCliqueAquiEConfiraSeusResultados(self):
        self._comandos.clicar(self.elemento.BOTAO_CLIQUE_AQUI_E_CONFIRA_SEUS_RESULTADOS)

    def clicarNoBotaoVejaMaisSobreAFundacaoAbrinq(self):
        self._comandos.clicar(self.elemento.BOTAO_VEJA_MAIS_SOBRE_A_FUNDACAO_ABRINQ)

    def clicarNoLinkDaFaq(self, link):
        if 'ler mais 1' in link:
            self._comandos.clicar(self.elemento.LINK_FAQ1)
        if 'ler mais 2' in link:
            self._comandos.clicar(self.elemento.LINK_FAQ2)
        if 'ver mais duvidas frequentes' in link:
            self._comandos.clicar(self.elemento.LINK_VER_DUVIDAS_FREQUENTES)

    def verificarSeEstaNaPaginaPoliticaDePrivacidade(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_POLITICA_DE_PRIVACIDADE)

    def verificarSeEstaNaPaginaDeCompraDoProduto(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_COMO_COMPRAR)
