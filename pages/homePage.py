import time
from selenium.webdriver.common.by import By
from nose.tools import assert_equal, assert_false, assert_true
from selenium.webdriver.support.select import Select
from pages.verificarPaginasPage import VerificarPaginas


class HomeElementos(object):
    MENSAGEM_COOKIE = (By.ID, 'cookieconsent:desc')
    LINK_POLITICA_DE_PRIVACIDADE_COOKIE = (By.XPATH, '/html/body/div/span/a')
    BANNER_PRINCIPAL_HOME_COMPRAR_TITULO = (By.CSS_SELECTOR, '.cta.btn.btn-secondary.ng-star-inserted')
    VALOR_UNITARIO_TITULO = (By.XPATH, '/html/body/app-root/div/ng-component/main/div[2]/div/app-produtos-quantidade/div/div/form/div/div[1]/div[2]')
    VALOR_TOTAL = (By.XPATH,
                   '/html/body/app-root/div/ng-component/main/div[2]/div/app-produtos-quantidade/div/div/form/div/div[3]/div/label')
    BOTAO_COMPRAR_HOME = (By.XPATH,
                          '/html/body/app-root/div/ng-component/main/div[2]/div/app-produtos-quantidade/div/div/form/div/div[3]/button')

    BOTAO_ADICIONAR_TITULO = (By.XPATH,
                              '/html/body/app-root/div/ng-component/main/div[2]/div/app-produtos-quantidade/div/div/form/div/div[2]/div[1]/div[2]/button')
    BOTAO_REMOVER_TITULO = (By.XPATH,
                            '/html/body/app-root/div/ng-component/main/div[2]/div/app-produtos-quantidade/div/div/form/div/div[2]/div[1]/div[1]/button')
    BOTAO_MAIS5_TITULOS = (By.XPATH,
                           '/html/body/app-root/div/ng-component/main/div[2]/div/app-produtos-quantidade/div/div/form/div/div[2]/app-adiciona/div/div/button[1]')
    BOTAO_MAIS10_TITULOS = (By.XPATH,
                            '/html/body/app-root/div/ng-component/main/div[2]/div/app-produtos-quantidade/div/div/form/div/div[2]/app-adiciona/div/div/button[2]')
    BOTAO_LIMPAR_TITULOS = (By.XPATH,
                            '/html/body/app-root/div/ng-component/main/div[2]/div/app-produtos-quantidade/div/div/form/div/div[2]/app-adiciona/div/div/button[3]')

    # Tela mobile
    SELECIONAR_A_QUANTIDADE_MOBILE = (By.ID, 'CheckoutQtdeMobile')

    BANNER_VANTAGENS_DO_BEM_DA_SORTE = (By.XPATH,
                                        '/html/body/app-root/div/ng-component/main/div[2]/div/app-banners-campanha/section/div/div/div/div/app-banners-campanha-banner/a/figure/picture/img')
    BOTAO_CLIQUE_AQUI_E_CONFIRA_SEUS_RESULTADOS = (
    By.XPATH, '/html/body/app-root/div/ng-component/main/app-como-receber-premio/section/div/div[2]/a')

    CARD_CONFERIR_SORTEIO = (
    By.XPATH, '/html/body/app-root/div/ng-component/main/app-meus-atalhos/section/div/div/div[1]')
    CARD_MEUS_PEDIDOS = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-meus-atalhos/section/div/div/div[2]')
    CARD_MEUS_TITULOS = (By.XPATH, '/html/body/app-root/div/ng-component/main/app-meus-atalhos/section/div/div/div[3]')

    BANNER_CADASTRE_SEU_BEM_DA_SORTE_FISICO = (By.XPATH, '/html/body/app-root/div/ng-component/main/section/div/div/div/a')

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

    def verificarValorUnitarioTiutlo(self, valor):
        assert_equal(self._comandos.obterTexto(self.elemento.VALOR_UNITARIO_TITULO), valor)

    def validarOValorTotal(self, valor):
        assert_equal(self._comandos.obterTexto(self.elemento.VALOR_TOTAL), valor)

    def validarBotaoCompraDesativado(self):
        assert_false(self._comandos.elementoAtivo(self.elemento.BOTAO_COMPRAR_HOME))

    def validarBotaoCompraAtivado(self):
        assert_true(self._comandos.elementoAtivo(self.elemento.BOTAO_COMPRAR_HOME))

    def adicionarTituloCompraHome(self, qtd):
        quantidade = int(qtd)
        # evento de clicar no botao
        try:
            for clicar in range(quantidade):
                # se a quantidade maxima de clique for maior ou igual
                # verifica que o botão esteja desativado
                if clicar >= 25:
                    assert_false(self._comandos.elementoAtivo(self.elemento.BOTAO_ADICIONAR_TITULO))
                    break
                self._comandos.clicar(self.elemento.BOTAO_ADICIONAR_TITULO)
        except:
            if int(qtd) > 25:
                qtd = '25'
            # caso caia aqui verificar se os elemetos Mobile esta ativo
            select_element = self._comandos.obterElemento(self.elemento.SELECIONAR_A_QUANTIDADE_MOBILE)
            self._comandos.clicar(self.elemento.SELECIONAR_A_QUANTIDADE_MOBILE)
            select_object = Select(select_element)
            select_object.select_by_value(qtd)

    def removerTituloCompraHome(self, qtd):
        quantidade = int(qtd)
        try:

            select_element = self._comandos.obterElemento(self.elemento.SELECIONAR_A_QUANTIDADE_MOBILE)
            self._comandos.clicar(self.elemento.SELECIONAR_A_QUANTIDADE_MOBILE)
            time.sleep(0.5)
            select_object = Select(select_element)
            select_object.select_by_value("")
        except:
            # evento de clicar no botao
            for clicar in range(quantidade):
                time.sleep(0.5)
                try:
                    self._comandos.clicar(self.elemento.BOTAO_REMOVER_TITULO)
                except:
                    break

    def clicarNoBotaoMais5(self):
        try:
            self._comandos.clicar(self.elemento.BOTAO_MAIS5_TITULOS)
        except:
            if self._comandos.elementoAtivo(self.elemento.SELECIONAR_A_QUANTIDADE_MOBILE):
                pass

    def clicarNoBotaoMais10(self):
        try:
            self._comandos.clicar(self.elemento.BOTAO_MAIS10_TITULOS)
        except:
            if self._comandos.elementoAtivo(self.elemento.SELECIONAR_A_QUANTIDADE_MOBILE):
                pass

    def clicarNoBotaoLimpar(self):
        try:
            self._comandos.clicar(self.elemento.BOTAO_LIMPAR_TITULOS)
        except:
            if self._comandos.elementoAtivo(self.elemento.SELECIONAR_A_QUANTIDADE_MOBILE):
                pass

    def clicarNoBotaoComprarDaPaginaHome(self):
        self._comandos.clicar(self.elemento.BOTAO_COMPRAR_HOME)

    def verificarValorTotalPaginaCheckout(self, valor):
        assert_equal(self._comandos.obterTexto(self.elementoPaginaCheckout.VALOR_TOTAL), valor)

    def verificarSubTotalPaginaCheckout(self, valor):
        assert_equal(self._comandos.obterTexto(self.elementoPaginaCheckout.SUBTOTAL), valor)

    def clicarNoBannerVantagensDoBemDaSorte(self):
        self._comandos.clicar(self.elemento.BANNER_VANTAGENS_DO_BEM_DA_SORTE)

    def clicarNoBotaoCliqueAquiEConfiraSeusResultados(self):
        self._comandos.clicar(self.elemento.BOTAO_CLIQUE_AQUI_E_CONFIRA_SEUS_RESULTADOS)

    def clicarNoCardConferirSorteio(self):
        self._comandos.clicar(self.elemento.CARD_CONFERIR_SORTEIO)

    def clicarNoCardMeusPedidos(self):
        self._comandos.clicar(self.elemento.CARD_MEUS_PEDIDOS)

    def clicarNoCardMeusTitulos(self):
        self._comandos.clicar(self.elemento.CARD_MEUS_TITULOS)

    def clicarNoBannerCadastreSeuBemDaSorteFisico(self):
        self._comandos.clicar(self.elemento.BANNER_CADASTRE_SEU_BEM_DA_SORTE_FISICO)

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
