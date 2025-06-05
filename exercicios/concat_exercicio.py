# %%
import pandas as pd
import os
# %%
# dataframe com os estados e suas abreviações
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'
uf = pd.read_html(url)
uf = uf[1][['Unidade federativa','Abreviação']]
# %%
# dataframe com a distribuição da população brasileira no ano de 2021, separado por estado e  raça
# organizado para mostar a porcentagem da população dividido entre preta/parda e não preta
raca = (pd.read_csv('../data/pov_raça_genero.csv', sep=';')
        .rename(columns = {'Unnamed: 1' : 'estado',})
        #                    'Unnamed: 2' : 'total',
        #                    'Unnamed: 3' : 'branca',
        #                    'Unnamed: 4' : 'preta',
        #                    'Unnamed: 5' : 'amarela',
        #                    'Unnamed: 6' : 'parda',
        #                    'Unnamed: 7' : 'indigena',})
        .drop(range(0,4))
        .drop(range(32,37))
        .assign(**{'populacao_preta_parda %' : lambda raca: round((raca['Unnamed: 4'].astype(int) + raca['Unnamed: 6'].astype(int)) / raca['Unnamed: 2'].astype(int), 3)})
        .assign(**{'populacao_nao_preta %' : lambda raca: round((raca['Unnamed: 3'].astype(int) + raca['Unnamed: 5'].astype(int) + raca['Unnamed: 7'].astype(int)) / raca['Unnamed: 2'].astype(int), 3)})
        .assign(**{'taxa população (preta / nao_preta)' : lambda raca: round((raca['populacao_preta_parda %'] / raca['populacao_nao_preta %']), 3)})
        .drop(columns=['Tabela 9605 - População residente, por cor ou raça, nos Censos Demográficos','Unnamed: 2',
                       'Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7'])
        )
# %%
# dataframe com a taxa de homicidios desde o ano de 1979, dividido por estados e separados por gênero e raça
# organizado para mostrar $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def get_data(valor):
    data = (pd.read_csv(f'../data/ipea/{valor}',sep=';')
            .rename(columns = {'valor': valor.split('.')[0]})
            .drop(columns='cod')
            .set_index(['nome','período'])

            )
    return data

dados = os.listdir('../data/ipea/')
lista = []
for i in dados:
    data = get_data(i)
    lista.append(data)

homicidios = (
    pd.concat(lista, axis=1)
      .reset_index() # reseta o index. O index atual está organizado por nome e periodo
    #   .sort_values(['período','nome'])
      .loc[lambda df: df['período']==2021,] # seleciona os dados do periodo de 2021
      .reset_index(drop=True) # reseta o index, pois ao selecionar o periodo de 2021, o index está bagunçado. Drop para que o index atual não seja adicionado ao df
      .assign(**{'homicidios-nao-negros %' : lambda df: round(df['homicidios-nao-negros']/(df['homicidios-nao-negros'] + df['homicidios-negros']), 3)},
              **{'homicidios-negros %' : lambda df: round(df['homicidios-negros'] / (df['homicidios-negros'] + df['homicidios-nao-negros']), 3)},
              **{'taxa homicidio (negro / nao negro)' : lambda df: round(df['homicidios-negros'] / df['homicidios-nao-negros'], 3)}
              ) # criação de duas colunas seguindo o cálculo acima
      .filter(['nome','homicidios-negros %','homicidios-nao-negros %','taxa homicidio (negro / nao negro)']) # selecionando somente as colunas criadas

)
# %%
dados = (uf.merge(raca, left_on="Unidade federativa", right_on='estado')
           .merge(homicidios, left_on='Abreviação',right_on='nome')
           .drop(columns=['Abreviação','estado','nome'])
           .assign(**{'proporcao homicidios' : lambda df: df['taxa homicidio (negro / nao negro)'] / df['taxa população (preta / nao_preta)']})
           .filter(['Unidade federativa','taxa população (preta / nao_preta)','taxa homicidio (negro / nao negro)', 'proporcao homicidios'])
           .sort_values(['proporcao homicidios'], ascending=False)
        )

dados

# %%
# Legenda:
# Unidade federativa: unidade federativa referente aos dados obtidos

# taxa população (preta / nao_preta): razão entre a população preta e a não preta. Exemplo para Alagoas, para cada pessoa não preta, há 2.322 pretas

# taxa homicidio (negro / nao negro): razão entre a taxa de homidicios. Exemplo para Alagoas, para cada homicídios de um pessoa não negra, há 87.000 homidícios de pessoas negras

# proporcao homidicios: razão entre a taxa de homicídios com a taxa da população. Quanto mais próximo de 1.0, mais proporcional é a taxa de homicídios de negros comparando
# com a taxa da população. Exemplo para Alagoas, houve 37.46 vezes mais homicídios de negros, comparando com a proporcionalidade da população negra/não negra

# Análise:
# A partir dos dados obtidos, observamos que em todos os estados, há mais homicídios de pessoas negras mesmo quando comparado proporcionalmente com a distribuição
# da raça da poopulação. 
# As maiores disparidades na proporção vem, principalmente, das região Norte e Nordeste. Diversos fatores poderia explicar tal situação, tais como menor renda, menor 
# escolaridade, condições precárias de trabalho, mas que seria necessária uma melhor análise, que não é possível com os dados obtidos.
# Mesmo na região Sul, onde a população negra é bem menos do que metade da população, houve mais homicídios de negros. Uma parcela consideravelmente menor da população
# representou mais da metade dos homicídios registrados.