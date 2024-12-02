from config.db import criar_conexao


def adicionar_cliente(nome_cliente, endereco, cpf, telefone):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'INSERT INTO farmacia.clientes (nome_cliente, endereco, cpf, telefone) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql, [nome_cliente, endereco, cpf, telefone])
    conn.commit()


def listar_clientes():
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'SELECT * FROM farmacia.clientes'
    cursor.execute(sql)
    clientes = cursor.fetchall()
    return clientes


def remover_cliente(id_cliente):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'DELETE FROM farmacia.clientes WHERE id_cliente = %s'
    cursor.execute(sql, [id_cliente])
    conn.commit()


def atualizar_cliente(id_cliente, nome_cliente, endereco, telefone):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'UPDATE farmacia.clientes SET nome_cliente = %s, endereco = %s, telefone = %s WHERE id_cliente = %s'
    cursor.execute(sql, [nome_cliente, endereco, telefone, id_cliente])
    conn.commit()