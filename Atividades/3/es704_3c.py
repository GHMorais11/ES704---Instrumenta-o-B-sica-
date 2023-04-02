import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

# Estilo
plt.style.use('default')

# Carrega os dados do arquivo .csv
dados = pd.read_csv('Data03.csv')

# Extrai as colunas de interesse
t = dados['t']
y = dados['y']

# Define os parâmetros para a STFT
fs = 1 / (t[1] - t[0])  # Frequência de amostragem
window = 'hann'        # Janela de Hann
nperseg = 256          # Tamanho da janela
noverlap = nperseg // 2 # Sobreposição entre janelas

# Calcula a STFT de y(t)
f, t, Zxx = stft(y, fs=fs, window=window, nperseg=nperseg, noverlap=noverlap)

# Plota o espectrograma
fig, ax = plt.subplots()
im = ax.pcolormesh(t, f, np.abs(Zxx), cmap='jet')
ax.tick_params(axis='both', labelsize=14)
ax.set_xlabel('Tempo (s)', fontsize=12, fontweight='bold', labelpad=12)
ax.set_ylabel('Frequência (Hz)', fontsize=12, fontweight='bold', labelpad=12)
ax.set_title('Espectrograma de y(t)', fontsize=18, fontweight='bold', pad=20)
cbar = fig.colorbar(im)
cbar.ax.tick_params(labelsize=14)
plt.show()
