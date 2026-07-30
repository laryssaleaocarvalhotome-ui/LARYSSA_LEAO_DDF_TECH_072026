import streamlit as st

st.set_page_config(
    page_title="Dashboard Olist",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Executivo — E-commerce Olist")

st.markdown(
    """
    Este Data App apresenta os principais indicadores e análises
    desenvolvidos no Case Técnico da Dadosfera.
    """
)

st.divider()

st.subheader("📌 Indicadores de Negócio")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Clientes únicos", "96.096")
col2.metric("Pedidos", "99.441")
col3.metric("Produtos", "32.951")
col4.metric("Vendedores", "3.095")

col5, col6, col7, col8 = st.columns(4)

col5.metric("Categorias", "71")
col6.metric("Faturamento", "R$ 13,59 mi")
col7.metric("Ticket médio", "R$ 136,68")
col8.metric("Nota média", "4,09")

st.divider()

st.subheader("📊 Dashboard Executivo")

st.image(
    "images/dashboard_executivo.png",
    caption="Visão geral dos principais indicadores do negócio",
    use_container_width=True
)

st.divider()

st.subheader("📈 Principais Visualizações")

aba1, aba2, aba3, aba4, aba5 = st.tabs(
    [
        "Clientes",
        "Categorias",
        "Pedidos",
        "Avaliações",
        "Entregas"
    ]
)

with aba1:
    st.image(
        "images/clientes_estado.png",
        caption="Distribuição dos clientes por estado",
        use_container_width=True
    )

with aba2:
    st.image(
        "images/top_categorias.png",
        caption="Top 10 categorias mais vendidas",
        use_container_width=True
    )

with aba3:
    st.image(
        "images/evolucao_pedidos.png",
        caption="Evolução mensal dos pedidos",
        use_container_width=True
    )

with aba4:
    st.image(
        "images/avaliacoes_clientes.png",
        caption="Distribuição das avaliações dos clientes",
        use_container_width=True
    )

with aba5:
    st.image(
        "images/tempo_entrega.png",
        caption="Distribuição do tempo de entrega",
        use_container_width=True
    )

st.divider()

st.subheader("💡 Principais Insights")

st.markdown(
    """
    - **Clientes:** São Paulo concentra a maior quantidade de clientes.
    - **Categorias:** Casa, decoração e beleza estão entre as categorias com maior volume de vendas.
    - **Avaliações:** A nota 5 é a mais frequente, indicando alta satisfação dos consumidores.
    - **Entregas:** Grande parte das entregas ocorre entre 7 e 20 dias.
    - **Pedidos:** O volume de pedidos apresentou crescimento ao longo do período analisado.
    """
)

st.divider()

st.caption(
    "Projeto desenvolvido por Laryssa Leão de Carvalho Tomé para o Case Técnico da Dadosfera."
)
