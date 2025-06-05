# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv("../data/transacoes.csv")
df.head()
# %%
# sqrt((amplitude - media) ** 2)

def amp_to_mean(valor: pd.Series):
    x = np.sqrt((valor.max() - valor.mean()) ** 2)
    return x

def time_time(valor: pd.Series):
    dt = pd.to_datetime(valor)
    return (pd.to_datetime('today') - dt.min()).days


# %%
data = (df.groupby(by = 'idCliente', as_index=False)
 .agg({'idTransacao':'count',
       'qtdePontos':('sum','mean', 'max',amp_to_mean),
       'dtCriacao' :time_time

     })
 
 )

# %%
data
# %%
data.columns = ['idCliente','cont_transacao','soma_pontos','media_pontos',
              'pont_max','amp_media','dias_criacao']
data# %%

# %%
