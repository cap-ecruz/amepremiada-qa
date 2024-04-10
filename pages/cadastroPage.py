import time
import json
import requests
from selenium.webdriver.common.by import By
from pages.verificarPaginasPage import VerificarPaginas
from nose.tools import assert_equal, assert_true

class CadastroElementos(object):
    BREADCRUMB_3 = (By.XPATH, '/html/body/app-root/ng-component/main/app-breadcrumb/nav/ol/li[3]/span')
    BOTAO_ENTENDI_POLITICA_COOKIES = (By.XPATH, '/html/body/div[1]/div/a')
    MENSAGEM_MODAL = (By.ID, 'swal2-content')

    # passo 1
    # PPE_NAO = (By.ID, "flPpeNao")
    PPE_SIM = (By.ID, "flPpeSim")
    PPE_NAO = (By.CSS_SELECTOR, ".custom-control")
    #'/html/body/app-root/ng-component/main/section/div/app-dados-pessoais/form/fieldset/div/label[2]')
    # BOTAO_DADOS_PESSOAIS = (By.XPATH, "/html/body/app-root/ng-component/main/section/div/app-dados-contato/div[1]/a")
    # BOTAO_DADOS_PESSOAIS = (By.XPATH, "/html/body/app-root/ng-component/main/section/div/app-dados-contato/div[1]/a/h5")
    BOTAO_PROXIMO_PASSO = (By.ID, "flCadastrar")
    BOTAO_PROXIMO_PASSO_FINALIZAR = (By.ID, "flFinalizar")

    NOME = (By.ID, "flNome")
    CPF = (By.ID, "cpf")
    NASCIMENTO = (By.ID, 'nascimento')
    CEP = (By.ID, "flCep")
    NUMERO_ENDERECO = (By.ID, "flNumero")
    COMPLEMENTO = (By.ID, "flComplemento")
    ENDERECO = (By.ID, "flEndereco")
    BAIRRO = (By.ID, "flBairro")
    CIDADE = (By.ID, "flCidade")
    ESTADO = (By.ID, "flEstado")

    # LINK_FACA_LOGIN = (By.XPATH, "/html/body/app-root/ng-component/main/section/div/app-dados-pessoais/form/div[7]/p/a")

    # passo 2
    #BOTAO_DADOS_DE_CONTATO = (By.XPATH, "/html/body/app-root/ng-component/main/section/div/app-dados-pessoais/div/a[1]/h5")
    EMAIL = (By.ID, "flEmail")
    CONF_EMAIL = (By.ID, "flEmailConfirm")
    TELEFONE_DDD = (By.ID, "flCelularDDD")
    TELEFONE_PRINCIPAL = (By.ID, "flCelular")
    SENHA = (By.ID, "flSenha")
    CONF_SENHA = (By.ID, "flSenhaConfirm")
    USO_DE_DADOS = (By.ID, "flReceberComunicado")
    BOTAO_PROXIMO_PASSO_DOIS = (By.ID, 'flCadastroSenhaAceites')

    # passo 3
    CONFIRMAR_PASSO_TRES = (By.CLASS_NAME, 'text-center')
    CODIGO1 = (By.ID, 'flCode1')
    CODIGO2 = (By.ID, 'flCode2')
    CODIGO3 = (By.ID, 'flCode3')
    CODIGO4 = (By.ID, 'flCode4')

    BOTAO_SENHA_E_ACEITES = (
        By.XPATH, "/html/body/app-root/ng-component/main/section/div/app-dados-pessoais/div/a[2]/h5")

    USO_DE_DADOS_OPCAO_NAO = (By.XPATH, '/html/body/app-root/ng-component/main/section/div/app-senha-aceites/form'
                                        '/fieldset/div/label[1]')

    BOTAO_MODAL = (By.XPATH, "/html/body/div/div/div[3]/button[1]")
    MODAL_USO_DE_DADOS = (By.XPATH, "/html/body/div/div")
    TEXTO_USO_DE_DADOS = (By.XPATH, '//*[@id="swal2-content"]/div[2]')
    TEXTO_MODAL = (By.ID, 'swal2-title')
    LINK_CADASTRAR_NOVO_EMAIL = (
        By.XPATH, '/html/body/app-root/ng-component/main/section/div/app-form-confirmar/form/div[4]/p[2]/span[2]/a')
    BOTAO_TROCAR_EMAIL = (By.ID, 'flTrocarEmail')
    CAMPO_CADASTRAR_NOVO_EMAIL = (By.CSS_SELECTOR, '.swal2-input')
    BOTAO_OK_CADASTRAR_NOVO_EMAIL = (By.CSS_SELECTOR, '.swal2-confirm')
    CAMPO_CONFIRMAR_CADASTRO = (By.XPATH, '/html/body/app-root/ng-component/main/section/div/app-form-confirmar/form'
                                          '/div[2]/app-code-input/form/div/input[1]')
    BOTAO_CONFIRMAR_CADASTRO = (By.ID, 'flConfirmar')

