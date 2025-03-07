import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",          # ajuste se necessário (pode ser 'root' ou outro usuário com permissão)
            password="",          # insira sua senha do MySQL, se houver
            database="meu_sistema"
        )
        if conexao.is_connected():
            print("Conectado ao banco de dados meu_sistema!")
        return conexao
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

def adicionar_usuario(email, senha):
    conexao = conectar()
    if conexao is None:
        return
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO usuarios (email, senha_hash) VALUES (%s, SHA2(%s, 256))"
        valores = (email, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Usuário cadastrado com sucesso!")
    except Error as e:
        print("Erro ao cadastrar usuário:", e)
    finally:
        cursor.close()
        conexao.close()

def verificar_usuario(email, senha):
    conexao = conectar()
    if conexao is None:
        return False
    try:
        cursor = conexao.cursor()
        sql = "SELECT * FROM usuarios WHERE email = %s AND senha_hash = SHA2(%s, 256)"
        valores = (email, senha)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()
        if resultado:
            print("Login bem-sucedido!")
            return True
        else:
            print("Usuário ou senha incorretos.")
            return False
    except Error as e:
        print("Erro ao verificar usuário:", e)
        return False
    finally:
        cursor.close()
        conexao.close()
