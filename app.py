import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título e introdução do projeto
st.title("Painel de Análise de Alunos")
st.markdown("""
Pode visualizar as informações completas, filtrar por curso, analisar estatísticas de notas
e até gerar gráficos ou baixar os dados filtrados.
""")

# carregar planilha em csv
df = pd.read_csv("dados.csv")

# Exibindo os dados 
st.subheader(" Alunos")
st.write("Alunos Registrados no Sistema:")
st.write(df)

# Filtro de seleção
curso_escolhido = st.selectbox(" Selecione o curso para análise:", df["curso"].unique())
dados_filtrados = df[df["curso"] == curso_escolhido]

# Estatísticas com base no curso selecionado
st.subheader(" Estatísticas das Notas")
media = round(dados_filtrados["nota"].mean(), 2)
maior = dados_filtrados["nota"].max()
menor = dados_filtrados["nota"].min()

st.write(f"Nota média: **{media}**")
st.write(f"Maior nota: **{maior}**")
st.write(f"Menor nota: **{menor}**")

# Exibição da tabela filtrada
st.subheader(f" Alunos do curso: {curso_escolhido}")
st.write("Os alunos abaixo estão matriculados no curso selecion ado:")
st.write(dados_filtrados.style.highlight_max("nota", color="lightgreen"))

# Gráfico de distribuição das notas
st.subheader("Distribuição das Notas")
fig, ax = plt.subplots()
dados_filtrados["nota"].hist(bins=10, ax=ax, color='skyblue', edgecolor='black')
ax.set_xlabel("Nota")
ax.set_ylabel("Quantidade de Alunos")
st.pyplot(fig)

# Opção para baixar os dados filtrados  
st.subheader("⬇ Exportar Dados")
st.download_button(
    label="📥 Baixar tabela em CSV",
    data=dados_filtrados.to_csv(index=False),
    file_name=f"alunos_{curso_escolhido}.csv",
    mime="text/csv"
)


st.markdown("---")
st.caption("Pablo Aguayo")
