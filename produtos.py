from database import produtos


#cores
VERMELHO = "\033[31m"
AMARELO = "\033[33m"
VERDE = "\033[32m"
RESET = "\033[0m"


# 1 - CADASTRAR PRODUTO

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque inicial: "))
    categoria = input("Categoria: ")

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
        "categoria": categoria
    }

    produtos.insert_one(produto)
    print("Produto cadastrado com sucesso!")



# 2 - LISTAR PRODUTOS

def listar_produtos():
    lista = list(produtos.find())

    if not lista:
        print("Nenhum produto cadastrado.")
        return

    print("\n=== PRODUTOS ===")

    for p in lista:

        estoque = p["estoque"]

        # Definindo cor baseada no estoque
        if estoque == 0:
            cor = VERMELHO
            status = "ESGOTADO"
        elif estoque < 10:
            cor = AMARELO
            status = "ESTOQUE BAIXO"
        else:
            cor = VERDE
            status = "OK"

        print(
            f"Nome: {p['nome']} | "
            f"Preço: R${p['preco']:.2f} | "
            f"Estoque: {cor}{estoque}{RESET} | "
            f"Status: {cor}{status}{RESET} | "
            f"Categoria: {p['categoria']}"
        )




# 3 - ATUALIZAR ESTOQUE

def atualizar_estoque():
    nome = input("Nome do produto: ")
    novo_estoque = int(input("Novo estoque: "))

    resultado = produtos.update_one(
        {"nome": nome},
        {"$set": {"estoque": novo_estoque}}
    )

    if resultado.matched_count:
        print("Estoque atualizado com sucesso.")
    else:
        print("Produto não encontrado.")



# 4 - ATUALIZAR PREÇO (ADMIN)

def atualizar_preco(usuario_logado):

    if usuario_logado["tipo"] != "admin":
        print("Apenas admin pode alterar preço.")
        return

    nome = input("Nome do produto: ")
    novo_preco = float(input("Novo preço: "))

    resultado = produtos.update_one(
        {"nome": nome},
        {"$set": {"preco": novo_preco}}
    )

    if resultado.matched_count:
        print("Preço atualizado com sucesso.")
    else:
        print("Produto não encontrado.")



# 5 - REMOVER PRODUTO (ADMIN)

def remover_produto(usuario_logado):

    if usuario_logado["tipo"] != "admin":
        print("Apenas admin pode remover produtos.")
        return

    nome = input("Nome do produto para remover: ")

    resultado = produtos.delete_one({"nome": nome})

    if resultado.deleted_count:
        print("Produto removido com sucesso.")
    else:
        print("Produto não encontrado.")



# 6 - RELATÓRIO (ADMIN)

def relatorio(usuario_logado):

    if usuario_logado["tipo"] != "admin":
        print("Apenas admin pode acessar relatórios.")
        return

    lista = list(produtos.find())

    if not lista:
        print("Nenhum produto cadastrado.")
        return

    total_produtos = len(lista)
    valor_total = sum(p["preco"] * p["estoque"] for p in lista)
    menor_estoque = min(lista, key=lambda x: x["estoque"])

    print("\n=== RELATÓRIO ===")
    print(f"Total de produtos cadastrados: {total_produtos}")
    print(f"Valor total em estoque: R${valor_total:.2f}")
    print(f"Produto com menor estoque: {menor_estoque['nome']} "
          f"({menor_estoque['estoque']} unidades)")
