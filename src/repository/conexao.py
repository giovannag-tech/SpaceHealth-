import sqlite3

DB_PATH = "spacehealth.db"


def conectar():
    return sqlite3.connect(DB_PATH)


if __name__ == "__main__":
    conn = conectar()
    print("Conexão realizada com sucesso!")
    conn.close()
