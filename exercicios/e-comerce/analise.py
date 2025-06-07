# exercício extraído a partir do chatgpt

# 1. Visualize os primeiros pedidos com .head() e veja a estrutura da tabela.

# 2. Crie uma nova coluna com o mês do pedido no formato YYYY-MM.

# 3. Qual foi o valor total vendido por mês? Use groupby() e sum().

# 4. Qual cliente mais comprou (em valor)? E qual comprou mais itens?

# 5. Mostre o número de pedidos por forma de pagamento, em ordem decrescente.

# 6. Filtre os pedidos cancelados.

# 7. Filtre pedidos entregues com valor acima de R$300.

# 8. Crie uma nova coluna ticketMedio que divide vlTotal por qtItens.

# 9. Substitua "Pix" por "PIX" e "Cartão" por "Cartao" na coluna formaPagamento.

# 10. Crie um ranking por cliente com base no total gasto.

# 11. Gere uma tabela resumo por cliente contendo:
# Total gasto
# Número de pedidos
# Média de itens por pedido
# % de pedidos entregues

# %%
import pandas as pd
df = pd.read_csv('dados_e-comerce.csv', sep=';', )
df
# %%
# 1. Visualize os primeiros pedidos com .head() e veja a estrutura da tabela.
df.head()
# %%
# 2. Crie uma nova coluna com o mês do pedido no formato YYYY-MM.
df['dtPedido'] = pd.to_datetime(df['dtPedido'])
df['mesPedido'] = df['dtPedido'].dt.strftime('%Y-%m')
df
# %%
# 3. Qual foi o valor total vendido por mês? Use groupby() e sum().
(df.groupby(by='mesPedido')[['vlTotal']]
   .sum()
   .pivot_table(values='vlTotal', 
                columns='mesPedido')
                
)
# %%
# 4. Qual cliente mais comprou (em valor)? E qual comprou mais itens?
(df.groupby('idCliente')[['vlTotal']]
   .sum()
)
# %%
# 4.1. E qual comprou mais itens?
(df.groupby('idCliente')[['qtItens']]
   .sum()
)
# %%
# 5. Mostre o número de pedidos por forma de pagamento, em ordem decrescente.
(df.groupby(by='formaPagamento')[[]]
   .value_counts()
   .reset_index()
   .sort_values('count', 
                ascending=False)
 )
# %%
df
# %%
# 6. Filtre os pedidos cancelados.
df[df['statusEntrega'] == 'Cancelado']
# %%
# 7. Filtre pedidos entregues com valor acima de R$300.
df[df['vlTotal']>= 300]
# %%
# 8. Crie uma nova coluna ticketMedio que divide vlTotal por qtItens.
df['ticketMedio'] = round((df['vlTotal'] / df['qtItens']), 2)
df



# %%
# 9. Substitua "Pix" por "PIX" e "Cartão" por "Cartao" na coluna formaPagamento.
filtro = {'Pix':'PIX', 'Cartão':'Cartao'}
df['formaPagamento'] = df['formaPagamento'].replace(filtro)
df
# %%
# 10. Crie um ranking por cliente com base no total gasto.
df.groupby('idCliente')[['vlTotal']].sum()

# %%
# 11. Gere uma tabela resumo por cliente contendo:
# Total gasto
# Número de pedidos
# Média de itens por pedido
# % de pedidos entregues
df2 = pd.DataFrame()
df2['vlTotal'] = df.groupby('idCliente')[['vlTotal']].sum()
df2['qttPedidos'] = df.groupby('idCliente')[['idPedido']].count()
df2['media_itens'] = (df.groupby('idCliente')[['qtItens']].sum() / df.groupby('idCliente')[['qtItens']].count())
df2['taxa_entrega_(%)'] = df.groupby("idCliente")[['foiEntregue']].mean() * 100
df2
