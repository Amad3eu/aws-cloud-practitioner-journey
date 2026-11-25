"""Laboratório 05: operações básicas no DynamoDB com boto3.

Uso:
    python app.py            cria a tabela e roda gravação, leitura, consulta e exclusão
    python app.py --cleanup  apaga a tabela
"""

import sys

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

REGIAO = "us-east-1"
TABELA = "clf-c02-estudos"

dynamodb = boto3.resource("dynamodb", region_name=REGIAO)


def criar_tabela():
    try:
        dynamodb.create_table(
            TableName=TABELA,
            KeySchema=[
                {"AttributeName": "modulo", "KeyType": "HASH"},
                {"AttributeName": "aula", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "modulo", "AttributeType": "S"},
                {"AttributeName": "aula", "AttributeType": "N"},
            ],
            # Provisionado com 5/5 cabe nas 25 unidades de leitura e de escrita
            # do Free Tier sem prazo. O modo sob demanda fica fora dele.
            BillingMode="PROVISIONED",
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
            Tags=[{"Key": "projeto", "Value": "clf-c02"}],
        )
        print(f"Criando a tabela {TABELA}...")
    except ClientError as erro:
        if erro.response["Error"]["Code"] != "ResourceInUseException":
            raise
        print(f"A tabela {TABELA} já existe.")
    tabela = dynamodb.Table(TABELA)
    tabela.wait_until_exists()
    return tabela


def exercitar(tabela):
    chave = {"modulo": "mod-05", "aula": 25}

    tabela.put_item(Item={**chave, "titulo": "DynamoDB", "concluida": False})
    lido = tabela.get_item(Key=chave, ConsistentRead=True)["Item"]
    assert lido["titulo"] == "DynamoDB", lido
    print("Gravou e leu:", lido)

    tabela.update_item(
        Key=chave,
        UpdateExpression="SET concluida = :valor",
        ExpressionAttributeValues={":valor": True},
    )
    tabela.put_item(
        Item={"modulo": "mod-05", "aula": 24, "titulo": "RDS e Aurora", "concluida": True}
    )

    # A consulta usa a chave de partição e devolve os itens ordenados pela chave de ordenação.
    aulas = tabela.query(
        KeyConditionExpression=Key("modulo").eq("mod-05"), ConsistentRead=True
    )["Items"]
    assert [aula["aula"] for aula in aulas] == [24, 25], aulas
    assert all(aula["concluida"] for aula in aulas), aulas
    print("Consulta pelo módulo:", [(int(a["aula"]), a["titulo"]) for a in aulas])

    tabela.delete_item(Key={"modulo": "mod-05", "aula": 24})
    restantes = tabela.query(
        KeyConditionExpression=Key("modulo").eq("mod-05"), ConsistentRead=True
    )["Count"]
    assert restantes == 1, restantes
    print("Apagou a aula 24. Itens restantes:", restantes)


def apagar_tabela():
    tabela = dynamodb.Table(TABELA)
    try:
        tabela.delete()
    except ClientError as erro:
        if erro.response["Error"]["Code"] != "ResourceNotFoundException":
            raise
        print(f"A tabela {TABELA} não existe, nada a apagar.")
        return
    tabela.wait_until_not_exists()
    print(f"Tabela {TABELA} apagada.")


if __name__ == "__main__":
    if "--cleanup" in sys.argv:
        apagar_tabela()
    else:
        exercitar(criar_tabela())
        print("Tudo certo. Rode `python app.py --cleanup` ao terminar.")
