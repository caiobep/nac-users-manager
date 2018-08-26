import json


def escrever_usuario_em_arquivo(dado):
    with open("users.json", "w") as outfile:
        json.dump(dado, outfile)

def importar_usuarios_do_arquivo():
    with open("users.json", "r") as usuarios:
        return json.read(usuarios)