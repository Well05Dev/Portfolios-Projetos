# BIBLIOTECAS
from mailbox import linesep
import os 
import sys 
import subprocess
import random

# Chave de repetição
debug = True

# Início
print (f"{os.linesep}Você quer jogar o dado?")
resp = input(f"digite 'sim' ou 'não'{os.linesep} {os.linesep}")

# Resposta
if debug == True:

    # Se a resposta for sim, ele joga o dado e termina o codigo
    if (resp == "sim") or (resp == "Sim") or (resp == "SIM") :
        print(f"O resultado do dado é {random.randint(1,6)}")

    # Se a resposta for não, ele dá carão e termina o codigo
    elif (resp == "nao") or (resp == "Nao") or (resp == "Nâo") or (resp == "não") or (resp == "NAO") or (resp == "NÂO"):
        print("Oxi, abriu isso por que então?")

    # Se não responder sim ou não, ele repete o código e dá um carão
    else:
        debug = False

        if debug == False:
            print(f"{os.linesep}DIGITE APENAS 'SIM' OU 'NAO'. {os.linesep}########################################################{os.linesep}")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
            sys.argv[1:])