# %%
import pandas as pd
# %%
df = pd.read_csv('../data/transacao_produto.csv')
df.head()
# %%
filtro = (df['idProduto'] == 5) | (df['idProduto'] == 11)
df[filtro]
# %%
df['idProduto'].isin([5,11])
# %%
filtro = df['idProduto'].isin([5,11])
df[filtro]
# %%
data = pd.read_csv('../data/clientes.csv')
data.head()
# %%
data['flag_1'] = 1
# %%
filtro = data['qtdePontos'] == 0
clientes_0 = data[filtro]
clientes_0.head()
# %%
clientes_0['flag_1'] = 1
# %%
