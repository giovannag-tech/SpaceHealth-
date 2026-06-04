import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="spacehealth",
    user="postgres",
    password="postgres123"
)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO cidades (nome, estado)
VALUES ('Sao Paulo', 'SP')
""")

conn.commit()

print("Cidade inserida com sucesso")

cursor.close()
conn.close()