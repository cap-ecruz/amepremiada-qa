import time
from selenium.webdriver.common.by import By
from pages.verificarPaginasPage import VerificarPaginas
from utils.utils import Utils as info
from nose.tools import assert_equal, assert_true


class MeusPedidosElementos(object):
    BOTAO_ENTENDI_POLITICA_COOKIES = (By.XPATH, '/html/body/div[1]/div/a')

    BOTAO_MOSTRAR_DETALHES = (By.XPATH, '/html/body/app-root/ng-component/main/section/div/div/div['
                                        '1]/app-pedidos-lista/ul/li[1]/div/div/div[2]/div[2]/a[2]')
    TIPO_DE_PEDIDO = (By.ID, 'pedidoTipo')
    VALOR_PAGO = (By.ID, 'pedidoValor')
    STATUS = (By.ID, 'pedidoStatus')
    QUANTIDADE = (By.ID, 'pedidoQuantidade')
    TOTAL_DA_COMPRA = (By.ID, 'pedidoTotal')
    STEP_TIMELINE_PEDIDO_RECEBIDO = (By.CSS_SELECTOR, 'div.step:nth-child(2) > span:nth-child(1)')
    STEP_TIMELINE_PAGAMENTO_APROVADO = (By.CSS_SELECTOR, 'div.step:nth-child(3) > span:nth-child(1)')
    STEP_TIMELINE_TITULOS_ENTREGUES = (By.CSS_SELECTOR, 'div.step:nth-child(4) > span:nth-child(1)')

    LISTA_TITULOS_CAMPANHA = (By.ID, 'tituloCampanha')
    LISTA_TITULOS_TITULO = (By.XPATH, '//td[@id="tituloNumero"]')
    LISTA_TITULOS_VALOR = (By.ID, 'tituloValor')


class MeusPedidosPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = MeusPedidosElementos()

    def paginaMeusPedidos(self):
        self._comandos.navegar(self.PAGINA_MEUS_PEDIDOS)

    def clicarNoBotaoEntendiPoliticaDeCookies(self):
        self._comandos.clicar(self.elemento.BOTAO_ENTENDI_POLITICA_COOKIES)
        time.sleep(0.5)

    def clicarNoBotaoMostrarDetalhes(self):
        self._comandos.clicar(self.elemento.BOTAO_MOSTRAR_DETALHES)

    def verificarTipoDePedido(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.TIPO_DE_PEDIDO), msg)

    def verificarValorDoPedido(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.VALOR_PAGO), msg)

    def verificarStatus(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.STATUS), msg)

    def verificarQuantidade(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.QUANTIDADE), msg)

    def verificarValorTotalDaCompra(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.TOTAL_DA_COMPRA), msg)

    def verificarStepTimeLinePedidoRecebido(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.STEP_TIMELINE_PEDIDO_RECEBIDO), msg)

    def verificarStepTimeLinePagamentoAprovado(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.STEP_TIMELINE_PAGAMENTO_APROVADO), msg)

    def verificarStepTimeLineTitulosEntregues(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.STEP_TIMELINE_TITULOS_ENTREGUES), msg)

    def verificarCampanhaAtualNaPaginaMeusPedidos(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.LISTA_TITULOS_CAMPANHA), msg)

    def armazenarNumeroDoTitulo(self):
        titulo = self._comandos.obterTexto(self.elemento.LISTA_TITULOS_TITULO)
        info.NUMERO_DO_TITULO = '{}.{}.{}'.format(titulo[:-6], titulo[-6:-3], titulo[-3:])

    def verificarDoValorDoTituloNovo(self):
        assert_true(self.elemento.LISTA_TITULOS_VALOR, info.VALOR_TITULO)
