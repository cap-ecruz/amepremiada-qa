from utils.comandos import Comandos
from utils.urlPage import Paginas
from nose.tools import assert_equal
from selenium.webdriver.common.by import By


class VerificarPaginas(Paginas):
    def __init__(self, webdriver):
        self._comandos = Comandos(webdriver)

    def verificarSeEstaNaPaginaLogin(self):
        self._comandos.encontrarClassePrincipal("login-page")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_LOGIN)

    def verificarSeEstaNaPaginaCadastroPasso2(self):
        self._comandos.encontrarClassePrincipal("cadastro-page")
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_PASSO2)

    def verificarSeEstaNaPaginaCadastroPasso3(self):
        self._comandos.encontrarClassePrincipal("cadastro-page")
        self._comandos.esperarTexto(
            (By.XPATH, '/html/body/app-root/ng-component/main/app-breadcrumb/nav/ol/li[3]/span'), 'Senha e Aceites')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_CADASTRO_PASSO3)

    def verificarSeEstaNaMinhaConta(self):
        self._comandos.encontrarClassePrincipal('minha-conta')
        assert_equal(self._comandos.capturar_url(), self.PAGINA_MINHA_CONTA)

    def verificarSeEstaNaPagamento(self):
        self._comandos.encontrarClassePrincipal('checkout-page')
        self._comandos.esperar_elemento((By.XPATH, '/html/body/app-root/ng-component/main/div/div['
                                                   '1]/app-checkout-formas-pagamento/div'))
        assert_equal(self._comandos.capturar_url(), self.PAGINA_COMPRA_PAGAMENTO)

    def verificarSeEstaNaConfirmacaoCompra(self):
        self._comandos.encontrarClassePrincipal('checkout-page')
        self._comandos.esperar_elemento((By.XPATH, '/html/body/app-root/ng-component/main/div/div['
                                                   '1]/app-checkout-pedido-status/div'))
        assert_equal(self._comandos.capturar_url(), self.PAGINA_COMPRA_CONFIRMACAO)
