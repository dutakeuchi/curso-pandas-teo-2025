# %%
import pandas as pd

df_pedidos = pd.DataFrame({
    'idPedido': [101, 102, 103, 104, 105, 106, 107, 108],
    'idCliente': [1, 2, 1, 3, 4, 2, 5, 3],
    'dtPedido': [
        '2025-01-10', '2025-01-15', '2025-02-01', '2025-02-10',
        '2025-03-05', '2025-03-20', '2025-04-02', '2025-04-15'
    ],
    'vlTotal': [250.0, 180.0, 320.0, 100.0, 400.0, 220.0, 600.0, 90.0],
    'formaPagamento': ['Cartão', 'Boleto', 'Pix', 'Cartão', 'Pix', 'Boleto', 'Cartão', 'Pix'],
    'statusEntrega': ['Entregue', 'Entregue', 'Cancelado', 'Entregue', 'Entregue', 'Cancelado', 'Entregue', 'Entregue'],
    'qtItens': [2, 1, 3, 1, 4, 2, 5, 1]
})
# %%
df_pedidos.to_csv('dados_e-comerce.csv', sep=';', index=False)
# %%
