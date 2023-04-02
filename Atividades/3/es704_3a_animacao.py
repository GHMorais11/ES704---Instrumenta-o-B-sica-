import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

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

# Define a função de atualização da animação
def update(frame):
    # Seleciona os dados até o frame atual
    t_atual = t[:frame]
    y_atual = y[:frame]
    
    # Limpa o gráfico
    plt.cla()
    
    # Plota a função y(t)
    plt.plot(t_atual, y_atual, linewidth=1)
    plt.xlabel('Tempo [s]')
    plt.ylabel('Saída')
    plt.title('Saída do Sensor y(t)')

# Cria a animação
anim = FuncAnimation(plt.gcf(), update, frames=len(t), interval=1)

# Exibe a animação
plt.show()
