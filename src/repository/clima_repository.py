import pandas as pd

from src.repository.conexao import conectar


def inserir_leitura(cidade_id, temperatura, chuva):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO clima (cidade_id, temperatura, chuva) VALUES (?, ?, ?)",
        (cidade_id, temperatura, chuva)
    )

    conn.commit()
    cursor.close()
    conn.close()


def buscar_clima_por_cidade():
    conn = conectar()

    df = pd.read_sql("""
        SELECT cl.id, c.id AS cidade_id, c.nome AS cidade, cl.temperatura, cl.chuva
        FROM clima cl
        JOIN cidades c ON cl.cidade_id = c.id
    """, conn)

    conn.close()
    return df
