# Ex1: Importe o arquivo CSV com o pandas.

# Ex2: Exiba as 5 primeiras linhas e as informações básicas do DataFrame.

# Ex3: Verifique os tipos de dados das colunas e altere o tipo de colunas numéricas, se necessário.

# Ex4: Renomeie colunas com nomes longos ou inconsistentes para facilitar a análise.

# Ex5: Selecione todas as colunas e apenas as linhas em que a nota da prova de matemática foi maior que 700.

# Ex6: Filtre os candidatos do estado de SP que fizeram a prova de ciências humanas.

# Ex7: Crie um filtro com duas condições: candidatos com nota de redação > 800 e idade < 18.

# Ex8: Crie uma nova coluna chamada media_notas com a média das notas das provas objetivas.

# Ex9: Ordene os candidatos por media_notas de forma decrescente.

# Ex10: Substitua todos os valores nulos das notas com zero.

# Ex11: Remova candidatos duplicados baseando-se no número de inscrição.

# Ex12: Aplique uma função que classifique os candidatos em "alto", "médio" ou "baixo" desempenho com base em media_notas.

# Ex13: Agrupe os dados por estado (UF) e calcule a média das notas por estado.

# Ex14: Use agg() para calcular a média e o desvio padrão das notas de matemática e redação.

# Ex15: Crie uma agregação personalizada que retorne:

# A maior nota de cada prova

# A menor nota

# A quantidade de valores não nulos

# Ex16: Suponha que você tenha dois DataFrames: um com candidatos de SP e outro com candidatos de MG. Use concat() para unificá-los.

# Ex17: Simule um segundo DataFrame com dados demográficos (ex: por município) e use merge() para juntar com base na cidade.

# Ex18: Use pivot_table() para calcular a média da nota de redação por estado e sexo.

# Ex19: Use stack() e unstack() para transformar o DataFrame agrupado por estado e sexo.

# Ex20: Se alguma coluna tiver listas (ex: línguas estrangeiras ou cursos), use explode() para transformar os valores em linhas separadas.

# %%
import pandas as pd
# %%
df = pd.read_csv("../../../Udemy/Estatística/treineiros_em_2019.csv", encoding='iso-8859-1')
df.head()
# %%
pd.set_option('display.max_columns',None)
# %%
# Ex3: Verifique os tipos de dados das colunas e altere o tipo de colunas numéricas, se necessário.
df.dtypes
# %%
# Ex4: Renomeie colunas com nomes longos ou inconsistentes para facilitar a análise.
df = (df.rename(columns = lambda x: x.lower())
   .drop(columns = ['co_escola','no_municipio_esc'])
     )

df
# %%
# Ex5: Selecione todas as colunas e apenas as linhas em que a nota da prova de matemática foi maior que 700.
df[df['nota_mt']> 700]
# %%
# Ex6: Filtre os candidatos do estado de SP que fizeram a prova de ciências humanas.
filtro = (df['no_municipio_residencia'] == 'São Paulo') & (df['tp_presenca_ch'] == 'presente')
df[filtro]


# %%
# Ex7: Crie um filtro com duas condições: candidatos com nota de redação > 800 e idade < 18.
filtro = (df['nota_redacao'] > 800) & (df['idade'] < 18)
df[filtro]

# %%
# Ex8: Crie uma nova coluna chamada media_notas com a média das notas das provas objetivas.
filtro = ['nota_cn','nota_ch','nota_lc','nota_mt','nota_comp1','nota_comp2','nota_comp3','nota_comp4','nota_comp5','nota_redacao',]
df[filtro] = df[filtro].fillna(0)
df['media_nota_objetiva'] = (df['nota_cn'] + df['nota_ch'] + df['nota_lc'] + df['nota_mt'] ) / 4
df


# %%
# Ex9: Ordene os candidatos por media_notas de forma decrescente.
df.sort_values('media_nota_objetiva', ascending=False)

# %%
# Ex10: Substitua todos os valores nulos das notas com zero.
df = df.fillna(0)

# %%
# Ex11: Remova candidatos duplicados baseando-se no número de inscrição.
df['nota_comp1'].unique()
# devido a formatação, todos os valores ficaram iguais

# %%
# Ex12: Aplique uma função que classifique os candidatos em "alto", "médio" ou "baixo" desempenho com base em media_notas.
# def class_nota(x):
#     if x['media_nota_objetiva'] > 558.61:
#         return'alta'
#     elif 391.0 < x['media_nota_objetiva'] <= 558.61:
#         return 'media'
#     else:
#         return 'baixa'

# df['classificacao'] = df.apply(class_nota, axis=1)
# df

import numpy as np
selecao = [ df['media_nota_objetiva'] > 558.61,
            (df['media_nota_objetiva'] > 391.0) & (df['media_nota_objetiva'] <= 558.61),
            (df['media_nota_objetiva'] <= 391.0) & df['media_nota_objetiva'] != 0,
            df['media_nota_objetiva'] == 0,
]
valor = ['alto','media','baixa','anulado']

df['classificacao'] = np.select(selecao, valor)
df
# %%
# Ex13: Agrupe os dados por estado (UF) e calcule a média das notas por estado.
(df.groupby(by='no_municipio_residencia')[['media_nota_objetiva']]
   .mean()
   .sort_values('media_nota_objetiva', 
                ascending=False))

# Ex14: Use agg() para calcular a média e o desvio padrão das notas de matemática e redação.
df.groupby(by='no_municipio_residencia')[['nota_mt','nota_redacao']].agg(['mean','std'])

# %%
# Ex15: Crie uma agregação personalizada que retorne:
# A maior nota de cada prova
# A menor nota
# A quantidade de valores não nulos
def count_not_null(x):
    return x[x!=0].count()

df[['nota_ch','nota_cn','nota_lc','nota_mt']].agg(['max','min', count_not_null])



# %%
# Ex16: Suponha que você tenha dois DataFrames: um com candidatos de SP e outro com candidatos de MG. Use concat() para unificá-los.
# os dados estão organizados por municípios e não por estados. Ao inves de SP e MG, foram selecionados São Paulo e Guarulhos
sp = df['no_municipio_residencia'] == 'São Paulo'
gru = df['no_municipio_residencia'] == 'Guarulhos'
df_sp = df[sp]
df_gru = df[gru]

df_novo = pd.concat([df_sp, df_gru]).reset_index(drop=True)
df_novo
# Ex17: Simule um segundo DataFrame com dados demográficos (ex: por município) e use merge() para juntar com base na cidade.



# %%
# Ex18: Use pivot_table() para calcular a média da nota de redação por estado e sexo.
# São Paulo, Guarulhos, Osasco, Santo André, São Caetano do Sul
filtro = ['São Paulo', 'Guarulhos', 'Osasco', 'Santo André', 'São Caetano do Sul']
df_filtrado = df[df['no_municipio_residencia'].isin(filtro)]
df_media = df_filtrado.groupby(by=['no_municipio_residencia','sexo'])[['nota_redacao','media_nota_objetiva',]].agg('mean').reset_index()
df_media.columns=['municipio','sexo','redacao','media']
df_media


# %%
# Ex19: Use stack() e unstack() para transformar o DataFrame agrupado por estado e sexo.
df_media.pivot_table(values=['redacao','media'], columns=['municipio','sexo'])


# Ex20: Se alguma coluna tiver listas (ex: línguas estrangeiras ou cursos), use explode() para transformar os valores em linhas separadas.

# %%
