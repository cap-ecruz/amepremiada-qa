import time

from selenium.webdriver.common.by import By
from nose.tools import assert_equal
from pages.verificarPaginasPage import VerificarPaginas

class RodapeElementos(object):
    RODAPE_LOGO_AME_PREMIADA = (By.XPATH, '/html/body/app-root/app-footer/footer/section[1]/div/div/div[1]/a')
    RODAPE_LOGO_AME = (By.XPATH, '/html/body/app-root/app-footer/footer/section[1]/div/div/div[1]/div/a')
    RODAPE_DUVIDAS = (By.XPATH, '//*[@title="Dúvidas Frequentes"]')
    RODAPE_RESULTADOS = (By.XPATH, '//*[@id="mainMenu"]/ul[1]/li[2]/a')
    RODAPE_BRASILCAP = (By.XPATH, '//*[@id="mainMenu"]/ul[1]/li[2]/a')
    RODAPE_CONDICOES_GERAIS = (By.XPATH, '//a[contains(text(), "Condições Gerais")]')
    RODAPE_TERMOS_LEGAL = (By.XPATH, '//a[contains(text(), "Termos Legais")]')
    RODAPE_TERMOS_USO = (By.XPATH, '//a[contains(text(), "Termos de Uso")]')
    RODAPE_TERMOS_PRIVACIDADE = (By.XPATH, '//a[contains(text(), "Política de Privacidade")]')
    RODAPE_TERMOS_COOKIE = (By.XPATH, '//a[contains(text(), "Política de Cookies")]')

class RodapePage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = RodapeElementos()

    def paginaHome(self):
        self._comandos.navegar(self.PAGINA_HOME)

    def clicarDuvidas(self):
        self._comandos.clicar(self.elemento.RODAPE_DUVIDAS)

    def verificarSeEstaNaPaginaAtendimento(self):
        self._comandos.trocarAba(self.PAGINA_DUVIDAS_FREQUENTES)
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES)

    def clicarTermos(self, opcoes):
        if 'condicoes gerais' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_CONDICOES_GERAIS)
        elif 'termos legais' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_TERMOS_LEGAL)
        elif 'termos de uso' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_TERMOS_USO)
        elif 'politica de privacidade' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_TERMOS_PRIVACIDADE)
        elif 'politica de cookies' in opcoes:
            self._comandos.clicar(self.elemento.RODAPE_TERMOS_COOKIE)
    
    def clicarIconeLogo(self, opcao):
        if 'ame premiada' in opcao:
            self._comandos.clicar(self.elemento.RODAPE_LOGO_AME_PREMIADA)
        elif 'ame' in opcao:
            self._comandos.clicar(self.elemento.RODAPE_LOGO_AME)

    def verificarSeEstaNaPagina(self, escolhida):
        if 'condicoes gerais' in escolhida:
            self.verificarSeEstaNaPaginaCondicoesGerais()
        elif 'termos legais' in escolhida:
            self.verificarSeEstaNaPaginaTermosLegais()
        elif 'termos de uso' in escolhida:
            self.verificarSeEstaNaPaginaTermosUso()
        elif 'politica de privacidade' in escolhida:
            self.verificarSeEstaNaPaginaPoliticaDePrivacidade()
        elif 'politica de cookies' in escolhida:
            self.verificarSeEstaNaPaginaPoliticaDeCookies()

    def verificarSeEstaNaPaginaCondicoesGerais(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CONDICOES_GERAIS)
    def verificarSeEstaNaPaginaTermosLegais(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_TERMOS_LEGAIS)
    def verificarSeEstaNaPaginaTermosUso(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_TERMOS_USO)

    def verificarSeEstaNaPaginaPoliticaDePrivacidade(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_POLITICA_DE_PRIVACIDADE)

    def verificarSeEstaNaPaginaPoliticaDeCookies(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_POLITICA_DE_COOKIES)

    def verificarSeEstaNaPaginaAme(self):
        time.sleep(2)
        assert_equal(self._comandos.capturar_url(), self.PAGINA_AME)

    def mudarDeAba(self, pagina):
        if 'home' in pagina:
            self._comandos.trocarAba(self.PAGINA_HOME)
        elif 'Ame' in pagina:
            self._comandos.trocarAba(self.PAGINA_AME)


    def verificarSeEstaNaPaginaHome(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_HOME)