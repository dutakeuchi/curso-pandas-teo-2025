# %%
import pandas as pd
# %%
df = pd.read_csv('../data/clientes.csv')
df.head()
# %%
df['qtdePontos']
# %%
df['qtdePontos'].astype(float)
# %%
df['dtCriacao']
# %%
pd.to_datetime(df['dtCriacao'])
# %%
df['dtCriacao'].replace({
    "0000-00-00 00:00:00.000":"2024-09-02 09:00:00.000"
})
# %%
df['dtCriacao'] = df['dtCriacao'].replace({
    "0000-00-00 00:00:00.000":"2024-09-02 09:00:00.000"
})
# %%
df['dtCriacao']
# %%
trocar_data = {"2024-09-02 09:00:00.000":"2024-10-02 09:00:00.000"}

df['dtCriacao'] = pd.to_datetime(df['dtCriacao'].replace(trocar_data))
df['dtCriacao']
# %%
df['dtCriacao'].dt.daysinmonth
# %%
