import time
from selenium.webdriver.common.by import By
from nose.tools import assert_true
from nose.tools import assert_equal
from pages.verificarPaginasPage import VerificarPaginas
from utils.utils import Utils as info

class BarraDeNavegacaoElementos(object):
    MENU_LOGO_AME_PREMIADA = (By.XPATH, '/html/body/app-root/app-header-home/header/nav/div/div[1]/div/a/img')
    MENU_HAMBURGUER = (By.XPATH, '/html/body/app-root/app-header-home/header/nav/div/div[1]/button')
    # MENU_HOME = (By.XPATH, '//*[@id="mainMenu"]/ul[1]/li[1]/a')
    # MENU_RESULTADOS = (By.CSS_SELECTOR, '.nav-link.link-active')
    MENU_RESULTADOS = (By.XPATH, '/html/body/app-root/app-header-home/header/nav/div/div[2]/ul[1]/li[1]/a')
    INSTITUICAO_BENEFICIADA = (By.XPATH, '/html/body/app-root/app-header-home/header/nav/div/div[2]/ul[1]/li[2]/a')
    COMPRAR_TITULO = (By.XPATH, '/html/body/app-root/app-header-home/header/nav/div/div[3]/span/button/span')
    #COMPRAR_TITULO_MOBILE = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[2]/ul[1]/li[4]/a')
    BOTAO_LOGIN = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/button[2]/span')

    # para efetuar login
    CAMPO_CPF = (By.ID, 'input-username')
    CAMPO_SENHA = (By.ID, 'flSenha')
    BOTAO_ENTRAR_LOGIN = (By.ID, 'flLogin')

    # submenu logado
    BOTAO_MINHA_CONTA_TOGGLER = (By.ID, 'userMenuToggler')
    MENU_USUARIO = (By.ID, 'userMenu')
    SUBMENU_MINHA_CONTA = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/div/div/ul/li[1]/a')
    # ('//*[@id="userMenu"]/div/ul/li[2]/a')
    SUBMENU_MEUS_TITULOS = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/div/div/ul/li[2]/a')
    SUBMENU_PREMIACOES = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/div/div/ul/li[3]/a')
    SUBMENU_MEUS_DADOS = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/div/div/ul/li[4]/a')
    SUBMENU_SAIR = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/div/div/div[2]')

    #dashboard
    DASHBOARD_MEUS_TITULOS = (By.XPATH, '/html/body/app-root/div/ng-component/main/section/div/div/div/div[1]/app-card/div/div[2]/a')
    DASHBOARD_PREMIACOES = (By.XPATH, '/html/body/app-root/div/ng-component/main/section/div/div/div/div[2]/app-card/div/div[2]/a')
    DASHBOARD_MEUS_DADOS = (By.XPATH, '/html/body/app-root/div/ng-component/main/section/div/div/div/div[3]/app-card/div/div[2]/a')
    DASHBOARD_HISTORICO_PREMIACOES = (By.XPATH, '/html/body/app-root/div/ng-component/main/section/div/div/div/div[4]/app-card/div/div[2]/a')

    #parte logada
    PAGINA_HOME = 'https://staging.amepremiada.com.br/#/'
    PAGINA_INICIAL = 'https://staging.amepremiada.com.br/#/'
    PAGINA_MINHA_CONTA = PAGINA_HOME + 'minha-conta.html'
    PAGINA_MEUS_TITULOS = PAGINA_HOME + 'meus-titulos/2023.html'
    PAGINA_MEUS_DADOS = PAGINA_HOME + 'meus-dados.html'
    PAGINA_MINHAS_PREMIACOES = PAGINA_HOME + 'minhas-premiacoes.html'
    PAGINA_HISTORICO_PREMIACOES = PAGINA_HOME + 'historico-premiacoes.html'

class BarraDeNavegacaoPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = BarraDeNavegacaoElementos()

    def paginaHome(self):
        self._comandos.navegar(self.PAGINA_HOME)

    def verificarSeEstaNaPaginaInicial(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_INICIAL)
    def verificarSeEstaNaPaginaAme(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_AME)
    def abrirMenuHamburguer(self):
        self._comandos.clicar(self.elemento.MENU_HAMBURGUER)

    def paginaLogin(self):
        self._comandos.navegar(self.PAGINA_LOGIN)

    def clicarNaLogo(self):
        self._comandos.clicar(self.elemento.MENU_LOGO_AME_PREMIADA)

    def clicarNaResultados(self):
        time.sleep(4)
        try:
            self._comandos.clicar(self.elemento.MENU_RESULTADOS)
        except:
            self.abrirMenuHamburguer()
            self._comandos.clicar(self.elemento.MENU_RESULTADOS)

    def clicarNoMenuInstituicaoBeneficiada(self):
        try:
            self._comandos.clicar(self.elemento.INSTITUICAO_BENEFICIADA)
        except:
            self.abrirMenuHamburguer()
            self._comandos.clicar(self.elemento.INSTITUICAO_BENEFICIADA)

    def clicarNoMenuComprarTitulo(self):
        try:
            self._comandos.clicar(self.elemento.COMPRAR_TITULO)
        except:
            self.abrirMenuHamburguer()
            #self._comandos.clicar(self.elemento.COMPRAR_TITULO_MOBILE)

    def clicarNoBotaoLogin(self):
        self._comandos.clicar(self.elemento.BOTAO_LOGIN)

    def clicarAbrirMenuDeUsuario(self):
        self._comandos.clicar(self.elemento.BOTAO_LOGIN)


    #  parte logada
    def efetuarLogin(self):
        self._comandos.inserirDado(self.elemento.CAMPO_CPF, info.CPF_CADASTRADO)
        self._comandos.inserirDado(self.elemento.CAMPO_SENHA, info.SENHA_CADASTRADO)
        self._comandos.clicar(self.elemento.BOTAO_ENTRAR_LOGIN)

    def validarSubmenuToggler(self):
        assert_true(self._comandos.obterElemento(self.elemento.MENU_USUARIO))

    def verificarSeEstaNaPaginaMinhaConta(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MINHA_CONTA)

    def clicarSubMenuMinhaContaToggler(self):
        self._comandos.clicar(self.elemento.BOTAO_MINHA_CONTA_TOGGLER)

    def clicarSubMenuMinhaContaToggler(self):
        self._comandos.clicar(self.elemento.SUBMENU_MINHA_CONTA)

    def clicarSubMenuMeusTitulosToggler(self):
        self._comandos.clicar(self.elemento.SUBMENU_MEUS_TITULOS)

    def verificarSeEstaNaPaginaSubMenuMeusTitulos(self):
        assert_equal(self._comandos.capturar_url(), self.elemento.SUBMENU_MEUS_TITULOS)

    def clicarSubMenuMinhasPremiacoesToggler(self):
        self._comandos.clicar(self.elemento.SUBMENU_PREMIACOES)

    def verificarSeEstaNaPaginaHome(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_HOME)
    def verificarSeEstaNaPaginaMeusDados(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MEUS_DADOS)

    def verificarSeEstaNaPaginaMinhasPremiacoes(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MINHAS_PREMIACOES)

    def verificarSeEstaNaPaginaHistoricoDePremiacoes(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_HISTORICO_PREMIACOES)

    def verificarSeEstaNaPaginaMeusDados(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_HOME)

    def clicarSubMenuMeusDados(self):
        time.sleep(2)
        self._comandos.clicar(self.elemento.SUBMENU_MEUS_DADOS)

    def clicarSubMenuSair(self):
        self._comandos.clicar(self.elemento.SUBMENU_SAIR)

    def clicarDashboardMeusTitulos(self):
        self._comandos.clicar(self.elemento.DASHBOARD_MEUS_TITULOS)

    def clicarDashboardPremiacoes(self):
        self._comandos.clicar(self.elemento.DASHBOARD_PREMIACOES)

    def clicarDashboardHistoricoDePremiacoes(self):
        self._comandos.clicar(self.elemento.DASHBOARD_HISTORICO_PREMIACOES)

    def clicarDashboardMeusDados(self):
        self._comandos.clicar(self.elemento.DASHBOARD_MEUS_DADOS)