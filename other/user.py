from dbcon import *

# funções de CRUD
def inserir_usuario(nome, email, telefone, data_nascimento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Usuarios (nome, email, telefone, data_nascimento) VALUES (?, ?, ?, ?)",
                   (nome, email, telefone, data_nascimento))
    conn.commit()
    conn.close()

def buscar_usuario_por_nome(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE LOWER(nome) LIKE LOWER(?)", ('%' + nome + '%',))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_telefone(id_usuario, novo_telefone):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Usuarios SET telefone = ? WHERE id_usuario = ?", (novo_telefone, id_usuario))
    conn.commit()
    conn.close()

def remover_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id_usuario = ?", (id_usuario,))
    conn.commit()
    conn.close()

# funções específicas
# Função de Inserção em Massa
def inserir_usuarios_massa(usuarios):
    conn = conectar()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO Usuarios (nome, email, telefone, data_nascimento) VALUES (?,?,?,?)", usuarios)
    conn.commit()

# Função de Busca por Substring (Case Sensitive)
def buscar_usuario_por_substring(substring):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE LOWER(nome) LIKE LOWER(?)", ('%' + substring + '%',))
    resultado = cursor.fetchall()
    conn.close()
    return resultado