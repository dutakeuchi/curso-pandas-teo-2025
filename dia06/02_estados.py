# %%
import pandas as pd
# %%
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

dfs = pd.read_html(url)
dfs
# %%
len(dfs)
# %%
uf = dfs[1]
# %%
# função para converter str para float e remover itens necessários para isso
def str_to_float(x):
    x = float(x.replace(" ","")
               .replace(",",".")
               .replace("\xa0","")
                )
    return x
# %%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
# %%
# função para converter a idade para float
def anos_to_float(x):
    x = float(x.replace(",",".")
               .replace(" anos",""))
    return x
# %%
uf['Expectativa de vida (2016)'] = uf['Expectativa de vida (2016)'].apply(anos_to_float)
# %%
# função para converter porcentagem para float
def porcent_to_float(x):
    x = float(x.replace(",",".")
              .replace("%","")
              )
    return x
# %%
uf['Alfabetização (2016)'] = uf['Alfabetização (2016)'].apply(porcent_to_float)
uf.rename(columns={'Alfabetização (2016)':'Alfabetização em % (2016)'},
          inplace=True)
# %%
# função para converter as mortes 
def morte_por_mil(x):
    x = float(x.replace("‰","").replace(",","."))
    return x
# %%
uf['Mortalidade infantil (2016)'] = uf['Mortalidade infantil (2016)'].apply(morte_por_mil)
uf.rename(columns = {'Mortalidade infantil (2016)': 'Mortalidade infantil a cada mil (2016)'}, inplace=True)
# %%
# função para definir a região do Estado
def regiao_brasil_2(estado):
    if estado in ['Distrito Federal', 'Goiás','Mato Grosso', 'Mato Grosso do Sul']:
        return 'Região Centro-Oeste'
    
    elif estado in ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']:
        return 'Nordeste'
    
    elif estado in ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins']:
        return 'Norte'
    
    elif estado in ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo']:
        return 'Sudeste'
    
    elif estado in ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']:
        return 'Sul'
    
    else:
        return 'Erro'
# %%
uf['Região do pais'] = uf['Unidade federativa'].apply(regiao_brasil)
# %%
uf

# %%
# PIB / capita > 30.000
# IDH > 650
# mortalidade infantil < 15/1000
# PARECE BOM

# caso contrário, NÃO PARECE BOM
cond = (uf['PIB per capita (R$) (2015)'] > 15000) & (uf['IDH (2010)'] > 650) & (uf['Mortalidade infantil a cada mil (2016)']< 15)

def bom_lugar(condicoes):
    if condicoes:
        return "Parece bom "
    else:
        return 'Parece ruim'
    
uf['Avaliação'] = cond.apply(bom_lugar)
uf
# %%
uf.sort_values(by='IDH (2010)', ascending=False)
# %%
# DADOS DA BOLÍVIA
# PIB per capita de U$ 3670 em 2019. Considerando o dolar a média de 4 reais, PIB per capita de R$ 14680.00
# IDH de 0.733 em 2019
# mortalidade de 10.1 em 2000. Em 2019 estava em 7.9 na qual nenhum estado atende ao critério

cond = (uf['PIB per capita (R$) (2015)'] > 14680) & (uf['IDH (2010)'] > 733) & (uf['Mortalidade infantil a cada mil (2016)']< 10.1)
uf[cond]

# apenas Espírito Santo, Paraná, Rio Grande do Sul, Santa Catarina e São Paulo atendem aos critérios expostos
# %%
