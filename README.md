# script-da-lovelace

Este repositório contém alguns scripts de automação da minha máquina que eu acredito que sejam interessantes serem públicos.

A documentação de como utiliza-los está disponível dentro do próprio script. 

## Lista de scripts:
### - lixeiro.py: 
script para esvaziar pastas que lotam muito fácil, como a pasta Downloads, mandando os arquivos para a lixeira. Para implementa-lo, certifique-se primeiro de possuir os pacotes do python Click e do Trash-CLI. Após isso, programe o ciclo de descarte usando um cronjob, chamando o interpretador python seguido do endereço deste arquivo e o caminho da pasta a ser esvaziada. Ex: @weekly python ~/user/lixero.py ~/user/Downloads (é recomendado que os caminhos do cronjob sejam descritos desde o root).