# %%
import pandas as pd
# %%
df = pd.DataFrame({
    'clientes':[1,2,3,4,5],
    'nome':['teo','jose','nah','mah','lah'],
})

df_02 = pd.DataFrame({
    'clientes':[6,7,8],
    'nome':['kozato','laura','dan'],
    'idade':[32,29,31]
})

df_03 = pd.DataFrame({
    'idade': [32,19,25,44,57]
})
# %%
df_03
# %%
pd.concat([df, df_03], axis=1)
# %%
df.merge(df_03, on=df.index)
# %%
lista = [pd.concat([df, df_03],axis=1), df_02,]
pd.concat(lista)

# %%
lista = [df, df_02,]
pd.concat(lista)
# %%
df_03.sort_values(by='idade').reset_index(drop=True)
# %%
