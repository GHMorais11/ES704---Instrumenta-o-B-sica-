import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Saída do Sensor y(t)')
plt.show()
