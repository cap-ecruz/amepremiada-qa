import os


def main():
    # os.system('behave --tags=@DESKTOP -f html -o Testevidencia.html')
    # os.system('behave --tags=@CELULAR -f html -o evidenciaMobile.html'
    # os.system('behave --tags=@TABLET -f html -o evidenciaMobile.html')
    # os.system('behave --tags=@testeTi -f html -o evidenciaTesteCadastro1.html')
    os.system('behave -f html -o evidenciaTesteCadastro.html')


if __name__ == '__main__':
    main()
