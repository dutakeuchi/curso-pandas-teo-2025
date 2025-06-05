# %%
import pandas as pd
# %%
df = pd.read_csv("../data/transacoes.csv")
df.head()
# %%
pontos = [10, 1, 1, 5, 50, 100, 35, 30, 1, 10, 15, 50, 150]
valores_50 = []

# for i in pontos:
#     if i>= 50:
#         valores_50.append(i)

valores_50 = [i for i in pontos if i >= 50]
valores_50


# %%
dados = pd.DataFrame(
    {'nome': ['teo','maria','carlos'],
    'idade': [32, 45, 15],
    'profissão': ['dev','chef','estudante']
    }
)
dados
# %%
teste  = [False, False, True]

dados[teste]
# %%
dados['idade']>18
# %%
dados[dados['idade']>18]
# %%
# pegando dados onde qtpontos é maior do que 50
df[df['qtdePontos']>= 50]
# %%
filtro = df['qtdePontos']>=50
df[filtro]
# %%
# isto não funciona
filtro = 50<= df['qtdePontos'] <100
df[filtro]
# %%
filtro = (df['qtdePontos'] >= 50) & (df['qtdePontos'] <= 100)
df_50_100 = df[filtro]
# %%
df_50_100['qtdePontos'].describe
# %%
df_50_100['qtdePontos'].describe()
# %%
filtro = df['qtdePontos']>=50
df_ = df[filtro]
df_
# %%
df_['qtdePontos'].describe()
# %%
filtro = df['qtdePontos'] >= 100
df[filtro]
# %%
filtro = (df['qtdePontos'] >= 1) & (df['qtdePontos'] <= 100)
df[filtro]
# %%
filtro = (df['qtdePontos'] == -9) | (df['qtdePontos'] == 600)
df[filtro]
# %%
df['qtdePontos'].value_counts()
# %%
filtro = ~(df['qtdePontos'] > -1000)
df[filtro]
# %%
