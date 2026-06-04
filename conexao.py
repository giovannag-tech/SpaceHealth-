import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="spacehealth",
    user="postgres",
    password="postgres123"
)

print("Conexão realizada com sucesso!")

conn.close()