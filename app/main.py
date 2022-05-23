"""""""""""""""""""""""""""""""""""
        MERCADO DE TRABALHO
"""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""
          IMPORTAÇÕES
"""""""""""""""""""""""""""""""""
import os
import numpy as np
import pandas as pd
import datetime as date
import matplotlib.pyplot as plt

import functions.colnames as fcolname
import functions.cities as fcity


"""""""""""""""""""""""""""""""""
          FUNÇÕES
"""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""
       PROGRAMA PRINCIPAL
"""""""""""""""""""""""""""""""""

# Selecionando o diretório
os.getcwd()
os.chdir('D:\\Programing\\python\\nepe\\nepe-mercado-trabalho\\data')

# Criando um array para as colunas e importando os dados
colnames = ['uf','code','city']
fcolname.setColNames(colnames)

uri = 'https://github.com/nogueira-guilherme/nepe-mercado-trabalho/blob/master/Data/caged-tabela.xlsx?raw=true'
caged = pd.read_excel(uri, sheet_name='Tabela 8.1', usecols='B:EI', nrows=(5577-7), skiprows=6, names=colnames)

# Selecionando os dados de São João del-Rei
sjdr = caged[(caged['code'] == 316250)]
sjdr = sjdr.fillna(0) # substituir dos valores não identificados (nan -> 0)


# Criando um DataFrame para São João del-Rei
df_sjdr = pd.DataFrame(columns=['data', 'estoque', 'admissoes', 'desligamentos', 'saldos', 'variacao'])

# Transformando o DataFrame: colunas->linhas
fcity.getCityDataframe(sjdr, df_sjdr)

# Reiniciar os index das linhas
df_sjdr = df_sjdr.reset_index()

# Manipulação
estoque = df_sjdr['estoque']
estoque.to_excel('estoque.xlsx')