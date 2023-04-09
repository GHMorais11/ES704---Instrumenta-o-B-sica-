import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Carrega os dados do arquivo .csv
data = pd.read_csv('Data04.csv')
data_parts = np.array_split(data, 4)

# Criar um objeto figure e adicionar quatro subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
(ax1, ax2), (ax3, ax4) = axs

# Criar um histograma para cada parte dos dados em cada subplot
ax1.hist(data_parts[0]['V'], bins=10, color='blue', alpha=0.5)

ax2.hist(data_parts[1]['V'], bins=10, color='red', alpha=0.5)

ax3.hist(data_parts[2]['V'], bins=10, color='green', alpha=0.5)

ax4.hist(data_parts[3]['V'], bins=10, color='purple', alpha=0.5)

# Adicionar rótulos aos eixos
for ax in axs.flat:
    ax.set(xlabel='Tensão [mV]', ylabel='Frequência')

# Ajustar as bordas do gráfico
for ax in axs.flat:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Adicionar uma grade
for ax in axs.flat:
    ax.xaxis.label.set_weight('bold')
    ax.yaxis.label.set_weight('bold')
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Use cores e transparência
ax1.hist(data_parts[0]['V'], bins=10, color='blue', alpha=0.5, label='T = 0\u00B0C', edgecolor='black')
ax2.hist(data_parts[1]['V'], bins=10, color='red', alpha=0.5, label='T = 20\u00B0C', edgecolor='black')
ax3.hist(data_parts[2]['V'], bins=10, color='green', alpha=0.5, label='T = 40\u00B0C', edgecolor='black')
ax4.hist(data_parts[3]['V'], bins=10, color='purple', alpha=0.5, label='T = 60\u00B0C', edgecolor='black')
for ax in axs.flat:
    ax.legend(fontsize=12)

# Ajustar as fontes
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['font.size'] = 14

# Adicionar um título informativo
fig.suptitle('Calibração Sensor de Temperatura', fontsize=20, color='black', fontweight='bold')

# Exibir a figura
plt.show()
