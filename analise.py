import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

global color_table
color_table = ['#540045', '#c60052', '#ff714b', '#eaff87', '#acffe9']

def retorna_tabela_df(nome_planilha):
    # Lê a tabela necessária
    df = pd.read_excel(nome_planilha)
    
    # Retorna a df
    return df

def grafico_tabela_df(df, algortimos, tempo):
    # Cria o gráfico agrupando todos os algoritmos
    fig = go.Figure(data=[
        go.Bar(name='Ordenado', x=algoritmos, y=df['Ordenado'], text=df['Ordenado'], textposition='auto'),
        go.Bar(name='Decrescente', x=algoritmos, y=df['Decrescente'], text=df['Decrescente'], textposition='auto'),
        go.Bar(name='Parcialmente Ordenado', x=algoritmos, y=df['Parcialmente Ordenado'], text=df['Parcialmente Ordenado'], textposition='auto'),
        go.Bar(name='Aleatório', x=algoritmos, y=df['Aleatório'], text=df['Aleatório'], textposition='auto')
    ])
   
    # Edita o layout do gráfico
    fig.update_layout(title='Análise de dados dos algoritmos de ordenação',
                   xaxis_title='Algoritmos',
                   yaxis_title=f'{tempo}')
    
    fig.update_layout(colorway=color_table)
    fig.update_traces(texttemplate='%{text:.2f}')
    
    return fig

def grafico_tabela_especifico_df(df, rotulos):
    
    # Cria o gráfico de barras
    fig = go.Figure(data=[
        go.Bar(name='Ordenado', x=tabelas, y=df['Ordenado'], text=df['Ordenado'], textposition='auto'),
        go.Bar(name='Decrescente', x=tabelas, y=df['Decrescente'], text=df['Decrescente'], textposition='auto'),
        go.Bar(name='Parcialmente Ordenado', x=tabelas, y=df['Parcialmente Ordenado'], text=df['Parcialmente Ordenado'], textposition='auto'),
        go.Bar(name='Aleatório', x=tabelas, y=df['Aleatório'], text=df['Aleatório'], textposition='auto')
    ])
    
    
    # Edita o layout do gráfico
    fig.update_layout(title='Análise de dados dos algoritmos de ordenação',
                   xaxis_title='Métodos de ordenação',
                   yaxis_title='Tempo médio (s)')
    
    fig.update_layout(colorway=color_table)
    fig.update_traces(texttemplate='%{text:.2f}')
   
    return fig
        
