@DESKTOP @CELULAR @TABLET
@cadastro
Funcionalidade: Cadastrar usuario novo

  Contexto: abrir na pagina cadastro passo1
        Dado que estou na pagina cadastro passo1

  Cenario: cadastrar usuario com dados validos
        Quando E preencho o campo nome com dados Teste da Silva
        E preencho o campo cpf na pagina login com usuario novo
        E preencho o campo data de nascimento com dados 01012000
        E preencho o campo cep com 01513010
        E preencho o campo numero com 4000
        E preencho o campo complemento com não tem complemento
        E clico em não no botao Você é uma pessoa politicamente exposta?
        E verifico que o botao proximo passo esteja habilitado
        E clico no botao proximo passo
              
        E valido o direcionamento para pagina cadastro passo2
        E preencho o campo email valido
        E preencho o campo confirme o seu email valido
        E preencho o DDD com dados 11
        E preencho o telefone valido com dados 940028922
        E preencho o campo senha com dados valido
        E preencho o campo confirme a sua senha com dados valido
        E clico na opcao autorizar receber as comunicações
        E verifico que o botao proximo passo esteja habilitado
        E clico no botao proximo passo

        E valido o direcionamento para pagina cadastro passo3
        E clico no campo trocar e-mail e reenviar código
        E ao inserir um email novo
        E ao inserir o codigo de ativacao
        E ao clicar no botao de confirmar cadastro
        Entao verifique o modal com o texto O seu cadastro foi completado com sucesso!

