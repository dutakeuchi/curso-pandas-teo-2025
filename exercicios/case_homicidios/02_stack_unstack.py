# %%
import pandas as pd
# %%
df = pd.read_csv("../../data/homicidio_consolidado.csv")
df
# %%
df_stack = (df.set_index(['nome','período'])
              .stack()
              .reset_index()
              .rename(columns={'level_2':'métrica',
                               0:'valor'})
            )
df_stack

# %%
df_unstack = (df_stack.set_index(['nome','período','métrica'])
                      .unstack()
                      .reset_index()
                      
                      )

df_unstack
# %%
colunas = df_unstack.columns.droplevel()[2:].tolist() # converte as colunas de df_unstack, retirando o multiindex, e ignorando os dois primeiros(são vazios) e trasnforma em uma lista
colunas = ['nome','período',] + colunas # cria uma nova lista com o nome das colunas desejadas
df_unstack.columns = colunas # renomeia os colunas do df com os nomes criados acima
df_unstack

# %%
(df_stack.pivot_table(values='valor',
                     index=['nome','período'], 
                     columns=['métrica'] )
         .reset_index()
)
# %%
