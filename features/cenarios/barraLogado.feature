@DESKTOP @CELULAR @TABLET
@barraLogado
Funcionalidade: barra de navegacao - logado

  Contexto: Efetuar o login do usuario
    Dado que eu estou na pagina Login
    E que efetue o login
    Entao valido o direcionamento para a pagina minha conta

  Cenario: clicar no submenu minha conta
    Quando clico no submenu minha conta toggler
    Entao verifico o submenu toggler


  Esquema do Cenario: Navegacao submenu minha conta <opcaomenu>
    Quando clico no submenu minha conta toggler
    E clico no submenu <opcaomenu>
    Entao valido o direcionamento para a pagina <paginadirecionada>

  Exemplos:
  |opcaomenu           | paginadirecionada |
  |minha conta         | minha conta       |
  |meus titulos        | meus titulos      |
  |meus dados          | meus dados        |
  |sair                | home              |
