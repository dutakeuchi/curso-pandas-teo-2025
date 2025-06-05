# %%
import pandas as pd
# %%
transacoes = pd.read_csv("../data/transacoes.csv")
clientes = pd.read_csv('../data/clientes.csv')
# %%
transacoes
# %%
clientes
# %%
transacoes.merge(right=clientes, 
                 on=['idCliente'], 
                 how='left',
                 suffixes=['transacoes','clientes']
                 )

# %%
df_1 = pd.DataFrame({
    'transacao':[1,2,3,4,5],
    'idCliente':[1,2,3,2,2],
    'valor':[10,45,32,17,87],
})

df_2 = pd.DataFrame({
    'id':[1,2,3,4],
    'nome':['teo','mah','nah','jose']
})
# %%
df_1
# %%
df_2
# %%
df_1.merge(df_2, left_on='idCliente',right_on='id', how='left')
# %%
