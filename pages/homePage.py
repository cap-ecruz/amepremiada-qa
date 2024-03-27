import time
from selenium.webdriver.common.by import By
from nose.tools import assert_equal, assert_false, assert_true
from selenium.webdriver.support.select import Select
from pages.verificarPaginasPage import VerificarPaginas

class HomeElementos(object):
    MENSAGEM_COOKIE = (By.ID, 'cookieconsent:desc')
    LINK_POLITICA_DE_PRIVACIDADE_COOKIE = (By.XPATH, '/html/body/div/span/a')
    BANNER_PRINCIPAL_HOME_COMPRAR_TITULO = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-home-banner-v2/figure/figcaption/span/a')
    BOTAO_CLIQUE_AQUI_E_CONFIRA_SEUS_RESULTADOS = (
    By.XPATH, '/html/body/app-root/div/ng-component/main/app-como-receber-premio/section/div/div[2]/a')
    BOTAO_VEJA_MAIS_SOBRE_A_FUNDACAO_ABRINQ = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-home-instituicao-beneficiada/section/div/div/div[1]/a')
    BOTAO_LOGIN = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/a/span')
    LINK_VER_DUVIDAS_FREQUENTES = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-home-duvidas-frequentes/section/div/div/a')
    LINK_FAQ1 = (By.XPATH, '(//*[@class="btn btn-text btn-faq"])[1]')
    LINK_FAQ2 = (By.XPATH, '(//*[@class="btn btn-text btn-faq"])[2]')
    LOJA_ANDROID = (By.XPATH, '(//*[@class="btn btn-secondary"])[1]')
    LOJA_IOS = (By.XPATH, '(//*[@class="btn btn-secondary"])[2]')
class HomePage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = HomeElementos()
    def paginaHome(self):
        self._comandos.navegar(self.PAGINA_HOME)
    def verificarSeEstaNaPaginaHome(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_HOME)
    def verificarMensagemCookie(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.MENSAGEM_COOKIE), msg)
    def clicarNoLinkPoliticaDePrivacidade(self):
        self._comandos.clicar(self.elemento.LINK_POLITICA_DE_PRIVACIDADE_COOKIE)
    def clicarNoBotaoDoBannerPrincipalHome(self):
        self._comandos.clicar(self.elemento.BANNER_PRINCIPAL_HOME_COMPRAR_TITULO)

    def clicarNoBotaoCliqueAquiEConfiraSeusResultados(self):
        self._comandos.clicar(self.elemento.BOTAO_CLIQUE_AQUI_E_CONFIRA_SEUS_RESULTADOS)

    def clicarNoBotaoVejaMaisSobreAFundacao(self):
        self._comandos.clicar(self.elemento.BOTAO_VEJA_MAIS_SOBRE_A_FUNDACAO_ABRINQ)

    def clicarNoBotaoLogin(self):
        self._comandos.clicar(self.elemento.BOTAO_LOGIN)

    def clicarNoLinkDaFaq1(self):
        self._comandos.clicar(self.elemento.LINK_FAQ1)

    def clicarNoLinkDaFaq2(self):
            self._comandos.clicar(self.elemento.LINK_FAQ2)

    def verificarSeEstaNaPaginaDuvidasFrequentes(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES)
    def verificarSeEstaNaPaginaFaq1(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES_FAQ1)

    def verificarSeEstaNaPaginaFaq2(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES_FAQ2)

    def clicarNoLinkVerDuvidasFrequentes(self):
        self._comandos.clicar(self.elemento.LINK_VER_DUVIDAS_FREQUENTES)

    def verificarSeEstaNaPaginaPoliticaDePrivacidade(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_POLITICA_DE_PRIVACIDADE)

    def verificarSeEstaNaPaginaComoComprar(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_COMO_COMPRAR)

    def verificarSeEstaNaPaginaResultados(self):
        time.sleep(2)
        assert_equal(self._comandos.capturar_url(), self.PAGINA_RESULTADOS)


    def clicarNoBotaoLojaAndorid(self):
        self._comandos.clicar(self.elemento.LOJA_ANDROID)

    def clicarNoBotaoLojaIos(self):
        self._comandos.clicar(self.elemento.LOJA_IOS)

    def verificarSeEstaNaPaginaGooglePlay(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_GOOGLE_PLAY)

    def verificarSeEstaNaPaginaAppStore(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_APP_STORE)