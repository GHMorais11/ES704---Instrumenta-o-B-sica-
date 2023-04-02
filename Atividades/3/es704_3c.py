import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

plt.style.use('dark_background')

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
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Frequência (Hz)')
ax.set_title('Espectrograma de y(t)')
fig.colorbar(im)
plt.show()
