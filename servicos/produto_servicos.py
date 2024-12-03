from config.db import criar_conexao


def adicionar_produto(nome_produto, quantidade_produto, preco_produto):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'INSERT INTO farmacia.produtos (nome_produto, quantidade_produto, preco_produto) VALUES (%s, %s, %s)'
    cursor.execute(sql, [nome_produto, quantidade_produto, preco_produto])
    conn.commit()


def listar_produtos():
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'SELECT * FROM farmacia.produtos'
    cursor.execute(sql)
    produtos = cursor.fetchall()
    return produtos

def remover_produto(id_produto):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'DELETE FROM farmacia.produtos where id_produto = %s'
    cursor.execute(sql, [id_produto])
    conn.commit()



def atualizar_produto(id_produto, nome_produto, quantidade_produto, preco_produtos):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'UPDATE farmacia.produtos SET nome_produto = %s, quantidade_produto = %s, preco_produto = %s WHERE id_produto = %s'
    cursor.execute(sql, [nome_produto, quantidade_produto, preco_produtos, id_produto])
    conn.commit()
