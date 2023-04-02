import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Estilo
plt.style.use('default')

# Carrega os dados do arquivo .csv
dados = pd.read_csv('Data03.csv')

# Extrai as colunas de interesse
t = dados['t']
y = dados['y']

# Calcula o valor médio de y(t)
valor_medio = np.mean(y)
print('Valor médio de y(t):', valor_medio)

# Calcula o valor rms de y(t)
valor_rms = np.sqrt(np.mean(y**2))
print('Valor rms de y(t):', valor_rms)

# Plota a função y(t)
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim([0, max(t)])
ax.tick_params(axis='both', labelsize=20)
ax.plot(t, y, linewidth=1.5, color='blue') 
ax.set_xlabel('Tempo [s]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_ylabel('Saída []', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_title('Saída do Sensor y(t)', fontsize=34, color='black', fontweight='bold', pad=20) 
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5) 

# Imprime os valores de valor_rms e valor_medio na janela do gráfico
ax.text(0.01, 0.95, f'Valor médio: {valor_medio:.8f}\nValor RMS: {valor_rms:.8f}',
        transform=ax.transAxes, fontsize=18, verticalalignment='top')

fig.tight_layout() 
plt.show()
