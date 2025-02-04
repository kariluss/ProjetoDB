from dbcon import *

def criar_pedido(id_usuario, itens):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Pedidos (id_usuario) VALUES (?)", (id_usuario,))
    id_pedido = cursor.lastrowid
    for item in itens:
        id_produto, quantidade = item
        cursor.execute("SELECT preco FROM Produtos WHERE id_produto = ?", (id_produto,))
        preco_unitario = cursor.fetchone()[0]
        cursor.execute("INSERT INTO Pedido_Produto (id_pedido, id_produto, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
                       (id_pedido, id_produto, quantidade, preco_unitario))
        cursor.execute("UPDATE Produtos SET estoque = estoque - ? WHERE id_produto = ?", (quantidade, id_produto))
    conn.commit()
    conn.close()
    return id_pedido

def buscar_pedido(id_pedido):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pedidos WHERE id_pedido = ?", (id_pedido,))
    pedido = cursor.fetchone()
    cursor.execute("SELECT * FROM Pedido_Produto WHERE id_pedido = ?", (id_pedido,))
    produtos = cursor.fetchall()
    conn.close()
    return pedido, produtos

def atualizar_status_pedido(id_pedido, novo_status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Pedidos SET status = ? WHERE id_pedido = ?", (novo_status, id_pedido))
    conn.commit()
    conn.close()

def remover_pedido(id_pedido):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pedido_Produto WHERE id_pedido = ?", (id_pedido,))
    cursor.execute("DELETE FROM Pedidos WHERE id_pedido = ?", (id_pedido,))
    conn.commit()
    conn.close()