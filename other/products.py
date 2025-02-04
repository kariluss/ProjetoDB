from dbcon import *

def inserir_produto(nome, preco, categoria, estoque):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produtos (nome, preco, categoria, estoque) VALUES (?,?,?,?)", (nome, preco, categoria, estoque))
    conn.commit()
    conn.close()

def buscar_produto_por_nome(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE LOWER(nome) LIKE LOWER(?)", ('%' + nome + '%',))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_estoque_produto(id_produto, novo_estoque):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Produtos SET estoque = ? WHERE id_produto = ?", (novo_estoque, id_produto))
    conn.commit()
    conn.close()

def remover_produto(id_produto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Produtos WHERE id_produto = ?", (id_produto,))
    conn.commit()
    conn.close()

def inserir_produtos_massa(produtos):
    conn = conectar()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO Produtos (nome, preco, categoria, estoque) VALUES (?,?,?,?)", produtos)
    conn.commit()
    conn.close()

def buscar_todos_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def buscar_produto_por_substring(substring):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE LOWER(nome) LIKE LOWER(?)", ('%' + substring + '%',))
    resultado = cursor.fetchall()
    conn.close()
    return resultado