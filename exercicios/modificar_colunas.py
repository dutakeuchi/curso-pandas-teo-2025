# %%
# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
# 05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
# 05.05 - Selecione a primeira transação diária de cada cliente.

# %%
import pandas as pd
import numpy as np
# %%
clientes = pd.read_csv('../data/clientes.csv')
clientes.head()
# %%
# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da 
# multiplicação do saldo de pontos e a marcação da twitch
clientes['twitch_pontos'] = clientes['flTwitch'] * clientes['qtdePontos']
clientes.head()
# %%
# 05.02 - Aplique o log na coluna de saldo de pontos, 
# criando uma coluna nova
clientes['logPontos'] = np.log(clientes['qtdePontos']+1)
clientes.head()
# %%
import matplotlib.pyplot as plt
plt.hist(clientes['logPontos'])
plt.show()

# %%
# 05.03 - Crie uma coluna que sinalize se a pessoa tem 
# vínculo com alguma (qualquer uma) plataforma de rede social.
lista = ['flEmail','flTwitch','flYouTube','flBlueSky','flInstagram']
df = clientes[lista].sum(axis=1)
clientes['RedeSocial'] = np.where(df != 0, 'Sim', 'Não')
clientes
# %%
# 05.04 - Qual é o id de cliente que tem maior saldo de pontos? 
# E o menor?
maior = clientes.sort_values(by= 'qtdePontos', ascending=False)
menor = clientes.sort_values(by='qtdePontos', ascending=True)

print('Maior pontuação: ', maior.head(1)['qtdePontos'])
print('Cliente:', maior.head(1)['idCliente'])
print('Menor pontuação: ', menor.head(1)['qtdePontos'])
print('Cliente:', menor.head(1)['idCliente'])
# %%1
# 05.05 - Selecione a primeira transação diária de cada cliente.
trans = pd.read_csv('../data/transacoes.csv')
trans.sort_values('dtCriacao', inplace=True)
trans['data'] = pd.to_datetime(trans['dtCriacao']).dt.date
trans.drop_duplicates(subset = ['idCliente','data'], keep='first')
# %%

# %%
