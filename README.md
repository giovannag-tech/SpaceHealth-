# SpaceHealth

## Integrantes

Giovanna Gomes Oliveira

## Descrição

O SpaceHealth é uma plataforma de monitoramento epidemiológico que utiliza Inteligência Artificial para prever riscos de dengue com base em dados climáticos.

A solução utiliza informações de temperatura, umidade e chuva obtidas através de APIs meteorológicas, armazenadas em banco de dados PostgreSQL e analisadas por um modelo de Machine Learning.

## Objetivo

Auxiliar órgãos públicos e profissionais da saúde na identificação antecipada de regiões com maior probabilidade de ocorrência de dengue.

## Tecnologias Utilizadas

- Python
- PostgreSQL
- pgAdmin 4
- Power BI
- Pandas
- Scikit-Learn
- API OpenWeather
- Machine Learning

## Arquitetura da Solução

1. Coleta de dados climáticos através da API OpenWeather.
2. Armazenamento dos dados no PostgreSQL.
3. Processamento dos dados utilizando Python.
4. Treinamento do modelo Random Forest.
5. Geração de previsões de risco.
6. Visualização dos resultados no Power BI.

## Machine Learning

Foi utilizado o algoritmo Random Forest para classificação do risco de dengue em:

- Baixo
- Médio
- Alto

Variáveis utilizadas:

- Temperatura
- Umidade
- Chuva

## Resultados

O sistema consegue prever automaticamente o nível de risco de dengue a partir de dados climáticos coletados pela API.

## Evidências

As imagens do projeto estão disponíveis na pasta:

docs/imagens

## Como Executar

Instalar dependências:

pip install pandas scikit-learn psycopg2 requests

Executar:

python buscar_clima.py

python treinar_modelo.py

python prever_banco.py