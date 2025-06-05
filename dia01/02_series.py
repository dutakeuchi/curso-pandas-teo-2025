# %%
import pandas as pd
# %%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]
# %%
media_idade = sum(idades) / len(idades)
media_idade
# %%
diff = 0
for i in idades:
    diff += (i -media_idade)**2

variancia = diff / (len(idades) - 1)
variancia
# %%
serie_idade = pd.Series()
serie_idade
# %%
serie_idade = pd.Series(idades)
serie_idade
# %%
serie_idade.mean()

# %%
serie_idade.var()
# %%
serie_idade.describe()
# %%
