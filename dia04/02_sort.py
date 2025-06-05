# %%
import pandas as pd
# %%
df = pd.read_csv('../data/clientes.csv')
df.head()
# %%
df['qtdePontos']
# %%
df['qtdePontos'].sort_values()
# %%
df.sort_values(by = 'qtdePontos', ascending=False, inplace = True)
# %%
df.columns()
# %%
df.head()
# %%
df.sort_values(by = df['index'], inplace = True)
# %%
df.sort_index(inplace = True)
df
# %%
brinquedo = pd.DataFrame(
    {
        'nome': ['teo','ana','mah','jose'],
        'idade': [32, 43, 35, 42],
        'salario': [2345, 4533, 3245, 4533]
    }
)
brinquedo
# %%
brinquedo.sort_values(by='salario', ascending=False)
# %%
brinquedo.sort_values(by=['salario','idade'], ascending=False)
# %%
brinquedo.sort_values(by=['salario', 'idade'], ascending=[False, True])
# %%
