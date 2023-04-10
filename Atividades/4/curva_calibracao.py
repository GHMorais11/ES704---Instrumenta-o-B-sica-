import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Estilo
plt.style.use('default')

# Importar o arquivo .csv e subdvidir os 4 trechos
data = pd.read_csv("Data04.csv")
data_parts = np.array_split(data, 4)

# cálculo da média de cada intervalo
mean = []
for i in range(4):
    mean.append(data_parts[i]['V'].mean())

#Pares VxT
V = mean
T = [0,20,40,60]

# Cálculo dos coeficientes da linha de tendência
coefs = np.polyfit(T, V, 1) # grau 1 para uma linha reta

# Criação dos valores da linha de tendência
trendline = np.polyval(coefs, T)

# Plot do gráfico de dispersão com linha de tendência
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim([-5,65])
ax.tick_params(axis='both', labelsize=20)

ax.set_xlabel('Temperatura [\u00B0C]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_ylabel('Tensão [mV]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_title('Curva de Calibração Sensor de Temperatura', fontsize=24, color='black', fontweight='bold', pad=20) 
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5) 

plt.plot(T, V, 'o', label='Valores Medidos')
plt.plot(T, trendline, '-', label='Linha de Tendência')
plt.legend(fontsize=16)
plt.show()
