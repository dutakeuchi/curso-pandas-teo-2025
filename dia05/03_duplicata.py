# %%
import pandas as pd
# %%
df = pd.DataFrame({
    'nome':['teo','maria','joao','carlos','ana','pedro','ana'],
    'sobrenome':['calvo','calvo','silva','silva','marques','marques','marques'],
    'salario':[1000,1000,1500,5461,5132,2000,5420],
})
# %%
df
# %%
df.drop_duplicates()
# %%
df.drop_duplicates(subset=['nome','sobrenome'])
# %%
df.sort_values(by='salario', inplace=True, ascending=False)
df
# %%
df.drop_duplicates(subset=['nome','sobrenome'])
# %%
df
# %%
