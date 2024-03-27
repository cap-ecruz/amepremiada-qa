@DESKTOP @CELULAR @TABLET
@barraLogado

Funcionalidade: barra de navegacao - logado

  Contexto: Efetuar o login do usuario
      Dado que eu estou na pagina Login
      E que efetue o login


  Esquema do Cenario: Navegacao submenu minha conta <opcaomenu>
      Quando clico em abrir menu de usuario
      E clico no submenu <opcaomenu> toggler
      Entao valido o direcionamento para a pagina <paginadirecionada>

  Exemplos:
  |opcaomenu           | paginadirecionada  |
  |minha conta         | minha conta        |
  |meus titulos        | meus titulos       |
  |minhas premiacoes   | minhas premiacoes  |
  |meus dados          | meus dados         |
  |sair                | inicial            |


  Esquema do Cenario: Navegacao minha conta <opcaomenu>
    Quando clico no dashboard <opcaomenu>
    Entao valido o direcionamento para a pagina <paginadirecionada>

  Exemplos:
  |opcaomenu                 | paginadirecionada       |
  |meus titulos              | meus titulos            |
  |premiacoes                | premiacoes       |
  |historico de premiacoes   | historico de premiacoes |
  |meus dados                | meus dados              |