class CadastroPage(VerificarPaginas):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.elemento = CadastroElementos()

    def paginaCadastroPasso1(self):
        self._comandos.navegar(self.PAGINA_CADASTRO_PASSO1)

    def clicarNoBotaoEntendiPoliticaDeCookies(self):
        self._comandos.clicar(self.elemento.BOTAO_ENTENDI_POLITICA_COOKIES)
        time.sleep(0.5)

    def inserirCPF(self, cpf):
        self._comandos.inserirDado(self.elemento.CPF, cpf)

    def inserirNome(self, nome):
        self._comandos.inserirDado(self.elemento.NOME, nome)

    def inserirData(self, data):
        self._comandos.inserirDado(self.elemento.NASCIMENTO, data)

    def clicarEmNaoPPE(self):
        self._comandos.clicar(self.elemento.PPE_NAO)

    def verificarBotaoProximoPasso1Ativo(self):
        time.sleep(1.5)
        assert_true(self._comandos.elementoAtivo(self.elemento.BOTAO_PROXIMO_PASSO))

    def verificarBotaoProximoPasso2Ativo(self):
        time.sleep(1.5)
        assert_true(self._comandos.elementoAtivo(self.elemento.BOTAO_PROXIMO_PASSO_DOIS))

    def verificarBotaoFinalizarCadastroEstaAtivo(self):
        time.sleep(1.5)
        assert_true(self._comandos.elementoAtivo(self.elemento.BOTAO_PROXIMO_PASSO_FINALIZAR))

    def clicarNoBotaoProximoPasso(self):
        self._comandos.clicar(self.elemento.BOTAO_PROXIMO_PASSO)

    def verificarSeEstaNaPaginaCastroPasso2(self):
        assert_true(self._comandos.elementoAtivo(self.elemento.EMAIL))

    def clicarNoBotaoFinalizarCadastro(self):
        self._comandos.clicar(self.elemento.BOTAO_PROXIMO_PASSO_FINALIZAR)

    def inserirDDD(self, dado):
        self._comandos.inserirDado(self.elemento.TELEFONE_DDD, dado)

    def inserirTelefone(self, dado):
        self._comandos.inserirDado(self.elemento.TELEFONE_PRINCIPAL, dado)

    def inserirEmail(self, dado):
        self._comandos.inserirDado(self.elemento.EMAIL, dado)

    def inserirConfirmeEmail(self, dado):
        self._comandos.inserirDado(self.elemento.CONF_EMAIL, dado)

    def inserirCEP(self, dado):
        self._comandos.inserirDado(self.elemento.CEP, dado)

    def inserirNumeroEndereco(self, dado):
        self._comandos.inserirDado(self.elemento.NUMERO_ENDERECO, dado)

    def inserirComplemento(self, dado):
        self._comandos.inserirDado(self.elemento.COMPLEMENTO, dado)

    def inserirSenha(self, dado):
        self._comandos.inserirDado(self.elemento.SENHA, dado)

    def inserirConfSenha(self, dado):
        self._comandos.inserirDado(self.elemento.CONF_SENHA, dado)

    def clicarNoBotaoNaoAutorizoOUsoDosDados(self):
        self._comandos.clicar(self.elemento.PPE_NAO)

    def clicarNoBotaoProximoPasso2(self):
        self._comandos.clicar(self.elemento.BOTAO_PROXIMO_PASSO_DOIS)

    def verificarSeEstaNaPaginaCastroPasso3(self):
        assert_true(self._comandos.elementoAtivo(self.elemento.CONFIRMAR_PASSO_TRES))

    def tabEmail(self):
        self._comandos.apertarTAB(self.elemento.CODIGO4)

    def clicarNoLinkCadastrarUmNovoEmail(self):
        self._comandos.scrolAteElemento(self.elemento.EMAIL)
        time.sleep(10)
        # self._comandos.clicar(self.elemento.EMAIL)

    def inserirUmNovoEmail(self, dado):
        self._comandos.inserirDado(self.elemento.EMAIL, dado)
        self._comandos.clicar(self.elemento.BOTAO_TROCAR_EMAIL)

    def validaModalSucesso(self):
        assert_equal(self._comandos.obterTexto(self.elemento.TEXTO_MODAL), 'Sucesso')
        self._comandos.clicar(self.elemento.BOTAO_OK_CADASTRAR_NOVO_EMAIL)

    def inserirCodigoDeAtivacao(self, cpf):
        #r = requests.get \
          #  ("https://staging.amepremiada.com.br/api/manutencao/cliente/chave-ativacao/" + cpf,
         #   headers={"X-Token": "9F8FE311-0A1A-4A4B-93CB-13C81FCB3937"})

        #todos = json.loads(r.content)
        #todos['chave']
        self._comandos.inserirDado(self.elemento.CODIGO1, 1111)

    def clicarNoBotaoDeConfirmarCadastro(self):
        self._comandos.clicar(self.elemento.BOTAO_CONFIRMAR_CADASTRO)

    def verificarMensagemNoModal(self, msg):
        assert_equal(self._comandos.obterTexto(self.elemento.MENSAGEM_MODAL), msg)
