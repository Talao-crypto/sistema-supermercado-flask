from database import usuarios

from database import usuarios


def criar_usuario():
    nome = input("Nome: ")
    senha = input("Senha: ")
    tipo = input("Admin / Funcionário: ").lower()

    if usuarios.find_one({"nome": nome}):
        print("Usuário já existe.")
        return

    usuario = {
        "nome": nome,
        "senha": senha,
        "tipo": tipo
    }

    usuarios.insert_one(usuario)
    print("Usuário criado com sucesso.")


def listar_usuarios():
    lista = list(usuarios.find())

    if not lista:
        print("Nenhum Usuário Cadastrado. ")
        return
    
    print("===USUÁRIOS===")
    for u in lista:
        print(f"Nome: {u['nome']} | Tipo: {u['tipo']}")

    

def remover_usuario():
    nome = input("Nome: ")

    resultado = usuarios.delete_one({"nome": nome})

    if resultado.deleted_count:
        print("Deletado com sucesso. ")
    else:
        print("usuario não encontrado")

def menu():
    while True:
        print("\n=== GERENCIAR USUÁRIOS ===")
        print("1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Remover usuário")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            remover_usuario()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()