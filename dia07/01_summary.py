# %%
import pandas as pd
# %%
df = pd.read_csv("../data/clientes.csv")
df.head()

# %%
df['flTwitch'].describe()

# %%
df.mean()
# apresenta erro pois há valores que o programa não consegue calcular. Ex.: object
# %%
df.dtypes
# %%
filtro = df.dtypes == 'object'
lista = df.dtypes[~filtro].index.to_list()
df[lista].describe()
# %%
df['flTwitch'].describe()
# %%
df.dtypes()
# %%
