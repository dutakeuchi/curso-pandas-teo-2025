# os dados são referentes a transações parceladas de compras. 
# Obter o valor que cada cliente tem que pagar mensalmente.

# %%
import pandas as pd
# %%
df = pd.read_csv("dados cartao.csv", sep=';')
df
# %%
df['dtTransacao'] = pd.to_datetime(df['dtTransacao']) # converta a data de str para datatime
# %%
df['vlParcela'] = df['vlVenda'] / df['qtParcelas']
df
# %%.groupby('idCliente') 
df['ordemParcela'] = df.apply(lambda row: [i for i in range(row['qtParcelas'])], axis=1)
df
# %%
# modo alternativo para obter as parcelas
# def lista(a):
#     asd = []
#     for i in range(a):
#         asd.append(i)
#     return asd

# df['ordemParcela2'] = df['qtParcelas'].apply(lista)
# df
# %%
df = df.explode('ordemParcela')
df
# %%
mes = df['dtTransacao'][0].dt.month + pd.DateOffset(months=df['ordemParcela'][0])
data = f"{df['dtTransacao'][0].dt.year} - {mes}"
data
# %%
pd.to_datetime()
# %%
df
# %%
def calcDtParcela(row):
    dado = row['dtTransacao'] + pd.DateOffset(months=row['ordemParcela'])
    dado = f"{dado.year}-{dado.month}" 
    return dado

df['dtPagamento'] = df.apply(calcDtParcela, axis=1)

# %%
type(df['dtPagamento'])
# %%
pd.to_datetime('2025-01-26') + pd.DateOffset(months=5)
# %%
pd.DateOffset(months=5)
# %%
mes = df['dtTransacao'][0].dt.month + pd.DateOffset(months=df['ordemParcela'][0])
data = f"{df['dtTransacao'][0].dt.year} - {mes}"
data
# %%
pd.DateOffset(months=df['ordemParcela'][0])
# %%
df
# %%
