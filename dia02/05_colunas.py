# %%
import pandas as pd
# %%
df = pd.read_csv('../data/transacoes.csv')
df.head()
# %%
df.shape
# %%
df.info(memory_usage='deep')
# %%
df.rename(columns={'qtdePontos':'qtPontos', 
                   "descSistemaOrigem":"SistemaOrigem"}, inplace=True)
# %%
df.head()
# %%
df[["idCliente","qtPontos"]]
# %%
