@DESKTOP @CELULAR @TABLET
#@vertitulo

Funcionalidade: Visualizar Titulos

  Contexto: verificar se o usuario tem titulos da campanha atual
    Dado que eu estou na pagina Login
    E que efetue o login

@vertitulo
  Cenario: visualizar Titulo 
    E clique em acessar meus titulos
    # E verifique que o usuario tenha titulos da campanha atual

    # Quando ao clicar no botao ver titulos
    # E ao clicar no botao abrir titulo
    # E verifique o breadcrumb e o mesmo titulo selecionado
    # E verifique o nome da campanha no header do titulo
    # E verifique se o documento Condições gerais é exibido

  Cenario: raspagem automatica do titulo
    E ao clicar no botao raspar automaticamente
    E verifique que o botao foi desabilitado
    E ao clicar no botão Numeros da sorte
    Então verifique que é exibido os numeros das rodadas

  Cenario: visualizar rodadas premiadas
    E ao clicar no conferir sorteio
    E verifique que o redirecionamento para seção de sorteios
    Então verifique que é exibido os numeros dos sorteios