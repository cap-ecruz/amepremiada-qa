@DESKTOP @CELULAR @TABLET
@barraDeslogado

Funcionalidade: barra de navegacao - deslogado

  Contexto: Navegacao sem login
    Dado que estou na home

  #Cenario: barra de navegacao - Logo ame premiada
    #Quando clico na logo
    #E valido o direcionamento para pagina home


  Esquema do Cenario: barra de navegacao <opcaomenu>
    Quando clico no menu <opcaomenu>
    Entao valido o direcionamento para a pagina <paginadirecionada>

  Exemplos:
  |opcaomenu                |paginadirecionada          |
  |resultados               |resultados                 |
  |instituicao              |instituicao                |
  |comprar titulo           |comprar titulo             |
#  |user login               |login                      |
  |logo                     |home                       |

