"""Laboratório 06: função Lambda chamada por uma HTTP API do API Gateway.

O evento chega no formato de payload 2.0 das HTTP APIs.
Autoteste local, sem AWS: python lambda_function.py
"""

import json
from datetime import datetime, timezone


def lambda_handler(event, context):
    parametros = event.get("queryStringParameters") or {}
    # O nome vem da URL, então é cortado antes de voltar na resposta.
    nome = str(parametros.get("nome", "mundo"))[:50]

    corpo = {
        "mensagem": f"Olá, {nome}! Esta resposta veio de uma função Lambda.",
        "metodo": event.get("requestContext", {}).get("http", {}).get("method"),
        "caminho": event.get("rawPath"),
        "horario_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json; charset=utf-8"},
        "body": json.dumps(corpo, ensure_ascii=False),
    }


if __name__ == "__main__":
    evento = {
        "rawPath": "/",
        "queryStringParameters": {"nome": "Ana"},
        "requestContext": {"http": {"method": "GET"}},
    }
    resposta = lambda_handler(evento, None)
    corpo = json.loads(resposta["body"])
    assert resposta["statusCode"] == 200
    assert corpo["mensagem"].startswith("Olá, Ana!"), corpo
    assert corpo["metodo"] == "GET" and corpo["caminho"] == "/", corpo

    # Evento vazio (teste pelo Console) e nome longo demais.
    assert "Olá, mundo!" in json.loads(lambda_handler({}, None)["body"])["mensagem"]
    longo = lambda_handler({"queryStringParameters": {"nome": "x" * 500}}, None)
    assert "x" * 51 not in longo["body"]

    print("ok:", resposta["body"])
