# %%
import pandas as pd
import os
# %%
data = (pd.read_csv('../data/ipea/homicidios.csv', sep=';')
        .set_index(['nome','período'])
        .drop(['cod'], axis=1)
        .rename(columns={'valor':'homicidios'})
        )
data
# %%
data2 = pd.read_csv('../data/ipea/homicidios-mulheres-negras.csv', sep=";")
data2
# %%
data2 = (pd.read_csv('../data/ipea/homicidios-mulheres-negras.csv', sep=';')
        .set_index(['nome','período'])
        .drop(['cod'], axis=1)
        .rename(columns={'valor':'homicidios-mulheres-negras'})
        )
data2
# %%
def get_homicidio(csv: str):
    data = (pd.read_csv(f'../data/ipea/{csv}.csv', sep=';')
            .set_index(['nome','período'])
            .drop(['cod'], axis=1)
            .rename(columns={'valor':csv})
    )
    return data
# %%
file_name = os.listdir('../data/ipea/')
file = []
for i in file_name:
    name = i.split('.')[0]
    file.append(get_homicidio(name))
file
# %%
data_atualizada = pd.concat(file, axis=1).sort_values(['período','nome']).reset_index()
data_atualizada
# %%
filtro = ['nome','homicidios-nao-negros','homicidios-negros',]
data_negros_2021 = data_atualizada[data_atualizada['período']==2021][filtro]
# %%
raca = (pd.read_csv('../data/pov_raça_genero.csv', sep=';')
          .rename(columns={'Unnamed: 1':'estado',
                           'Unnamed: 2':'total',
                           'Unnamed: 3':'branca',
                           'Unnamed: 4':'preta',
                           'Unnamed: 5':'amarela',
                           'Unnamed: 6':'parda',
                           'Unnamed: 7':'indigena',})
          .drop(range(0,4), axis='index')
          .drop(range(32,37), axis='index')
          .reset_index()
          .drop(columns = ['index','Tabela 9605 - População residente, por cor ou raça, nos Censos Demográficos',])

       )
raca
# %%
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'
uf = pd.read_html(url)

uf = uf[1][['Unidade federativa','Abreviação']]
uf
# %%
# data_negros_2021
# raca
# uf
# %%
def str_to_int(valor):
    valor = int(valor)
    return valor

filtro = ['total','branca','preta','parda','amarela','indigena',]
for i in filtro:
    raca[i] = raca[i].apply(str_to_int)

raca['preta_parda'] = raca[['preta','parda',]].sum(axis=1)
raca['nao_preta'] = raca[['branca','amarela','indigena']].sum(axis=1)
raca.drop(columns=['branca','preta','amarela','parda','indigena'])
# %%
raca['preta_parda %'] = round((raca['preta_parda'] / raca['total']), 3)
raca['nao_preta %'] = round((raca['nao_preta'] / raca['total']), 3)
raca['populacao_preta/nao_preta %'] = round((raca['preta_parda'] / raca['nao_preta'] ), 3)
raca.drop(columns=['total','branca','preta','amarela','parda','indigena','preta_parda','nao_preta'], inplace=True)
raca
# %%
data_negros_2021['homicidio_negro/homicidio_nao_negro'] = round((data_negros_2021['homicidios-negros'] / data_negros_2021['homicidios-nao-negros']), 3)
data_negros_2021
# %%
uf = uf.merge(data_negros_2021, left_on='Abreviação', right_on='nome', how='left')  
# %%
raca
# %%
uf = uf.merge(raca, left_on='Unidade federativa',right_on='estado')
# %%
uf.drop(columns = ['Abreviação','nome','estado', 'homicidios-nao-negros','homicidios-negros','preta_parda %','nao_preta %'], inplace=True)
# %%
uf
# %%
raca
# %%
uf.assign(teste=lambda uf: uf['homicidio_negro/homicidio_nao_negro'] + 6)
# %%
data_atualizada.to_csv('../data/homicidio_consolidado.csv', index=False)
# %%
data_atualizada
# %%
