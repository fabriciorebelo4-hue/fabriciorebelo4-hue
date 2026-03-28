import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página para ficar mais bonita e ocupar a tela toda
st.set_page_config(page_title="Dashboard Executivo", layout="wide")

# Título do App
st.title("🚀 Painel de Inteligência de Negócios (Em Tempo Real)")
st.markdown("Uma solução disruptiva para análise de dados usando Python.")

# Gerando dados fictícios para a demonstração (finja que veio do banco de dados da empresa)
@st.cache_data
def carregar_dados():
    datas = pd.date_range(start='1/1/2023', periods=100)
    df = pd.DataFrame({
        'Data': datas,
        'Vendas': np.random.randint(1000, 5000, size=100),
        'Custos': np.random.randint(500, 3000, size=100),
        'Setor': np.random.choice(['Tecnologia', 'Varejo', 'Serviços'], size=100)
    })
    df['Lucro'] = df['Vendas'] - df['Custos']
    return df

dados = carregar_dados()

# Criando uma barra lateral interativa
st.sidebar.header("Filtros Inteligentes")
setor_selecionado = st.sidebar.multiselect(
    "Selecione os Setores:",
    options=dados['Setor'].unique(),
    default=dados['Setor'].unique()
)

# Filtrando os dados com base na escolha do usuário
dados_filtrados = dados[dados['Setor'].isin(setor_selecionado)]

# Criando métricas de destaque (KPIs) parecidas com painéis de diretoria
st.subheader("📊 Indicadores Chave de Performance (KPIs)")
col1, col2, col3 = st.columns(3)

col1.metric("Vendas Totais", f"R$ {dados_filtrados['Vendas'].sum():,.2f}")
col2.metric("Custo Total", f"R$ {dados_filtrados['Custos'].sum():,.2f}", delta="-1.2% (redução)", delta_color="inverse")
col3.metric("Lucro Líquido", f"R$ {dados_filtrados['Lucro'].sum():,.2f}", delta="5.4% (crescimento)")

# Gráfico interativo
st.subheader("📈 Evolução Financeira")
# Transformando a coluna 'Data' no índice para o gráfico de linhas do Streamlit
grafico_dados = dados_filtrados.set_index('Data')[['Vendas', 'Custos', 'Lucro']]
st.line_chart(grafico_dados)

st.success("Tudo rodando em tempo real com Python! Fim do relatório estático.")
