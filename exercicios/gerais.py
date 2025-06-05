# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
# 06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
# 06.03 - Qual usuário teve maior quantidade de pontos debitados?
# 06.04 - Quem teve mais transações de Streak?
# 06.05 - Qual a média de transações / dia?
# 06.06 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?
# %%
import pandas as pd
import numpy as np
# %%
# 06.01 - Qual a quantidade média de redes sociais dos usuários? 
# E a Variância? E o máximo?
clientes = pd.read_csv("../data/clientes.csv")
filtro = ['flEmail','flTwitch','flYouTube','flBlueSky','flInstagram',]
clientes['redes'] = clientes[filtro].sum(axis=1)
clientes['redes'].describe()
# %%
# 06.02 - Quais são os usuários que mais fizeram transações? 
# Considere os 10 primeiros.
transacoes = pd.read_csv('../data/transacoes.csv')
transacoes
# %%
(transacoes.groupby('idCliente')['idTransacao']
           .count()
           .sort_values(ascending=False)
           .head(10)

           )
# %%
# 06.03 - Qual usuário teve maior quantidade de pontos debitados?
filtro = transacoes['qtdePontos'] < 0
(transacoes[filtro].groupby(by='idCliente')['qtdePontos']
                   .sum()
                   .sort_values(ascending=True)
                   .head(1)
 
                   )
# %%
# 06.04 - Quem teve mais transações de Streak?
produto = pd.read_csv('../data/produtos.csv')
transacao_produto = pd.read_csv('../data/transacao_produto.csv')

transacao_merge = (transacoes.merge(transacao_produto, on = 'idTransacao', how='left')
[['idTransacao','idCliente','idProduto']] )

transicao_merge = transacao_merge.merge(produto, on='idProduto')
transicao_merge = transicao_merge[transicao_merge['descProduto'] == 'Presença Streak']

(transicao_merge.groupby(by='idCliente')['idProduto']
                .count()
                .sort_values(ascending=False)
                .head(1)
 )
# %%
# 06.04 - Quem teve mais transações de Streak?
produto = produto[produto['descProduto'] == 'Presença Streak']

(transacoes.merge(transacao_produto, on='idTransacao')
           .merge(produto, on='idProduto', how='inner')
           .groupby('idCliente')['idTransacao']
           .count()
           .sort_values(ascending=False)
           .head(1)        
 
 )

# %%
# 06.05 - Qual a média de transações / dia?
transacoes['dia'] = pd.to_datetime(transacoes['dtCriacao']).dt.date
inicio = transacoes['dia'].min()
final = transacoes['dia'].max()
contagem = (final - inicio).days

len(transacoes) / contagem
# %%
summary = transacoes.agg({'idTransacao': 'count',
                'dia':'nunique'

})
summary['idTransacao'] / summary['dia']
# %%
# 06.06 - Como podemos calcular as estatísticas descritivas dos 
# pontos das transações de cada usuário?
transacoes.groupby('idCliente')['qtdePontos'].describe()