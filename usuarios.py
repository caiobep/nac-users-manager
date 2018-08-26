
def criar_departamento(nome, ramal, responsavel, andar):
    return {
      "nome": nome,
      "ramal": ramal,
      "responsavel": responsavel,
      "andar": andar
    }


def criar_historico(url, ip_origem, data, hora):
    return {
      "url": url,
      "ip_origem": ip_origem,
      "data": data,
      "hora": hora
    }


def criar_usuario(
  nome_completo,
  nome_reduzido,
  cargo,
  nivel_acesso,
  data_ultimo_acesso,
  hora_ultimo_acesso,
  departamento,
  historico
  ):

    niveis_acesso_permitidos = [
        "VISITANTE",
        "USUARIO",
        "ADMINISTRATIVO",
        "TECNICO",
        "SUPER USUARIO"]

    if not (nivel_acesso.upper() in niveis_acesso_permitidos):
        raise ValueError('Nivel de acesso desconhecido')

    return {
      "nome_completo": nome_completo,
      "nome_reduzido": nome_reduzido,
      "cargo": cargo,
      "nivel_acesso": nivel_acesso,
      "hora_ultimo_acesso": hora_ultimo_acesso,
      "data_ultimo_acesso": data_ultimo_acesso,
      "departamento": departamento,
      "historico": historico
    }
