# %%
import pandas as pd
# %%
df = pd.read_csv('../data/clientes.csv')
df.head()
# %%
df.dropna()
# %%
brinquedo = pd.DataFrame(
    {
        'nome': ['teo',None,'mah','jose'],
        'idade': [None, None, 35, 42],
        'salario': [2345, 4533, None, 4533]
    }
)
# %%
brinquedo
# %%
brinquedo.dropna(how='all')
# %%
brinquedo.dropna(subset='idade')
# %%
brinquedo.fillna(0)
# %%
brinquedo
# %%
brinquedo.fillna({'nome':'Teste', 'idade': brinquedo['idade'].mean()})
# %%
brinquedo[['idade','salario']].mean()
# %%
