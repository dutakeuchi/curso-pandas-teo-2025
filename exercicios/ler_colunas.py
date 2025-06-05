# 04.01 - Quantos clientes tem vínculo com a Twitch?
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

# %%
import pandas as pd
# %%
clientes = pd.read_csv('../data/clientes.csv')
clientes
# %%
# 04.01 - Quantos clientes tem vínculo com a Twitch?
filtro = clientes['flTwitch'] == 1
clientes[filtro].value_counts().sum()
# 820 clientes tem vínculo com a twitch
# %%
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
filtro2 = clientes['qtdePontos']> 1000
clientes[filtro2].value_counts().sum()
# Há 154 clientes com saldo maior do que 1000
# %%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?
clientes['dtCriacao'] = clientes['dtCriacao'].replace({
    '0000-00-00 00:00:00.000' : '2025-01-01 00:00:00.000'
})
clientes['dtCriacao'] = pd.to_datetime(clientes['dtCriacao'])

filtro3 = pd.to_datetime('2025-02-01').date()
(clientes['dtCriacao'].dt.date == filtro3).value_counts()
# Não há transações que ocorreram em 2025-02-01
# %%
