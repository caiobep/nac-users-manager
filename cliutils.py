import os
import platform


def clear_screen():
    if (platform.system() == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printar_usuario(usuario):
    for key in usuario:
        valor = usuario[key]

        if isinstance(valor, dict):
            print(bcolors.BOLD + bcolors.OKBLUE + key.upper() + bcolors.ENDC)
            printar_usuario(valor)
        else:
            print(bcolors.ENDC + key + ": " + bcolors.OKGREEN + valor + bcolors.ENDC)

