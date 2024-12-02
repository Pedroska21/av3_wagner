from servicos.cliente_servicos import adicionar_cliente, listar_clientes, remover_cliente, atualizar_cliente
from servicos.produto_servicos import adicionar_produto, listar_produtos, remover_produto, atualizar_produto
from servicos.compra_servicos import cadastrar_compra, listar_compras, remover_compra

def admin_tela(usuario):
    while(True):
        print(f"Bem vindo {usuario[1]}")
        print("""
        1 - Gerenciar clientes
        2 - Gerenciar produtos
        3 - Gerenciar compras
        4 - Sair
        """)

        menu = input("Digite a opção desejada: ")

        if menu == "1":
            while(True):
                print("""
                1 - Cadastrar cliente
                2 - Listar clientes
                3 - Deletar cliente
                4 - Atualizar cliente
                5 - Sair
                """)

                opc = input("Digite a opção desejada: ")

                if opc == "1":
                    nome_cliente = input("Digite o nome do cliente: ")
                    endereco = input("Digite o endereco do cliente: ")
                    cpf = input("digite o cpf do cliente: ")
                    telefone =  input("digite o telefone do cliente: ")
                    adicionar_cliente(nome_cliente, endereco, cpf, telefone)
                    print("cliente adicionado com sucesso!")
                elif opc == "2":
                    clientes = listar_clientes()
                    print(clientes)
                elif opc == "3":
                    id_cliente = input("Digite o id do cliente: ")
                    remover_cliente(id_cliente)
                elif opc == "4":
                    nome_cliente = input("Digite o nome do cliente: ")
                    endereco = input("Digite o endereco do cliente: ")
                    telefone = input("digite o telefone do cliente: ")
                    id_cliente = input("Digite o id do cliente: ")
                    atualizar_cliente(id_cliente, nome_cliente, endereco, telefone)
                elif opc == "5":
                    break
        elif menu == "2":
            while (True):
                print("""
                1 - Cadastrar produto
                2 - Listar produtos
                3 - Deletar produto
                4 - Atualizar produto
                5 - Sair
                """)

                opc = input("Digite a opção desejada: ")

                if opc == "1":
                    nome_produto = input("Digite o nome do produto: ")
                    quantidade_produto = input("Digite a quantidade do produto: ")
                    preco_produto = input("digite o preço do produto: ")
                    adicionar_produto(nome_produto, quantidade_produto, preco_produto)
                    print("produto adicionado com sucesso!")
                elif opc == "2":
                    produto = listar_produtos()
                    print(produto)
                elif opc == "3":
                    id_produto = input("Digite o id do produto: ")
                    remover_produto(id_produto)
                elif opc == "4":
                    nome_produto = input("Digite o nome do produto: ")
                    quantidade_produto = input("Digite a quantidade do produto: ")
                    preco_produto = input("digite o preço do produto: ")
                    id_produto = input("Digite o id do produto: ")
                    atualizar_produto(id_produto, nome_produto, quantidade_produto, preco_produto)
                elif opc == "5":
                    break

        elif menu == "3":
            while(True):
                print("""
                1 - Cadastrar compra
                2 - Listar compras
                3 - Remover compra
                4 - Sair
                """)

                opc = input("Digite a opção desejada: ")

                if opc == "1":
                    preco_compra = input("Digite o preço da compra: ")
                    id_cliente = input("insira o id do cliente")
                    id_produto = input("insira o id do produto")
                    cadastrar_compra(preco_compra, id_cliente, id_produto, usuario[0])
                    print("compra cadastrada com sucesso!")
                elif opc == "2":
                    compras = listar_compras(usuario[0])
                    print(compras)
                elif opc == "3":
                    id_compra = input("Digite o id da compra: ")
                    remover_compra(id_compra, usuario[0])
                elif opc == "4":
                    break

        elif menu == "4":
            break