import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Carregar dados do arquivo .csv
df = pd.read_csv('Tabela01.csv')
data = df[['x', 't1', 't2', 't3']]

# Definir cores e marcadores para cada conjunto de dados
markers = ['o', '^', 's']
temps = ['20\u00B0C','40\u00B0C','60\u00B0C']

# Criar gráfico de dispersão com linhas de tendência para cada conjunto de dados
fig, ax = plt.subplots(figsize=(12, 8))
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5) 
for i in range(1, 4):
    tn = data.iloc[:, i] # selecione a coluna tn
    slope, intercept, r_value, p_value, std_err = linregress(data['x'], tn)
    line = slope * data['x'] + intercept # calcule a linha de tendência
    plt.scatter(data['x'], tn, marker=markers[i-1], label=temps[i-1]) # crie o gráfico de dispersão
    plt.plot(data['x'], line, label='Equação: y = {:.2f}x + {:.2f}'.format(slope, intercept)) # adicione a linha de tendência
    plt.legend(fontsize=16) # adicione a legenda
    plt.title('Curvas de Tensão x Deslocamento', fontsize=24, color='black', fontweight='bold', pad=20) # adicione o título do gráfico
    plt.xlabel('Deslocamento [μm]',fontsize=18, color='black', labelpad=12, fontweight='bold') # adicione o rótulo do eixo x
    plt.ylabel('Tensão [V]',fontsize=18, color='black', labelpad=12, fontweight='bold') # adicione o rótulo do eixo y

# Obter os coeficientes angulares das linhas de tendência para as diferentes temperaturas
temperaturas = [20, 40, 60]
slopes = []
for i in range(1, 4):
    tn = data.iloc[:, i]
    slope, intercept, r_value, p_value, std_err = linregress(data['x'], tn)
    slopes.append(slope)

# Criar gráfico de dispersão para os coeficientes angulares
fig, ax = plt.subplots(figsize=(12, 8))
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5) 
plt.scatter(temperaturas, slopes, marker='o', label='Coeficientes angulares') # criar gráfico de dispersão
slope, intercept, r_value, p_value, std_err = linregress(temperaturas, slopes) # calcular a linha de tendência
line = slope * np.array(temperaturas) + intercept # calcular a linha de tendência
plt.plot(temperaturas, line, label='Equação: y = {:.2f}x + {:.2f}'.format(slope, intercept)) # adicionar a linha de tendência
plt.legend(fontsize=16) # adicionar a legenda
plt.title('Sensibilidade Estática em função da temperatura', fontsize=24, color='black', fontweight='bold', pad=20) # adicionar o título do gráfico
plt.xlabel('Temperatura [\u00B0C]',fontsize=18, color='black', labelpad=16, fontweight='bold') # adicionar o rótulo do eixo x
plt.ylabel('Sensibilidade Estática [V/\u00B0C]',fontsize=18, color='black', labelpad=12, fontweight='bold') # adicionar o rótulo do eixo y

plt.show() # exiba o gráfico
