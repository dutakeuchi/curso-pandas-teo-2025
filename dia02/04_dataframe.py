# %%
import pandas as pd
# %%
df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes
# %%
df_clientes.info(memory_usage='deep')
# %%
df_clientes.dtypes
# %%
