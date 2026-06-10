import requests

API_KEY = "5f93e1156d7ed761ac74c3141c1e08b0"


def buscar_clima_atual(cidade="Sao Paulo"):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    )

    resposta = requests.get(url)
    return resposta.status_code, resposta.json()


if __name__ == "__main__":
    status, dados = buscar_clima_atual()
    print(status)
    print(dados)
