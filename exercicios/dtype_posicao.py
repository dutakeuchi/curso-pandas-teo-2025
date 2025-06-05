# 03.01 - Quantas linhas há no arquivo clientes.csv ?
# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
# 03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

# %%
# 03.01 - Quantas linhas há no arquivo clientes.csv ?
import pandas as pd
clientes = pd.read_csv('../data/clientes.csv')
clientes.head()
clientes.shape
# Há 2436 linhas no arquivo
# %%
# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
transacoes = pd.read_csv('../data/transacoes.csv')
transacoes.dtypes
# Há somente uma coluna do tipo int
# %%
# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
produtos = pd.read_csv('../data/produtos.csv')
produtos.dtypes
# Há somente uma coluna do tipo object
# %%
# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
clientes['idCliente'][4]
# O idCliente do índice 4 é '00684343-40b5-4ce7-b2e8-71a5340973bf'
# %%
# 03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?
clientes['qtdePontos'][9]
# o cliente da 10ª posição tem 119 pontos
