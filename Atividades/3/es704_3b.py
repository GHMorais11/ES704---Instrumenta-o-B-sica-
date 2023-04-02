import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

# Plota os espectros de magnitude, fase e potência de y(t) em cada subplot
ax1.plot(frequencias, espectro_mag)
ax1.set_ylabel('Magnitude')
ax1.set_title('Espectro de magnitude, fase e potência de y(t)')

ax2.plot(frequencias, espectro_fase)
ax2.set_ylabel('Fase (rad)')

ax3.plot(frequencias, espectro_pot)
ax3.set_xlabel('Frequência (Hz)')
ax3.set_ylabel('Potência')

plt.show()
