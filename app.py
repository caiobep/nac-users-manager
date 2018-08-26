#! /usr/bin/env python3
import os
import platform
import signal
import sys
from usuarios import criar_usuario, criar_departamento, criar_historico
from infrastructure import escrever_usuario_em_arquivo


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


def cadastrar_usuario():
    print("Olá querido usuario! Vamos cadastrar uns alunos!")
    continuar_cadastrando = True
    usuarios = []

    while continuar_cadastrando:
        usuario = criar_usuario(
            nome_completo=input("Informe o nome Completo: "),
            nome_reduzido=input("Informe o nome reduzido: "),
            cargo=input("Informe o cargo: "),
            nivel_acesso=input("Informe o nível de acesso: "),
            hora_ultimo_acesso=input("Informe a Hora do ultimo Acesso: "),
            data_ultimo_acesso=input("Informe a data do ultimo Acesso: "),

            departamento=criar_departamento(
                ramal=input("Informe o Ramal: "),
                responsavel=input("Informe o Responsável: "),
                andar=input("Informe o Andar: ")
            ),

            historico=criar_historico(
                url=input("Informe a URL: "),
                ip_origem=input("Informe o ip de origem: "),
                data=input("Informe a data: "),
                hora=input("Informe a hora:")
            )
        )
        
        # Verifique se exite algum usuario com o mesmo nome reduzido
        existe_usuario_com_mesmo_nome_reduzido = any(
            u['nome_reduzido'] == usuario['nome_reduzido'] for u in usuarios
        )

        if not existe_usuario_com_mesmo_nome_reduzido:
            usuarios.append(usuario)
        else:
            print("Usuario não cadastrado! \r\n")
            print("Já existe um usuario com este nome reduzido.")

        continuar_cadastrando = True if input(
            "Digite <S> para continar cadastrando? "
        ).upper() == "S" else False

    devo_gravar_json = True if input(
        "Digite <S> para gravar os dados no arquivo `users.json`"
    ).upper() == "S" else False

    if devo_gravar_json:
        escrever_usuario_em_arquivo(usuarios)


def consultar_nivel_acesso(usuarios):
    raise NotImplementedError


def consultar_usuarios_departamento(usuarios):
    raise NotImplementedError


def menu():
    clear_screen()
    print(bcolors.BOLD)
    print("O que podemos fazer por você hoje?")
    print(bcolors.ENDC)
    print(bcolors.HEADER)
    print("Digite <1> para cadastrar usuarios")
    print("Digite <2> para consultar usuario por nivel de acesso")
    print("Digite <3> para consultar usuarios por departamento")
    print(bcolors.ENDC)
    item_desejado = input("Informe sua resposta: ")

    modulos = {
        1: cadastrar_usuario,
        2: consultar_nivel_acesso,
        3: consultar_usuarios_departamento,
    }

    if int(item_desejado) in [1, 2, 3]:
        clear_screen()
        print(bcolors.ENDC)
        modulos.get(item_desejado)()
    else:
        print(bcolors.FAIL + "Item não encontrado \r\n \r\n")
        print(bcolors.ENDC)
        input("Pressione Qualquer tecla para continuar")
        menu()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        clear_screen()
        print("\r\n \r\n Até Mais! \r\n")
        print("De: @caiobep e <Wiliam Oliveira>")
        print("=================================")
