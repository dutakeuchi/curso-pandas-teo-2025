# %%
import pandas as pd
# %%
clientes = pd.read_csv('../data/clientes.csv')
clientes.head()
# %%
clientes['idCliente'][0].split('-')[-1]
# %%
def get_last_id(x):
    return x.split("-")[-1]
# %%
get_last_id('000ff655-fa9f-4baa-a108-47f581ec52a1')
# %%
id_novo = []
for i in clientes['idCliente']:
    novo = get_last_id(i)
    id_novo.append(novo)
clientes['novo_id'] = id_novo
clientes.head()
# %%
clientes['idCliente'].apply(get_last_id)
# %%
