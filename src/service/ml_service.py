import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Modelo treina sobre clima real: temperatura + chuva.
COLUNAS = ["temperatura", "chuva"]

DATASET_REAL = "data/dataset_treino.csv"


def dados_reais():
    """
    Dataset real: casos confirmados de dengue (SINAN 2012-2021, 12.4M registros)
    agregados por mes e cruzados com as normais climaticas do Brasil
    (Banco Mundial, 1991-2020). O 'risco' vem do tercil dos casos observados.
    """
    df = pd.read_csv(DATASET_REAL)
    return df[["temperatura", "chuva", "risco"]]


def dados_exemplo():
    """Dataset sintetico de fallback, caso o CSV real nao esteja disponivel."""
    return pd.DataFrame({
        'temperatura': [29, 31, 27, 30, 33, 25, 28, 32],
        'chuva':       [12,  0, 18,  5,  0, 25, 15,  0],
        'risco':       ['Alto', 'Baixo', 'Alto', 'Medio',
                        'Baixo', 'Alto', 'Alto', 'Baixo']
    })


def treinar_modelo(dados):
    X = dados[COLUNAS]
    y = dados["risco"]

    modelo = RandomForestClassifier()
    modelo.fit(X, y)
    return modelo


def prever_risco(modelo, temperatura, chuva):
    entrada = pd.DataFrame([[temperatura, chuva]], columns=COLUNAS)
    return modelo.predict(entrada)[0]


if __name__ == "__main__":
    dados = dados_reais()
    modelo = treinar_modelo(dados)

    risco = prever_risco(modelo, 30, 200)
    print("Previsao de risco de dengue:", risco)