def graficos_tabela_df_quatro():
    # Ordenação 
    selection_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Selection Sort', 'Ordenado'].values[0]
        selection_sort_array.append(valor_temp)
        
    bubble_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Bubble Sort', 'Ordenado'].values[0]
        bubble_sort_array.append(valor_temp)
        
    insertion_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Insertion Sort', 'Ordenado'].values[0]
        insertion_sort_array.append(valor_temp)
    
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tabelas, y=selection_sort_array,
                    mode='lines+markers',
                    name='Selection Sort',))
    
    fig.add_trace(go.Scatter(x=tabelas, y=bubble_sort_array,
                    mode='lines+markers',
                    name='Bubble Sort'))
    fig.add_trace(go.Scatter(x=tabelas, y=insertion_sort_array,
                    mode='lines+markers',
                    name='Insertion Sort'))
    
    # Edita o layout do gráfico
    fig.update_layout(title='Análise de dados dos algoritmos de ordenação "Ordenado"',
                   xaxis_title='Quantidade de elementos',
                   yaxis_title='Tempo médio (s)')
    
    fig.update_layout(colorway=color_table)
    
    col1.plotly_chart(fig)
    
    # Decrescente
    selection_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Selection Sort', 'Decrescente'].values[0]
        selection_sort_array.append(valor_temp)
        
    bubble_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Bubble Sort', 'Decrescente'].values[0]
        bubble_sort_array.append(valor_temp)
        
    insertion_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Insertion Sort', 'Decrescente'].values[0]
        insertion_sort_array.append(valor_temp)
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tabelas, y=selection_sort_array,
                    mode='lines+markers',
                    name='Selection Sort'))
    
    fig.add_trace(go.Scatter(x=tabelas, y=bubble_sort_array,
                    mode='lines+markers',
                    name='Bubble Sort'))
    
    fig.add_trace(go.Scatter(x=tabelas, y=insertion_sort_array,
                    mode='lines+markers',
                    name='Insertion Sort'))
    
    # Edita o layout do gráfico
    fig.update_layout(title='Análise de dados dos algoritmos de ordenação "Decrescente"',
                   xaxis_title='Quantidade de elementos',
                   yaxis_title='Tempo médio (s)')
    
    fig.update_layout(colorway=color_table)
    
    
    col2.plotly_chart(fig)
    
    # Parcialmente ordenado
    selection_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Selection Sort', 'Parcialmente Ordenado'].values[0]
        selection_sort_array.append(valor_temp)
        
    bubble_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Bubble Sort', 'Parcialmente Ordenado'].values[0]
        bubble_sort_array.append(valor_temp)
        
    insertion_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Insertion Sort', 'Parcialmente Ordenado'].values[0]
        insertion_sort_array.append(valor_temp)
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tabelas, y=selection_sort_array,
                    mode='lines+markers',
                    name='Selection Sort'))
    
    fig.add_trace(go.Scatter(x=tabelas, y=bubble_sort_array,
                    mode='lines+markers',
                    name='Bubble Sort'))
    
    fig.add_trace(go.Scatter(x=tabelas, y=insertion_sort_array,
                    mode='lines+markers',
                    name='Insertion Sort'))
    
    # Edita o layout do gráfico
    fig.update_layout(title='Análise de dados dos algoritmos de ordenação "Parcialmente Ordenado"',
                   xaxis_title='Quantidade de elementos',
                   yaxis_title='Tempo médio (s)')
    
    fig.update_layout(colorway=color_table)
    
    
    col3.plotly_chart(fig)
    
    # Aleatório
    selection_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Selection Sort', 'Aleatório'].values[0]
        selection_sort_array.append(valor_temp)
        
    bubble_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Bubble Sort', 'Aleatório'].values[0]
        bubble_sort_array.append(valor_temp)
        
    insertion_sort_array = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == 'Insertion Sort', 'Aleatório'].values[0]
        insertion_sort_array.append(valor_temp)
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tabelas, y=selection_sort_array,
                    mode='lines+markers',
                    name='Selection Sort'))
    
    fig.add_trace(go.Scatter(x=tabelas, y=bubble_sort_array,
                    mode='lines+markers',
                    name='Bubble Sort'))
    
    fig.add_trace(go.Scatter(x=tabelas, y=insertion_sort_array,
                    mode='lines+markers',
                    name='Insertion Sort'))
    
    # Edita o layout do gráfico
    fig.update_layout(title='Análise de dados dos algoritmos de ordenação "Aleatório"',
                   xaxis_title='Quantidade de elementos',
                   yaxis_title='Tempo médio (s)')
    
    fig.update_layout(colorway=color_table)
    
    col4.plotly_chart(fig)

def grafico_tabela_df_separado(type):
    array_type = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == type, 'Ordenado'].values[0]
        array_type.append(valor_temp)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tabelas, y=array_type,
                    mode='lines+markers',
                    name='Ordenado'))
    
    # Decrescente
    array_type = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == type, 'Decrescente'].values[0]
        array_type.append(valor_temp)
       
    fig.add_trace(go.Scatter(x=tabelas, y=array_type,
                    mode='lines+markers',
                    name='Decrescente'))
    
    # Parcialmente ordenado
    array_type = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == type, 'Parcialmente Ordenado'].values[0]
        array_type.append(valor_temp)
        
    fig.add_trace(go.Scatter(x=tabelas, y=array_type,
                    mode='lines+markers',
                    name='Parcialmente Ordenado'))
    
    # Aleatório
    array_type = []
    for tabela in tabelas:
        valor_temp = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == type, 'Aleatório'].values[0]
        array_type.append(valor_temp)
        
    fig.add_trace(go.Scatter(x=tabelas, y=array_type,
                    mode='lines+markers',
                    name='Aleatório'))
    
    # Edita o layout do gráfico
    fig.update_layout(title=f'Análise de dados dos algoritmos de ordenação "{type}"',
                     xaxis_title='Quantidade de elementos',
                     yaxis_title='Tempo médio (s)')
    
    fig.update_layout(colorway=color_table)
    
    return fig

