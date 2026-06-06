# FIAP - Faculdade de Informática e Administração Paulista

# SpaceHealth
## Sistema Inteligente de Previsão de Risco de Dengue

### 👩‍🎓 Integrante

- RM567169 - Giovanna Gomes Oliveira

---

## 📝 Descrição

O SpaceHealth é uma solução desenvolvida para auxiliar na previsão de risco de dengue utilizando dados climáticos coletados através da API OpenWeather.

O sistema integra Inteligência Artificial, Machine Learning, Banco de Dados PostgreSQL e uma interface web para análise dos dados.

A proposta utiliza informações de temperatura, umidade e precipitação para identificar padrões associados ao aumento do risco de dengue em cidades brasileiras.

---

## 🚀 Tecnologias Utilizadas

- Python
- PostgreSQL
- Machine Learning (Scikit-Learn)
- OpenWeather API
- HTML5
- CSS3
- GitHub
- Power BI

---

## 📂 Estrutura do Projeto

```text
SpaceHealth/
│
├── buscar_clima.py
├── conexao.py
├── inserir_cidade.py
├── prever_banco.py
├── treinar_modelo.py
├── index.html
├── README.md
└── docs/
```

---

## ⚙️ Funcionalidades

- Cadastro de cidades
- Coleta automática de dados climáticos
- Armazenamento em PostgreSQL
- Treinamento do modelo de Machine Learning
- Previsão de risco de dengue
- Dashboard analítico
- Interface Web em HTML

---

## 🖥️ Interface Web

A aplicação possui uma interface HTML desenvolvida para apresentação da solução.

Recursos disponíveis:

- Descrição do projeto
- Tecnologias utilizadas
- Objetivos da solução
- Apresentação visual do sistema

---

## 📊 Banco de Dados

Banco utilizado:

- PostgreSQL

Tabelas principais:

- cidades
- clima
- previsao_dengue

---

## 🤖 Machine Learning

O modelo foi desenvolvido utilizando a biblioteca Scikit-Learn.

Variáveis analisadas:

- Temperatura
- Umidade
- Precipitação

Objetivo:

- Identificar padrões climáticos relacionados ao aumento do risco de dengue.

---

## ▶️ Como Executar

Instalar dependências:

```bash
pip install pandas scikit-learn psycopg2 requests
```

Executar coleta climática:

```bash
python buscar_clima.py
```

Treinar modelo:

```bash
python treinar_modelo.py
```

Gerar previsões:

```bash
python prever_banco.py
```

---

## 📈 Resultados Esperados

O sistema permite identificar cidades com maior probabilidade de ocorrência de dengue através da análise de dados climáticos.

A solução pode auxiliar órgãos públicos e profissionais da saúde na tomada de decisões preventivas.

---

## 🎯 Conclusão

O projeto SpaceHealth demonstra a aplicação prática de Inteligência Artificial, Banco de Dados, APIs e Machine Learning para solucionar problemas reais relacionados à saúde pública.

A utilização de dados climáticos possibilita prever cenários de risco e contribuir para ações preventivas contra a dengue.

---

## 🔗 Repositório

Projeto desenvolvido para a Global Solution FIAP 2026.1.

RM567169 - Giovanna Gomes Oliveira