@DESKTOP @CELULAR @TABLET
@homeLogado
Funcionalidade: Home - logado

  Contexto: Abrir pagina home
    Dado que eu estou na pagina Login
    E que efetue o login
    Entao valido o direcionamento para a pagina minha conta
    Dado que eu estou na pagina home
    Entao valido o direcionamento para a pagina home

  Cenario: Mensagem de cookie
    Entao verifico a exibicao da mensagem de cookie Utilizamos cookies para analisar o uso do nosso site, direcionar conteúdos e oferecer ótima experiência para você. Para maiores informações consulte nossa POLÍTICA DE PRIVACIDADE, ou para seguir, declare estar ciente.

  Cenario: Link Politica privacidade
    Quando ao clicar no link Politica de privacidade
    Entao verifica o direcionamento para pagina Politica de Privacidade

  Cenario: Clicar no botao da banner principal
    Quando ao clicar no botao do banner principal
    Entao valido o direcionamento para a pagina compra do produto

  Cenario: clicar no banner vantagens do ame premiada
    Quando ao clicar no banner vantagens do ame premiada
    Entao valido o direcionamento para a pagina compra do produto

  Cenario: premiacao sem complicacao - pagina resultados logado
    Quando ao clicar no botao clique aqui e confira seus resultados
    Entao valido o direcionamento para pagina resultados

  Esquema do Cenario: meus atalhos logado- <opcaoatalho>
    Quando ao clicar no card <opcaoatalho>
    Entao valido o direcionamento para a pagina <paginadirecionada>

  Exemplos:
  |opcaoatalho              |paginadirecionada          |
  |conferir sorteios        |resultados                 |
  |meus pedidos             |meus pedidos               |
  |meus titulos             |meus titulos               |


  Cenario: clicar o botao veja mais sobre a fundacao abrinq
    Quando ao clicar no botao veja mais sobre a fundacao abrinq
    Entao valido o direcionamento para a pagina Instituicao beneficiada

  Esquema do Cenario: Secao tem alguma duvida acesse nossa faq - <linkfaq>
    Quando ao clicar <linkfaq>
    Entao valido o direcionamento para pagina <paginadirecionada>

  Exemplos:
  |linkfaq                        |paginadirecionada         |
  |ler mais 1                     |faq1                      |
  |ler mais 2                     |faq2                      |
  |ver mais duvidas frequentes    |faq                       |




