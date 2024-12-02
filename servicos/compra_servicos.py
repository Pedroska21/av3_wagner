from config.db import criar_conexao


def cadastrar_compra(preco_compra, id_cliente, id_produto, id_usuario):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'INSERT INTO farmacia.compras (preco_compra, id_cliente, id_produto, id_usuario) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql, [preco_compra, id_cliente, id_produto, id_usuario])
    conn.commit()


def listar_compras(id_usuario):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'SELECT * FROM farmacia.compras where id_usuario = %s'
    cursor.execute(sql, [id_usuario])
    compras = cursor.fetchall()
    return compras
