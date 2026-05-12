import os
import subprocess
import click 

#Este script lista todos os arquivos e diretórios de uma pasta especificada e os descarta na lixeira do sistema.
#Para implementa-lo, certifique-se primeiro de possuir os pacotes do python Click e do Trash-CLI. Após isso, programe o ciclo de descarte usando um cronjob, chamando o interpretador python seguido do endereço deste arquivo e o caminho da pasta a ser esvaziada. Ex: @weekly python ~/user/lixero.py ~/user/Downloads
#É recomendado que os caminhos do cronjob sejam descritos desde o root.

@click.command()
@click.argument("caminho")

def esvaziar_diretorio(caminho):
    """
    Lista todos os arquivos e diretórios de um caminho especificado
    e move cada item para a lixeira utilizando o comando `trash-put`.

    Parâmetros:
        caminho (str): Caminho absoluto do diretório que será esvaziado.
        Ex: python lixeiro.py /home/seu_usuário/diretorio_destino

    Observações:
        - O script depende do utilitário `trash-put` e do pacote 'click' instalado no sistema.
        - Caso o nome do arquivo contenha espaços, os espaços serão
          substituídos por hífens antes do descarte.
        - O conteúdo não é apagado permanentemente, apenas enviado
          para a lixeira do sistema.
    """                                                          # Documentação gerada pelo ChatGPT 5.5
    downloads = os.listdir(f"{caminho}")                         # Lista todos os arquivos e diretórios do caminho informado
    if len(downloads) > 0:                                       # Verifica se existem arquivos para descartar
        for i in range(len(downloads)):                          # Percorre todos os itens encontrados
            if ' ' in downloads[i]:                              # Se o nome do arquivo possuir espaços, substitui os espaços por hífens
                arquivo_ruim = f"{caminho}/{downloads[i]}"
                arquivo = arquivo_ruim.replace(" ","-")
                subprocess.run(["mv", arquivo_ruim, arquivo])    # Renomeia o arquivo antes de enviá-lo para a lixeira
            else:
                arquivo = f'{caminho}/{downloads[i]}'
            subprocess.run(["trash-put", arquivo])               # Move o arquivo/diretório para a lixeira
            
if __name__ == '__main__':
    esvaziar_diretorio()                                         # Chama a função com o caminho especificado