def dataframe_segundos_minutos(df):
    df_min = df.copy()
        
    df_min['Ordenado'] = df['Ordenado'] / 60
    df_min['Decrescente'] = df['Decrescente'] / 60
    df_min['Parcialmente Ordenado'] = df['Parcialmente Ordenado'] / 60
    df_min['Aleatório'] = df['Aleatório'] / 60
    
    return df_min

# Função para carregar os dados
algoritmos = ['Selection Sort', 'Bubble Sort', 'Insertion Sort']
rotulos = ['Ordenado', 'Decrescente', 'Parcialmente Ordenado', 'Aleatório']

tabelas = ['100', '200', '500', '1000', '2000', '5000', '7500', '10000', '15000', '30000', '50000', '75000', '100000', '200000', '500000', '750000', '1000000', '1250000', '1500000', '2000000']

# Define a dictionary to simulate a switch case
tabela_arquivos = {
    '100': 'planilha_100.xlsx',
    '200': 'planilha_200.xlsx',
    '500': 'planilha_500.xlsx',
    '1000': 'planilha_1000.xlsx',
    '2000': 'planilha_2000.xlsx',
    '5000': 'planilha_5000.xlsx',
    '7500': 'planilha_7500.xlsx',
    '10000': 'planilha_10000.xlsx',
    '15000': 'planilha_15000.xlsx',
    '30000': 'planilha_30000.xlsx',
    '50000': 'planilha_50000.xlsx',
    '75000': 'planilha_75000.xlsx',
    '100000': 'planilha_100000.xlsx',
    '200000': 'planilha_200000.xlsx',
    '500000': 'planilha_500000.xlsx',
    '750000': 'planilha_750000.xlsx',
    '1000000': 'planilha_1000000.xlsx',
    '1250000': 'planilha_1250000.xlsx',
    '1500000': 'planilha_1500000.xlsx',
    '2000000': 'planilha_2000000.xlsx'
}

with st.sidebar:
    st.markdown("### Análise de dados dos algoritmos de ordenação")
    st.markdown("##### Desenvolvido por: [Gabriel Mazzuco] [Rodrigo Rocha] [Gabriel Norato]")
    st.markdown("- Aqui podemos analisar os dados dos algoritmos de ordenação, separadamente ou todos juntos, com tabelas e gráficos, mostrando os dados em segundos e em minutos, sendo iterativo e dinâmico, podendo ser alterado a qualquer momento")
    st.divider()
    selecao_unitaria_multialgoritmo = st.sidebar.radio('Selecione a análise', ['Unitária', 'Multialgoritmo'])

