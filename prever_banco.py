import psycopg2
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

conn = psycopg2.connect(
    host="localhost",
    database="spacehealth",
    user="postgres",
    password="postgres123"
)

query = """
SELECT 
    cl.temperatura,
    cl.umidade,
    cl.chuva,
    p.risco
FROM clima cl
JOIN previsao_dengue p 
ON cl.cidade_id = p.cidade_id;
"""

dados = pd.read_sql(query, conn)

X = dados[["temperatura", "umidade", "chuva"]]
y = dados["risco"]

modelo = RandomForestClassifier()
modelo.fit(X, y)

nova_previsao = modelo.predict([[30, 80, 20]])

print("Previsao de risco de dengue:", nova_previsao[0])

conn.close()