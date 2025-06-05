# %% 
import pandas as pd
# %%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 31
]

nomes = [
    'Teo','Maria','Jose','Carlos','Pedro',
    'Edu','Carla','Joana','Dani','Fer',
    'Naty','Nih','Luiz','Ana','Denis'
]
# %%
series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)   
# %%
df = pd.DataFrame()
df['Idades'] = series_idades
df
# %%
df['nomes'] = series_nomes
df
# %%
