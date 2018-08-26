#! /usr/bin/env python3

from usuarios import criar_usuario, criar_departamento, criar_historico
from cliutils import clear_screen, bcolors, printar_usuario
from infrastructure import escrever_usuario_em_arquivo
from infrastructure import importar_usuarios_do_arquivo


def cadastrar_usuario():
    continuar_cadastrando = True
    usuarios = []

    while continuar_cadastrando:
        clear_screen()
        print("Cadastro de usuarios")
        quantidade_de_usuarios_cadastrados = len(usuarios)
        if (quantidade_de_usuarios_cadastrados > 1):
            print(str(quantidade_de_usuarios_cadastrados) + " já cadastrados.")

        print("=====================")

        usuario = criar_usuario(
            nome_completo=input("Informe o nome Completo: "),
            nome_reduzido=input("Informe o nome reduzido: ").upper(),
            cargo=input("Informe o cargo: "),
            nivel_acesso=input("Informe o nível de acesso: "),
            hora_ultimo_acesso=input("Informe a Hora do ultimo Acesso: "),
            data_ultimo_acesso=input("Informe a data do ultimo Acesso: "),

            departamento=criar_departamento(
                nome=input("Informe o nome do departamento: "),
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
            print(bcolors.FAIL)
            print("Já existe um usuario com este nome reduzido.")
            print("\r\nUsuário não cadastrado!")
            print(bcolors.ENDC)

        continuar_cadastrando = True if input(
            "Digite <S> para continar cadastrando?: "
        ).upper() == "S" else False

    devo_gravar_json = True if input(
        "Digite <S> para gravar os dados no arquivo `users.json`: "
    ).upper() == "S" else False

    if devo_gravar_json:
        escrever_usuario_em_arquivo(usuarios)


def consultar_nivel_acesso():
    print("Consulta por nível de acesso")
    print("=====================")
    nivel_de_acesso = input("Informe o nível de acesso: ").upper()
    usuarios = importar_usuarios_do_arquivo()

    usuarios_desejados = filter(
        lambda x: x['nivel_acesso'].upper() == nivel_de_acesso.upper(),
        usuarios
    )

    for usuario in list(usuarios_desejados):
        print(bcolors.OKBLUE + bcolors.BOLD)
        print("USUARIO" + bcolors.ENDC)
        printar_usuario(usuario)


def consultar_usuarios_departamento():
    print("Consulta por departamento")
    print("=====================")
    departamento = input("Informe o nome do departamento: ").upper()
    usuarios = importar_usuarios_do_arquivo()

    usuarios_desejados = filter(
        lambda x: x['departamento']['nome'].upper() == departamento.upper(),
        usuarios
    )

    for usuario in list(usuarios_desejados):
        print(bcolors.HEADER + bcolors.BOLD)
        print("Usuario")
        printar_usuario(usuario)


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
        modulos[int(item_desejado)]()
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
        print("=================================")
        print("           Até Mais!        \r\n")
        print("De: @caiobep e @willrof")
        print("=================================")
