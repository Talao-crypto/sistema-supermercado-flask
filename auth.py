from database import usuarios

def login():
    nome = input("Usuário: ")
    senha = input("Senha: ")

    usuario = usuarios.find_one({
        "nome": nome,
        "senha": senha
    })

    if usuario:
        print(f"\nBem vindo, {usuario['nome']} ({usuario['tipo']})")
        return usuario
    else:
        print("Login inválido.")
        return None
