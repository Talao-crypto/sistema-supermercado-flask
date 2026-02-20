import produtos
from auth import login
import vendas



# MENU ADMIN

def menu_admin(usuario):

    opcoes = {
        "1": produtos.cadastrar_produto,
        "2": produtos.listar_produtos,
        "3": produtos.atualizar_estoque,
        "4": lambda: produtos.atualizar_preco(usuario),
        "5": lambda: produtos.remover_produto(usuario),
        "6": lambda: produtos.relatorio(usuario),
        "7": lambda: vendas.registrar_vendas(usuario),
    }

    while True:
        print("\n=== PAINEL ADMIN ===")
        print("1 - Criar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar estoque")
        print("4 - Atualizar preço")
        print("5 - Remover produto")
        print("6 - Relatório")
        print("7 - VENDER")
        print("8 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "8":
            print("Saindo do painel admin...")
            break

        acao = opcoes.get(escolha)

        if acao:
            acao()
        else:
            print("Opção inválida.")



# MENU FUNCIONÁRIO

def menu_funcionario(usuario):

    opcoes = {
        "1": produtos.listar_produtos,
        "2": produtos.atualizar_estoque,
        "3": lambda: vendas.registrar_venda(usuario),
    }

    while True:
        print("\n=== PAINEL FUNCIONÁRIO ===")
        print("1 - Listar produtos")
        print("2 - Atualizar estoque")
        print("3 - VENDER")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "4":
            print("Saindo...")
            break

        acao = opcoes.get(escolha)

        if acao:
            acao()
        else:
            print("Opção inválida.")



def main():
    usuario_logado = login()

    if not usuario_logado:
        return

    if usuario_logado["tipo"] == "admin":
        menu_admin(usuario_logado)
    else:
        menu_funcionario(usuario_logado)



if __name__ == "__main__":
    main()