if selecao_unitaria_multialgoritmo == 'Unitária':
    # Cria o layout da página com streamlit
    st.title('Análise de dados (Unitária)')
    tabela_selecionada = st.sidebar.selectbox('Selecione a tabela', tabelas)

    # Recebe o nome do meu arquivo e le ele, pegando-o do dicionário
    arquivo_selecionado = tabela_arquivos[tabela_selecionada]
    st.markdown(f"- Analise de dados dos algoritmos de ordenação com {tabela_selecionada} elementos, mostrando os dados em uma tabela e em gráficos")

    # Modifica os layouts para a tabela e para os gráficos
    col1, col2 = st.columns(2)
    st.divider()
    col3, col4 = st.columns(2)

    # Load the data if a file was selected
    if arquivo_selecionado:
        
        df = retorna_tabela_df(arquivo_selecionado)
        
        # Divide os valores da tabela de segundos para minutos e cria uma nova DF
        df_min = dataframe_segundos_minutos(df)

        st.divider()
        
        st.markdown("#### Análise separada de dados dos algoritmos de ordenação")
        st.markdown("- Aqui podemos selecionar algum dos algoritmos para analisar separadamente, sua analise será feita apenas com os dados da sua própria tabela")
        
        escolha_algoritmo = st.selectbox('Selecione o algoritmo', algoritmos)
        
        with col1:
            st.markdown("### Tabela de dados")
            col1.table(df)
            
        with col2:
            st.markdown("### Tabela de dados estatísticos")
            col2.table(df.describe())
        
        
        with col3:
            st.markdown("### Tabelas de dados em minutos")
            col3.table(df_min)
        
        with col4:
            st.markdown("### Gráficos de análise dos algoritmos de ordenação")
            activated = st.toggle('Mostrar tabela de dados em minutos', False)
            
            if activated == False:
                # Gráfico da df
                fig_df = grafico_tabela_df(df, algoritmos, 'Tempo médio (s)')
                col4.plotly_chart(fig_df)
                
            else:
                # Gráfico da df em minutos
                fig_df_min = grafico_tabela_df(df_min, algoritmos, 'Tempo médio (min)')
                col4.plotly_chart(fig_df_min)
            
        
        if escolha_algoritmo == 'Selection Sort':
            name = 'Selection Sort'
            df_selection_sort = df.loc[df['Algoritmo'] == name]
            df_selection_sort
            
            fig_selection_sort = grafico_tabela_especifico_df(df_selection_sort, rotulos)
                    
            col4, col5 = st.columns(2)
            col4.plotly_chart(fig_selection_sort)
            
            with col5:
                st.markdown("### Algoritmo Selection Sort")
                st.markdown("A ordenação por seleção ou **selection sort** consiste em selecionar o menor item e colocar na primeira posição, selecionar o segundo menor item e colocar na segunda posição, segue estes passos até que reste um único elemento. Para todos os casos (melhor, médio e pior caso) possui complexidade `C(n) = O(n²)` e não é um algoritmo estável.")
                st.markdown(
                    "<div style='text-align: center;'>"
                    "<img src='https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif' alt='Selection Sort GIF'>"
                    "</div>",
                    unsafe_allow_html=True
                )
            
        elif escolha_algoritmo == 'Bubble Sort':
            name = 'Bubble Sort'
            df_bubble_sort = df.loc[df['Algoritmo'] == name]
            df_bubble_sort
            
            fig_bubble_sort = grafico_tabela_especifico_df(df_bubble_sort, rotulos)
                    
            col4, col5 = st.columns(2)
            col4.plotly_chart(fig_bubble_sort)
            
            with col5:
                st.markdown("### Algoritmo Bubble Sort")
                st.markdown("**Bubble Sort** é um algoritmo de ordenação que pode ser aplicado em Arrays e Listas dinâmicas. Se o objetivo é ordenar os valores em forma decrescente, então, a posição atual é comparada com a próxima posição e, se a posição atual for maior que a posição posterior, é realizada a troca dos valores nessa posição. Caso contrário, não é realizada a troca, apenas passa-se para o próximo par de comparações. Possui complexidade `C(n) = O(n)` no melhor caso e `C(n) = O(n²)` no caso médio e pior caso.")
                st.markdown(
                    "<div style='text-align: center;'>"
                    "<img src='https://upload.wikimedia.org/wikipedia/commons/3/37/Bubble_sort_animation.gif' alt='Bubble Sort GIF'>"
                    "</div>",
                    unsafe_allow_html=True
                )
            
        else:
            name = 'Insertion Sort'
            df_insertion_sort = df.loc[df['Algoritmo'] == name]
            df_insertion_sort
            
            fig_insertion_sort = grafico_tabela_especifico_df(df_insertion_sort, rotulos)
                    
            col4, col5 = st.columns(2)
            col4.plotly_chart(fig_insertion_sort)
            
            with col5:
                st.markdown("### Algoritmo Insertion Sort")
                st.markdown("**Insertion Sort** ou ordenação por inserção é o método que percorre um vetor de elementos da esquerda para a direita e à medida que avança vai ordenando os elementos à esquerda. Possui complexidade `C(n) = O(n)` no melhor caso e `C(n) = O(n²)` no caso médio e pior caso. É considerado um método de ordenação estável.")
                st.markdown(
                    "<div style='text-align: center;'>"
                    "<img src='https://d2m498l008ebpa.cloudfront.net/2016/12/insertion-sort-animation-1-1.gif' alt='Insertion Sort GIF'>"
                    "</div>",
                    unsafe_allow_html=True
                )
            
    else:
        df = None
        media_df = None

