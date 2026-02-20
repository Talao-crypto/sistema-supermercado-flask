# Sistema de Gestão de Supermercado (Flask + MongoDB)

Projeto Full Stack desenvolvido em Python com Flask e MongoDB para gerenciamento completo de um supermercado.

O sistema permite controle de produtos, estoque, vendas, histórico e usuários com permissões diferentes (Admin e Funcionário).

---

## Funcionalidades

### Autenticação
- Login com verificação de usuário e senha
- Controle de sessão
- Permissões diferentes para Admin e Funcionário

### Gestão de Produtos
- Criar produto
- Listar produtos
- Atualizar estoque
- Atualizar preço (apenas admin)
- Remover produto (apenas admin)
- Indicador visual de estoque:
  - Esgotado
  - Estoque baixo
  - Estoque normal

### Sistema de Vendas
- Registro de venda
- Validação de estoque
- Atualização automática do estoque
- Registro de:
  - Produto
  - Quantidade
  - Vendedor
  - Data
  - Total da venda
- Histórico completo de vendas

### Gerenciamento de Usuários
- Criar usuário
- Definir tipo (Admin / Funcionário)
- Listar usuários
- Remover usuário
- Controle de acesso por tipo

---

## Tecnologias Utilizadas

- Python
- Flask
- MongoDB
- PyMongo
- HTML5
- CSS3
- Git / GitHub

---

## Estrutura do Projeto

```
projetoMercado/
│
├── app.py
├── database.py
├── produtos.py
├── vendas.py
├── gerenciar_usuarios.py
├── static/
│   └── style.css
├── templates/
│   ├── login.html
│   ├── painel_admin.html
│   ├── painel_funcionario.html
│   ├── historico.html
│   ├── usuarios.html
│   └── ...
```

---

## Como Executar o Projeto

### 1. Instalar dependências

```
pip install flask pymongo
```

### 2. Iniciar o MongoDB localmente

Certifique-se que o MongoDB está rodando em:

```
mongodb://localhost:27017/
```

### 3. Rodar a aplicação

```
python app.py
```

### 4. Acessar no navegador

```
http://127.0.0.1:5000
```

---

## Controle de Permissões

Admin:
- CRUD completo de produtos
- Alterar preços
- Gerenciar usuários
- Ver histórico e relatórios

Funcionário:
- Atualizar estoque
- Registrar vendas
- Visualizar produtos

---

## Possíveis Melhorias Futuras

- Implementação de hash de senha
- Dashboard analítico
- Testes automatizados
- Deploy em produção
- Containerização com Docker

---

## Autor

Tales Martins

Projeto desenvolvido para prática de desenvolvimento Full Stack com foco em backend, banco de dados e arquitetura de sistema web.
