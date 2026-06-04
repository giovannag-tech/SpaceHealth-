import requests

api_key = "5f93e1156d7ed761ac74c3141c1e08b0"

cidade = "Sao Paulo"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

resposta = requests.get(url)

dados = resposta.json()

print(resposta.status_code)
print (dados)