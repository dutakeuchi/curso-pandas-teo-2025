# %%
import pandas as pd
# %%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 31
]
# %%
series_idades = pd.Series(idades)
# %%
idades[0]
# %%
series_idades[0]
# %%
idades[-1]
# %%
series_idades[10:]
# %%
