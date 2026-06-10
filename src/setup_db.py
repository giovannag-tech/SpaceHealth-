from src.repository.conexao import conectar

SCHEMA = """
CREATE TABLE IF NOT EXISTS cidades (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nome   TEXT NOT NULL,
    estado TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS clima (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    cidade_id   INTEGER NOT NULL REFERENCES cidades(id),
    temperatura REAL NOT NULL,
    chuva       REAL NOT NULL
);
"""

CIDADES = [
    ("Sao Paulo", "SP"),
    ("Campinas",  "SP"),
    ("Santos",    "SP"),
    ("Sorocaba",  "SP"),
]


def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.executescript(SCHEMA)

    cursor.executemany(
        "INSERT OR IGNORE INTO cidades (id, nome, estado) VALUES (?, ?, ?)",
        [(i + 1, nome, estado) for i, (nome, estado) in enumerate(CIDADES)]
    )

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    criar_banco()
    print("Banco spacehealth.db criado com sucesso!")
    print("Tabelas: cidades, clima")
    print("Cidades inseridas: Sao Paulo, Campinas, Santos, Sorocaba")