elif selecao_unitaria_multialgoritmo == 'Multialgoritmo':
    # Cria o layout da página com streamlit
    st.title('Análise de dados (Multialgoritmos)')
    
    st.markdown("#### Gráficos de análise dos algoritmos de ordenação")
    st.markdown(f"- Analise de dados dos algoritmos de ordenação, com todas as tabelas fazendo comparações entre eles mesmo, separando-os por tipo de ordenação (Ordenado, Decrescente, Parcialmente Ordenado e Aleatório)")
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    dfs = {}
    dfs_rotulos = {}

    for tabela in tabelas:
        dfs[tabela] = retorna_tabela_df(f'planilha_{tabela}.xlsx')
      
    graficos_tabela_df_quatro()          

    st.divider()
    
    st.markdown("#### Análise separada de dados dos algoritmos de ordenação")
    st.markdown("- Aqui podemos selecionar algum dos algoritmos para analisar separadamente, sua analise será feita apenas com os dados da sua própria tabela")

    escolha_algoritmo = st.selectbox('Selecione o algoritmo', algoritmos)   
    
    if escolha_algoritmo == 'Selection Sort':
        col5, col6 = st.columns(2) 
        
        name = 'Selection Sort'
        for tabela in tabelas:
            dfs_rotulos[tabela] = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == name]

        fig = grafico_tabela_df_separado(name)
        
        col5.plotly_chart(fig)
        
        with col6:
            st.markdown("### Algoritmo Selection Sort")
            st.markdown("A ordenação por seleção ou **selection sort** consiste em selecionar o menor item e colocar na primeira posição, selecionar o segundo menor item e colocar na segunda posição, segue estes passos até que reste um único elemento. Para todos os casos (melhor, médio e pior caso) possui complexidade `C(n) = O(n²)` e não é um algoritmo estável.")
            st.markdown(
                "<div style='text-align: center;'>"
                "<img src='https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif' alt='Selection Sort GIF'>"
                "</div>",
                unsafe_allow_html=True
            )

        
    elif escolha_algoritmo == 'Bubble Sort':
        col5, col6 = st.columns(2)
        
        name = 'Bubble Sort'
        for tabela in tabelas:
            dfs_rotulos[tabela] = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == name]
        
        fig = grafico_tabela_df_separado(name)
        
        col5.plotly_chart(fig)
        
        with col6:
            st.markdown("### Algoritmo Bubble Sort")
            st.markdown("**Bubble Sort** é um algoritmo de ordenação que pode ser aplicado em Arrays e Listas dinâmicas. Se o objetivo é ordenar os valores em forma decrescente, então, a posição atual é comparada com a próxima posição e, se a posição atual for maior que a posição posterior, é realizada a troca dos valores nessa posição. Caso contrário, não é realizada a troca, apenas passa-se para o próximo par de comparações. Possui complexidade `C(n) = O(n)` no melhor caso e `C(n) = O(n²)` no caso médio e pior caso.")
            st.markdown(
                "<div style='text-align: center;'>"
                "<img src='https://upload.wikimedia.org/wikipedia/commons/3/37/Bubble_sort_animation.gif' alt='Bubble Sort GIF'>"
                "</div>",
                unsafe_allow_html=True
            )
        
    
    else:
        col5, col6 = st.columns(2)
        
        name = 'Insertion Sort'
        for tabela in tabelas:
            dfs_rotulos[tabela] = dfs[tabela].loc[dfs[tabela]['Algoritmo'] == name]
            
        fig = grafico_tabela_df_separado(name)
        
        col5.plotly_chart(fig)
        
        with col6:
            st.markdown("### Algoritmo Insertion Sort")
            st.markdown("**Insertion Sort** ou ordenação por inserção é o método que percorre um vetor de elementos da esquerda para a direita e à medida que avança vai ordenando os elementos à esquerda. Possui complexidade `C(n) = O(n)` no melhor caso e `C(n) = O(n²)` no caso médio e pior caso. É considerado um método de ordenação estável.")
            st.markdown(
                "<div style='text-align: center;'>"
                "<img src='https://d2m498l008ebpa.cloudfront.net/2016/12/insertion-sort-animation-1-1.gif' alt='Insertion Sort GIF'>"
                "</div>",
                unsafe_allow_html=True
            )
    