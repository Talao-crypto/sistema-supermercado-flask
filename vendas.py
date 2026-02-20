# gerenciar vendas e estoque dos produtos

'''
Pedir nome do produto

Pedir quantidade

Verificar estoque

Diminuir estoque

Registrar venda

Mostrar total pago

'''

from database import produtos, vendas
from datetime import datetime



def registrar_vendas(usuario_logado):

    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))

    produto = produtos.find_one({"nome": nome})

    if not produto:
        print("Produto não encontrado.")
        return

    if quantidade <= 0:
        print("Quantidade inválida.")
        return

    if produto["estoque"] < quantidade:
        print("Estoque insuficiente.")
        return

    total = produto["preco"] * quantidade

    #  Atualiza estoque
    produtos.update_one(
        {"nome": nome},
        {"$inc": {"estoque": -quantidade}}
    )

    #  Registra venda
    venda = {
        "produto": nome,
        "quantidade": quantidade,
        "preco_unitario": produto["preco"],
        "total": total,
        "vendedor": usuario_logado["nome"],
        "data": datetime.now()
    }

    vendas.insert_one(venda)

    print(f"Venda realizada com sucesso! Total: R${total:.2f}")
