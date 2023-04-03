import numpy as np
import scipy.fft as fft
import math
import matplotlib.pyplot as plt

# Carregando dados do arquivo Data03.csv
data = np.genfromtxt('Data03.csv', delimiter=',')

# Definindo parâmetros
N = len(data)   # Número de pontos
fs = 1000       # Frequência de amostragem
t = np.arange(N) / fs  # Vetor de tempo

# Calculando a transformada de Fourier usando FFT
Y = np.fft.fft(data)

# Definir o número de componentes senoidais a serem usadas na reconstrução
n_components = 100

# Identificando as componentes espectrais
freqs = np.fft.fftfreq(N, 1/fs)   # Frequências correspondentes às componentes espectrais
idx = np.argsort(freqs)              # Ordenando as frequências
amps = 2*np.abs(Y[idx])/n_components   # Amplitudes das componentes espectrais
phases = np.angle(Y[idx])            # Fases das componentes espectrais

# Obter as amplitudes e frequências das componentes senoidais
#amplitudes = 2*np.abs(Y) / N
#frequencies = np.fft.fftfreq(N, 1 / fs)

# Gerar um array vazio para armazenar a forma de onda reconstruída
reconstructed_data = np.zeros_like(t)

# Gerar a forma de onda reconstruída usando as amplitudes e frequências das componentes senoidais
for i in range(n_components):
    reconstructed_data += (amps[i][1])* np.sin(2 * math.pi * idx[i] * t + phases[i][1])

# Plotar a forma de onda reconstruída
plt.plot(t, reconstructed_data, label='Dados reconstruídos')

plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
