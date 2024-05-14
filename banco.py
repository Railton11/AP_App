import sqlite3


def criar_banco_de_dados():
    try:
        conn = sqlite3.connect("banco_de_dados.db")
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
                       matricula INTEGER PRIMARY KEY NOT NULL,
                       nome TEXT NOT NULL,
                       foto TEXT,
                       data_adm DATE,
                       data DATE,
                       cargo TEXT NOT NULL,
                       empresa TEXT NOT NULL
        );''')
        conn.commit()
        print("Banco de dados e tabela criados com sucesso!")
    except sqlite3.Error as e:
        print("Erro com banco de dados", e)
    finally:
        if conn:
            conn.close()
            print("Conexão com o banco fechada")