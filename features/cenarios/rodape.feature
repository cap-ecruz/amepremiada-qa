@DESKTOP @CELULAR @TABLET
@rodape
Funcionalidade: navegacao no rodape

Contexto: abrir pagina do site do ame premiada
    Dado que estou em uma pagina do ame premiada

Cenario: Acesse a central de atendimento
    Quando clico no link Duvidas Frequentes
    Então valido do direcionamento para pagina faq

Esquema do Cenario: (Links) Menus rodape (<opcao>)
    navegacao entre as pagina pelo link do rodape

    Quando clico no menu do rodape '<opcao>'
    Entao verifico o direcionamento para pagina '<escolhida>'

    Exemplos:
    | opcao                         | escolhida                |
    | condicoes gerais              | condicoes gerais         |
    | termos legais                 | termos legais            |
    | termos de uso                 | termos de uso            |
    | politica de privacidade       | politica de privacidade  |
    | politica de cookies           | politica de cookies      |

#Cenario: numero da susep
#Entao valido no rodape o numero susep

Esquema do Cenario: Logomarca
    Quando clico no icone <imagem>
    Entao valido o direcionamento para pagina da <pagina>

    Exemplos:
    | imagem         | pagina    |
    | ame premiada   | home      |
    | ame            | ame       |