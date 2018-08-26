#! /usr/bin/env python3

from usuarios import criar_usuario, criar_departamento, criar_historico
from json-parser import escrever_usuario_em_arquivo


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

        usuarios.append(usuario)
        continuar_cadastrando = True if input(
            "Digite <S> para continar cadastrando? "
        ).upper() == "S" else False
 
    devo_gravar_json = True if input(
        "Digite <S> para gravar os dados no arquivo `users.json`"
    ).upper() == "S" else False
    
    if devo_gravar_json:
        escrever_usuario_em_arquivo(usuarios)


def menu():
    print("O que podemos fazer por você hoje?")
    print("Digite <1> para cadastrar usuarios")
    print("Digite <2> para consultar usuario por nivel de acesso")
    print("Digite <3> para consultar usuarios por departamento")
    item_desejado = input("Informe sua resposta: ")

    modulos = {
        1: cadastrar_usuario,
        2: consultar_nivel_acesso,
        3: consultar_usuarios_departamento,
    }

    modulos


if __name__ == "__main__":
    cadastrar_usuario()
