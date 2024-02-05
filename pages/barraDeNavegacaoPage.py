from selenium.webdriver.common.by import By
from nose.tools import assert_true
from nose.tools import assert_equal

from pages.verificarPaginasPage import VerificarPaginas
from utils.utils import Utils as info


class BarraDeNavegacaoElementos(object):
    MENU_LOGO_AME_PREMIADA = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[1]/div/a')
    MENU_HAMBURGUER = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[1]/button')
    # MENU_HOME = (By.XPATH, '//*[@id="mainMenu"]/ul[1]/li[1]/a')
    MENU_RESULTADOS = (By.CSS_SELECTOR, '.nav-link.link-active') #(By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[2]/ul[1]/li[1]/a')
    MENU_CADASTRE_SEU_TITULO = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[2]/ul[1]/li[2]/a')
    MENU_CADASTRE_SEU_TITULO_MOBILE = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[2]/ul[1]/li[2]/a')
    INSTITUICAO_BENEFICIADA = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[2]/ul[1]/li[3]/a')
    COMPREJA = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/span[1]/a')
    COMPREJA_MOBILE = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[2]/ul[1]/li[4]/a')
    CARRINHO = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/span[2]/a')
    BOTAO_LOGIN = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/a')

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
    SUBMENU_MEUS_DADOS = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/div/div/ul/li[5]/a')
    SUBMENU_SAIR = (By.XPATH, '/html/body/app-root/app-header/header/nav/div/div[3]/div/div/div[2]/a')


class BarraDeNavegacaoPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = BarraDeNavegacaoElementos()

    def paginaHome(self):
        self._comandos.navegar(self.PAGINA_HOME)

    def verificarSeEstaNaPaginaHome(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_HOME)

    def abrirMenuHamburguer(self):
        self._comandos.clicar(self.elemento.MENU_HAMBURGUER)

    def paginaLogin(self):
        self._comandos.navegar(self.PAGINA_LOGIN)

    def clicarNaLogo(self):
        self._comandos.clicar(self.elemento.MENU_LOGO_AME_PREMIADA)


    def clicarNaResultados(self):
        try:
            self._comandos.clicar(self.elemento.MENU_RESULTADOS)
        except:
            self.abrirMenuHamburguer()
            self._comandos.clicar(self.elemento.MENU_RESULTADOS)

    def clicarNoMenuCadastreSeuTitulo(self):
        try:
            self._comandos.clicar(self.elemento.MENU_CADASTRE_SEU_TITULO)
        except:
            self.abrirMenuHamburguer()
            self._comandos.clicar(self.elemento.MENU_CADASTRE_SEU_TITULO_MOBILE)

    def clicarNoMenuInstituicaoBeneficiada(self):
        try:
            self._comandos.clicar(self.elemento.INSTITUICAO_BENEFICIADA)
        except:
            self.abrirMenuHamburguer()
            self._comandos.clicar(self.elemento.INSTITUICAO_BENEFICIADA)

    def clicarNoMenuCompreJa(self):
        try:
            self._comandos.clicar(self.elemento.COMPREJA)
        except:
            self.abrirMenuHamburguer()
            self._comandos.clicar(self.elemento.COMPREJA_MOBILE)

    def clicarNoCarrinho(self):
        self._comandos.clicar(self.elemento.CARRINHO)

    def clicarNoBotaoLogin(self):
        self._comandos.clicar(self.elemento.BOTAO_LOGIN)

    #  parte logada

    def efetuarLogin(self):
        self._comandos.inserirDado(self.elemento.CAMPO_CPF, info.CPF_CADASTRADO)
        self._comandos.inserirDado(self.elemento.CAMPO_SENHA, info.SENHA_CADASTRADO)
        self._comandos.clicar(self.elemento.BOTAO_ENTRAR_LOGIN)

    def clicarSubMenuMinhaContaToggler(self):
        self._comandos.clicar(self.elemento.BOTAO_MINHA_CONTA_TOGGLER)

    def clicarSubMenuMinhaConta(self):
        self._comandos.clicar(self.elemento.SUBMENU_MINHA_CONTA)

    def validarSubmenuToggler(self):
        assert_true(self._comandos.obterElemento(self.elemento.MENU_USUARIO))

    def clicarSubMenuMeusTitulos(self):
        self._comandos.clicar(self.elemento.SUBMENU_MEUS_TITULOS)

    def clicarSubMenuMeusDados(self):
        self._comandos.clicar(self.elemento.SUBMENU_MEUS_DADOS)

    def clicarSubMenuSair(self):
        self._comandos.clicar(self.elemento.SUBMENU_SAIR)

    def verificarSeEstaNaPaginaResultados(self):
        assert_equal(self._comandos.capturar_url(), self.PAGINA_RESULTADOS)
