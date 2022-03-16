import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

df_gasolina_sp = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=df_gasolina_sp, x='dia', y='venda', palette='pastel')
  grafico.set(title='Preço médio gasolina em SP nos 10 primeiros dias de Julho de 2021',
              xlabel='Dia', ylabel='Preço');
  plt.savefig(fname='gasolinaSP.png', box_inches='tight')