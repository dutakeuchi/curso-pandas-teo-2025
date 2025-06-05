# %%
import pandas as pd
# %%
transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()
# %%
transacoes.groupby('idCliente', as_index=False).count()
# %%
transacoes.groupby(by='idCliente', as_index=False)[['idTransacao']].count()
# %%
summary = transacoes.groupby(by='idCliente', as_index=False).agg({'idTransacao':'count', 'qtdePontos':['sum','mean']})
summary
# %%
summary.index
# %%
summary[[('qtdePontos','mean')]]
# %%
summary['qtdePontos'][['mean']]
# %%
summary
# %%
summary.columns = ['idCliente','contagem','soma_pontos','media_pontos']
# %%
summary
# %%
