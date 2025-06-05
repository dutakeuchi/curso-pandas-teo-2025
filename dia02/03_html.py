# %%
import pandas as pd
# %%
df = pd.read_clipboard()
df
# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
dfs
# %%
len(dfs)
# %%
dfs[1
    ]
# %%
df_uf = dfs[1]
df_uf
# %%
df_uf.to_csv("unidade federativa do brasil.csv", index = False, sep=';')
# %%
