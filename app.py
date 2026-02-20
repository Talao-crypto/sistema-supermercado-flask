from flask import Flask, render_template, request, redirect, url_for, session
from database import usuarios, produtos, vendas
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supermercado_secret_key"



# LOGIN

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]

        usuario = usuarios.find_one({
            "nome": nome,
            "senha": senha
        })

        if usuario:
            session["usuario"] = usuario["nome"]
            session["tipo"] = usuario["tipo"]

            if usuario["tipo"] == "admin":
                return redirect(url_for("painel_admin"))
            else:
                return redirect(url_for("painel_funcionario"))

    return render_template("login.html")



# LOGOUT

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))



# PAINEL ADMIN

@app.route("/admin")
def painel_admin():
    if session.get("tipo") != "admin":
        return redirect(url_for("login"))

    lista = list(produtos.find())
    return render_template("painel_admin.html", produtos=lista)



# PAINEL FUNCIONÁRIO

@app.route("/funcionario")
def painel_funcionario():
    if "usuario" not in session:
        return redirect(url_for("login"))

    lista = list(produtos.find())
    return render_template("painel_funcionario.html", produtos=lista)



# CADASTRAR PRODUTO

@app.route("/cadastrar_produto", methods=["POST"])
def cadastrar_produto():

    if session.get("tipo") != "admin":
        return redirect(url_for("login"))

    produtos.insert_one({
        "nome": request.form["nome"],
        "preco": float(request.form["preco"]),
        "estoque": int(request.form["estoque"]),
        "categoria": request.form["categoria"]
    })

    return redirect(url_for("painel_admin"))



# ATUALIZAR ESTOQUE

@app.route("/atualizar_estoque/<id>", methods=["POST"])
def atualizar_estoque(id):

    novo_estoque = int(request.form["estoque"])

    produtos.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"estoque": novo_estoque}}
    )

    if session["tipo"] == "admin":
        return redirect(url_for("painel_admin"))
    else:
        return redirect(url_for("painel_funcionario"))



# ATUALIZAR PREÇO

@app.route("/atualizar_preco/<id>", methods=["POST"])
def atualizar_preco(id):

    if session.get("tipo") != "admin":
        return redirect(url_for("login"))

    novo_preco = float(request.form["preco"])

    produtos.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"preco": novo_preco}}
    )

    return redirect(url_for("painel_admin"))



# REMOVER PRODUTO

@app.route("/remover/<id>")
def remover(id):

    if session.get("tipo") != "admin":
        return redirect(url_for("login"))

    produtos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("painel_admin"))



# REGISTRAR VENDA

@app.route("/vender/<id>", methods=["POST"])
def vender(id):

    quantidade = int(request.form["quantidade"])

    if quantidade <= 0:
        return redirect(url_for("painel_admin"))

    produto = produtos.find_one({"_id": ObjectId(id)})

    if not produto or produto["estoque"] < quantidade:
        return redirect(url_for("painel_admin"))

    total = produto["preco"] * quantidade

    produtos.update_one(
        {"_id": ObjectId(id)},
        {"$inc": {"estoque": -quantidade}}
    )

    vendas.insert_one({
        "produto_id": produto["_id"],
        "produto": produto["nome"],
        "quantidade": quantidade,
        "preco_unitario": produto["preco"],
        "total": total,
        "vendedor": session["usuario"],
        "data": datetime.now()
    })

    return redirect(url_for("historico"))



# HISTÓRICO

@app.route("/historico")
def historico():

    if "usuario" not in session:
        return redirect(url_for("login"))

    lista = list(vendas.find().sort("data", -1))
    return render_template("historico.html", vendas=lista)



# GERENCIAR USUÁRIOS

@app.route("/usuarios")
def gerenciar_usuarios():

    if session.get("tipo") != "admin":
        return redirect(url_for("login"))

    lista = list(usuarios.find())
    return render_template("usuarios.html", usuarios_lista=lista)


@app.route("/criar_usuario", methods=["POST"])
def criar_usuario_web():

    if session.get("tipo") != "admin":
        return redirect(url_for("login"))

    nome = request.form["nome"]
    senha = request.form["senha"]
    tipo = request.form["tipo"].lower()

    if not usuarios.find_one({"nome": nome}):
        usuarios.insert_one({
            "nome": nome,
            "senha": senha,
            "tipo": tipo
        })

    return redirect(url_for("gerenciar_usuarios"))


@app.route("/remover_usuario/<id>")
def remover_usuario_web(id):

    if session.get("tipo") != "admin":
        return redirect(url_for("login"))

    usuarios.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("gerenciar_usuarios"))


if __name__ == "__main__":
    app.run(debug=True)
