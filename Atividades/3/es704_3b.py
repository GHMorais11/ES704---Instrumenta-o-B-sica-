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

# Calcula a transformada de Fourier de y(t) usando o algoritmo FFT
fft_y = np.fft.fft(y)

# Calcula o espectro de magnitude e de fase de y(t)
espectro_mag = abs(fft_y)
espectro_fase = np.angle(fft_y)

# Calcula o espectro de potência de y(t)
espectro_pot = espectro_mag**2

# Calcula as frequências correspondentes aos índices do espectro
frequencias = np.fft.fftfreq(len(y), d=t[1]-t[0])

# Cria uma figura com três subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# Plota os espectros de magnitude, fase e potência de y(t) em cada subplot
ax1.plot(frequencias, espectro_mag, linewidth=1, color='blue')
ax1.set_ylabel('Magnitude', fontsize=16, color='black', labelpad=12, fontweight='bold')
ax1.set_title('Espectro de magnitude, fase e potência de y(t)', fontsize=20, color='black', fontweight='bold', pad=20)
ax1.tick_params(axis='both', labelsize=12)
ax1.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

ax2.plot(frequencias, espectro_fase, linewidth=1, color='green')
ax2.set_ylabel('Fase (rad)', fontsize=16, color='black', labelpad=12, fontweight='bold')
ax2.tick_params(axis='both', labelsize=12)
ax2.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

ax3.plot(frequencias, espectro_pot, linewidth=1, color='orange')
ax3.set_xlabel('Frequência (Hz)', fontsize=16, color='black', labelpad=12, fontweight='bold')
ax3.set_ylabel('Potência', fontsize=16, color='black', labelpad=12, fontweight='bold')
ax3.tick_params(axis='both', labelsize=12)
ax3.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

plt.tight_layout()
plt.show()
