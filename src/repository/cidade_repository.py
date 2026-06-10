from src.repository.conexao import conectar


def inserir_cidade(nome, estado):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cidades (nome, estado) VALUES (?, ?)",
        (nome, estado)
    )

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    inserir_cidade("Sao Paulo", "SP")
    print("Cidade inserida com sucesso")
