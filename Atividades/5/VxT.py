import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Estilo
plt.style.use('default')

# Carrega os dados do arquivo .csv
dados = pd.read_csv('Data05.csv')

# ordenar os valores por uma coluna específica
dados_sorted = dados.sort_values(by='T')

# criar um novo arquivo csv com os valores ordenados
dados_sorted.to_csv('Data05_sorted.csv', index=False)

# Extrai as colunas de interesse
T = dados_sorted['T']
V = dados_sorted['V']

# Plota a função y(t)
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim([0, max(T)])
ax.tick_params(axis='both', labelsize=20)
ax.plot(T, V, linewidth=1.5, color='blue') 

ax.set_xlabel('Temperatura [\u00B0C]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_ylabel('Tensão [mV]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_title('Calibração Sensor de Temperatura', fontsize=28, color='black', fontweight='bold', pad=20) 
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5) 

fig.tight_layout() 
plt.show()
