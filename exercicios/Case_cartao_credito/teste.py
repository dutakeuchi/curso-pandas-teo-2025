# %%
import pandas as pd
# %%
df = pd.read_csv("dados_cartao.csv", sep=';')
df
# %%
df['dtTransacao'] = pd.to_datetime(df['dtTransacao'])
# %%
# obtem o valor de cada parcela desta compra
df['vlParcela'] = round((df['vlVenda'] / df['qtParcelas']), 2)
df
# %%
# obtem os números das parcelas
def get_parcela(a):
    lista = []
    for i in range(a):
        lista.append(i)
    return lista

df['numero_parcela'] = df['qtParcelas'].apply(get_parcela)
df
# %%
# para cada número de parcela, faz com que tenha uma nova linha
df = df.explode('numero_parcela').reset_index(drop=True)
df
# %%
# soma o numero_parcela com o mês da dtTransacao. A nova coluna criada é o
# mês de vigência da parcela a ser paga
def get_pay_month(a):
    dt = a['dtTransacao'] + pd.DateOffset(months=a['numero_parcela'])
    dt = f"{dt.year}-{dt.month}"
    return dt
df['mes_parcela'] = df.apply(get_pay_month, axis=1)
df
# %%

df_final = (df.groupby(by=['idCliente','mes_parcela'])['vlParcela']
              .sum()
              .reset_index()
              .pivot_table(values='vlParcela',
                           index='idCliente',
                           columns='mes_parcela',
                           fill_value=0)     
)
df_final.columns = (pd.to_datetime(df_final.columns)
                      .strftime('%Y-%m')
                    )
df_final = df_final[sorted(df_final.columns)]
df_final
df_final
# %%
##########################################
df_final.columns
# %%
df_final.columns = pd.to_datetime(df_final.columns).strftime("%Y-%m")
df_final = df_final[sorted(df_final.columns)]
df_final
# %%
