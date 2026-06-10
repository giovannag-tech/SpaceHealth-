import os
import sys

import streamlit as st
import plotly.express as px

# streamlit roda este arquivo como script: a pasta src/ entra no sys.path, nao a
# raiz do projeto. Adiciona a raiz para que "import src..." funcione.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.repository.clima_repository import buscar_clima_por_cidade
from src.service.ml_service import dados_reais, treinar_modelo, prever_risco

st.set_page_config(page_title="SpaceHealth", page_icon="🦟", layout="wide")

# ---------- Tema escuro estilo index.html ----------
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #ffffff; }
    .block-container { max-width: 1100px; padding-top: 2rem; }

    h1, h2, h3 { color: #38bdf8 !important; }

    .sh-card {
        background: #1e293b;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }

    .sh-tag {
        display: inline-block;
        background: #334155;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 4px;
        color: #e2e8f0;
    }

    .sh-pipeline { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .sh-step {
        background: #0f172a;
        border: 1px solid #38bdf8;
        padding: 10px 16px;
        border-radius: 8px;
        font-size: 0.85rem;
        color: #e2e8f0;
    }
    .sh-arrow { color: #38bdf8; font-size: 1.1rem; }

    [data-testid="stMetric"] {
        background: #334155;
        padding: 14px;
        border-radius: 10px;
    }

    .risco-Alto  { color: #f87171; font-weight: bold; }
    .risco-Medio { color: #fbbf24; font-weight: bold; }
    .risco-Baixo { color: #34d399; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("🦟 SpaceHealth")
st.caption("Sistema Inteligente de Previsão de Risco de Dengue · Global Solution 2026.1 · FIAP")

# ---------- Sobre o Projeto ----------
st.markdown("""
<div class="sh-card">
  <h2>Sobre o Projeto</h2>
  <p style="color:#cbd5e1; line-height:1.7;">
    O SpaceHealth coleta dados climáticos em tempo real via <strong>OpenWeather API</strong> e por meio de
    um <strong>simulador de sensores ESP32</strong> (DHT22 + pluviômetro), armazenando tudo em um banco
    <strong>SQLite</strong> local. Um modelo de <strong>Machine Learning (Random Forest)</strong> analisa
    temperatura e precipitação para classificar o risco de dengue em cidades brasileiras,
    apoiando ações preventivas de saúde pública.
  </p>
</div>
""", unsafe_allow_html=True)

# ---------- Pipeline ----------
st.markdown("""
<div class="sh-card">
  <h2>Pipeline da Solução</h2>
  <div class="sh-pipeline">
    <div class="sh-step">🌡️ Sensor ESP32<br><small>DHT22 + Pluviômetro</small></div>
    <span class="sh-arrow">→</span>
    <div class="sh-step">🌐 OpenWeather API<br><small>Dados em tempo real</small></div>
    <span class="sh-arrow">→</span>
    <div class="sh-step">🗄️ SQLite<br><small>spacehealth.db</small></div>
    <span class="sh-arrow">→</span>
    <div class="sh-step">🤖 Random Forest<br><small>Scikit-Learn</small></div>
    <span class="sh-arrow">→</span>
    <div class="sh-step">⚠️ Previsão de Risco<br><small>Alto / Médio / Baixo</small></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- Tecnologias ----------
st.markdown("""
<div class="sh-card">
  <h2>Tecnologias Utilizadas</h2>
  <div>
    <span class="sh-tag">Python</span>
    <span class="sh-tag">SQLite</span>
    <span class="sh-tag">Scikit-Learn</span>
    <span class="sh-tag">OpenWeather API</span>
    <span class="sh-tag">Random Forest</span>
    <span class="sh-tag">Streamlit</span>
    <span class="sh-tag">Plotly</span>
    <span class="sh-tag">GitHub</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- Dados ----------
@st.cache_data(ttl=5)
def carregar_dados():
    return buscar_clima_por_cidade()

clima = carregar_dados()

if clima.empty:
    st.warning("Nenhum dado encontrado. Execute `python -m src.service.sensor_service` para gerar leituras.")
    st.stop()

# ---------- Previsão em tempo real por cidade ----------
# Modelo treinado com dados reais (SINAN + clima Banco Mundial): temperatura + chuva
modelo = treinar_modelo(dados_reais())

ultima_leitura = clima.sort_values("id").groupby("cidade").tail(1)
ultima_leitura = ultima_leitura.copy()
ultima_leitura["risco"] = [
    prever_risco(modelo, row["temperatura"], row["chuva"])
    for _, row in ultima_leitura.iterrows()
]

st.markdown('<div class="sh-card"><h2>Previsão em Tempo Real por Cidade</h2></div>', unsafe_allow_html=True)

cols = st.columns(len(ultima_leitura))
for col, (_, row) in zip(cols, ultima_leitura.iterrows()):
    with col:
        st.markdown(f"""
        <div class="sh-card" style="text-align:center;">
            <h3>{row['cidade']}</h3>
            <p>🌡️ {row['temperatura']:.1f}°C</p>
            <p>🌧️ {row['chuva']:.1f}mm</p>
            <p>Risco: <span class="risco-{row['risco']}">{row['risco']}</span></p>
        </div>
        """, unsafe_allow_html=True)

# ---------- KPIs ----------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Leituras Registradas", len(clima))
col2.metric("Cidades Monitoradas", clima["cidade"].nunique())
col3.metric("Temp. Média (°C)", f"{clima['temperatura'].mean():.1f}")
col4.metric("Chuva Média (mm)", f"{clima['chuva'].mean():.1f}")

st.divider()

# ---------- Gráficos ----------
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Temperatura Média por Cidade")
    media_temp = clima.groupby("cidade")["temperatura"].mean().reset_index()
    fig = px.bar(
        media_temp, x="cidade", y="temperatura",
        color="temperatura", color_continuous_scale="Reds",
        labels={"temperatura": "°C", "cidade": ""},
        text_auto=".1f"
    )
    fig.update_layout(showlegend=False, coloraxis_showscale=False,
                       paper_bgcolor="#1e293b", plot_bgcolor="#1e293b", font_color="#ffffff")
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    st.subheader("Precipitação Média por Cidade")
    media_chuva = clima.groupby("cidade")["chuva"].mean().reset_index()
    fig = px.bar(
        media_chuva, x="cidade", y="chuva",
        color="chuva", color_continuous_scale="Blues",
        labels={"chuva": "mm", "cidade": ""},
        text_auto=".1f"
    )
    fig.update_layout(showlegend=False, coloraxis_showscale=False,
                       paper_bgcolor="#1e293b", plot_bgcolor="#1e293b", font_color="#ffffff")
    st.plotly_chart(fig, use_container_width=True)

col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Risco Atual por Cidade")
    cores = {"Alto": "#f87171", "Medio": "#fbbf24", "Baixo": "#34d399"}
    fig = px.bar(
        ultima_leitura, x="cidade", y=[1] * len(ultima_leitura),
        color="risco",
        color_discrete_map=cores,
        labels={"y": "", "cidade": ""},
    )
    fig.update_layout(yaxis_visible=False,
                       paper_bgcolor="#1e293b", plot_bgcolor="#1e293b", font_color="#ffffff")
    st.plotly_chart(fig, use_container_width=True)

with col_d:
    st.subheader("Temperatura × Precipitação")
    fig = px.scatter(
        clima, x="temperatura", y="chuva",
        color="cidade",
        labels={"temperatura": "Temperatura (°C)", "chuva": "Precipitação (mm)"},
    )
    fig.update_layout(paper_bgcolor="#1e293b", plot_bgcolor="#1e293b", font_color="#ffffff")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Precipitação por Cidade (todas as leituras)")
fig = px.box(
    clima, x="cidade", y="chuva",
    color="cidade",
    labels={"chuva": "Precipitação (mm)", "cidade": ""},
    points="all"
)
fig.update_layout(showlegend=False,
                   paper_bgcolor="#1e293b", plot_bgcolor="#1e293b", font_color="#ffffff")
st.plotly_chart(fig, use_container_width=True)

# ---------- Variáveis do Modelo ----------
st.markdown("""
<div class="sh-card">
  <h2>Variáveis do Modelo</h2>
  <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
    <div style="background:#334155; padding:18px; border-radius:10px;">
      <h3 style="font-size:0.95rem;">Temperatura</h3>
      <p style="color:#94a3b8;">Temperaturas elevadas favorecem a reprodução do <em>Aedes aegypti</em></p>
    </div>
    <div style="background:#334155; padding:18px; border-radius:10px;">
      <h3 style="font-size:0.95rem;">Precipitação</h3>
      <p style="color:#94a3b8;">Chuva acumula água parada — principal criadouro</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- Objetivo ----------
st.markdown("""
<div class="sh-card">
  <h2>Objetivo</h2>
  <p style="color:#cbd5e1; line-height:1.7;">
    Apoiar órgãos públicos e profissionais de saúde na tomada de decisões preventivas,
    identificando antecipadamente cidades com maior probabilidade de surto de dengue
    com base em dados climáticos objetivos.
  </p>
</div>
""", unsafe_allow_html=True)

# ---------- Dados brutos ----------
with st.expander("Ver dados brutos"):
    st.dataframe(clima, use_container_width=True)

st.caption("Giovanna Gomes Oliveira · Gabriel Coppola · Cloves Silva Filho")
