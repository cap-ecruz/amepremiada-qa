Para rodar o projeto é necessário ter a versão 3.11 do Python instalado em sua máquina.

## Installation
1. Clone o projeto `(https://github.com/cap-ecruz/amepremiada-qa.git)`.

2. Entre na pasta `cd amepremiada-qa` 

3. Rode o comando `pip install -r requirements.txt` para instalar as dependencias de desenvolvimento.

## Testes
Para o rodar os testes devemos rodar, no terminal o comando:
`behave` para rodar todos os scripts de teste,
`behave  --tags=@barraDeslogado` para rodar apenas um script de teste (@barraDeslogado, por exemplo) ou
`behave -f html -o behave-report.html` para rodar todos os scripts e gerar o relatório (report.html)

    

