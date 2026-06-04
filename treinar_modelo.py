import pandas as pd
from sklearn.ensemble import RandomForestClassifier

dados = pd.DataFrame({
    'temperatura': [29, 31, 27, 30, 33, 25, 28, 32],
    'umidade': [75, 60, 85, 68, 55, 90, 80, 50],
    'chuva': [12, 0, 18, 5, 0, 25, 15, 0],
    'risco': ['Alto', 'Baixo', 'Alto', 'Medio',
              'Baixo', 'Alto', 'Alto', 'Baixo']
})

X = dados[['temperatura', 'umidade', 'chuva']]
y = dados['risco']

modelo = RandomForestClassifier()

modelo.fit(X, y)

previsao = modelo.predict([[30, 80, 20]])

print("Previsao:", previsao[0])