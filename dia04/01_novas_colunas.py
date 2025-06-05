# %%
import pandas as pd
# %%
df = pd.read_csv('../data/clientes.csv')
df.head()
# %%
df['qtdePontos'] + 100
# %%
df.tail()
# %%
df.head(10)
# %%
data = pd.DataFrame(
    {'nome':['teo','mah','joao','pedro'],
     'email':[1,0,1,1],
     'twitter':[0,0,1,1],
     'youtube':[1,0,1,1]
    }
)
data
# %%
data['email'] + data['twitter']
# %%
data['email'] + data['twitter'] + data['youtube']
# %%
data['rede_social'] = data['email'] + data['twitter'] + data['youtube']
data
# %%
data['rede_social'].rename('qtt_rede_social', inplace=True)
data
# %%
data.rename(columns={'rede_social' :'qtt_rede_social'}, inplace=True)
# %%
data
# %%
df['qtdePontos'].describe()
# %%
import numpy as np
# %%
df['logPontos'] = np.log(df['qtdePontos'] + 1)
df['logPontos']
# %%
df['logPontos'].describe()
# %%
import matplotlib.pyplot as plt
# %%
plt.hist(df['qtdePontos'])
plt.show()
# %%
plt.hist(df['logPontos'])
plt.show()
# %%
