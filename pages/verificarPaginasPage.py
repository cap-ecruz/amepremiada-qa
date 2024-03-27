import time
from utils.comandos import Comandos
from utils.urlPage import Paginas
from nose.tools import assert_equal
from selenium.webdriver.common.by import By

class VerificarPaginas(Paginas):
    def __init__(self, webdriver):
        self._comandos = Comandos(webdriver)

    def verificarSeEstaNaPaginaLogin(self):
        self._comandos.encontrarClassePrincipal("page-login")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_LOGIN)

    def verificarSeEstaNaPaginaCadastroPasso1(self):
        self._comandos.encontrarClassePrincipal("page-cadastro")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_PASSO1)

    def verificarSeEstaNaPaginaCadastroPasso2(self):
        self._comandos.encontrarClassePrincipal("page-cadastro")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_PASSO2)

    def verificarSeEstaNaPaginaCadastroPasso3(self):
        self._comandos.encontrarClassePrincipal("page-cadastro")
        self._comandos.esperarTexto(
            (By.XPATH, '/html/body/app-root/ng-component/main/app-breadcrumb/nav/ol/li[3]/span'), 'Senha e Aceites')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_PASSO3)

    def verificarSeEstaNaMinhaConta(self):
        self._comandos.encontrarClassePrincipal("page-minha-conta.ng-tns-c11-2")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MINHA_CONTA)

    def verificarSeEstaNaPaginaInstituicaoBeneficiada(self):
        self._comandos.encontrarClassePrincipal("page-entidade.ng-tns-c118-1.ng-trigger.ng-trigger-slide")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_INSTITUICAO_BENEFICIADA)

    def verificarSeEstaNaPaginaComoComprar(self):
        self._comandos.encontrarClassePrincipal("page-como-comprar")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_COMO_COMPRAR)


    def verificarSeEstaNaPaginaResultados(self):
        self._comandos.encontrarClassePrincipal("page-resultados")
        time.sleep(1)
        assert_equal(self._comandos.capturar_url(), self.PAGINA_RESULTADOS)

    # def verificarSeEstaNaPaginaResultadosTeste(self):
        # self._comandos.encontrarClassePrincipal(self.elemento.PAGINA_RESULTADOS)
       # self._comandos.encontrarClassePrincipal("page-resultados.ng-tns-c102-1")
       #  assert_equal(self._comandos.capturar_url(), self.PAGINA_RESULTADOS)

    def verificarSeEstaNaPaginaDuvidasFrequentes(self):
        self._comandos.encontrarClassePrincipal("page-faq")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES)

    def verificarSeEstaNaPaginaFaq(self):
        self._comandos.encontrarClassePrincipal("page-faq")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES)
    def verificarSeEstaNaPaginaFaq1(self):
        self._comandos.encontrarClassePrincipal("page-faq1")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES_FAQ1)
    def verificarSeEstaNaPaginaFaq2(self):
        self._comandos.encontrarClassePrincipal("page-faq2")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_DUVIDAS_FREQUENTES_FAQ2)

    def verificarSeEstaNaPaginaMeusTitulos(self):
        self._comandos.encontrarClassePrincipal("page-meus-titulos.ng-tns-c48-5")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MEUS_TITULOS)