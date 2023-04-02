import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt

# Carregando dados do arquivo Data03.csv
data = np.genfromtxt('Data03.csv', delimiter=',')

# Definindo parâmetros
N = len(data)   # Número de pontos
fs = 1000       # Frequência de amostragem
t = np.arange(N) / fs  # Vetor de tempo

# Calculando a transformada de Fourier usando FFT
Y = np.fft.fft(data)

# Identificando as componentes espectrais
freqs = np.fft.fftfreq(N, 1/fs)   # Frequências correspondentes às componentes espectrais
idx = np.argsort(freqs)        # Ordenando as frequências
amps = np.abs(Y[idx])          # Amplitudes das componentes espectrais
phases = np.angle(Y[idx])      # Fases das componentes espectrais

# Criando as ondas senoidais correspondentes às componentes espectrais
#tiled_freqs = np.tile(freqs, (N, 1)).T   # Replicando as frequências para criar as ondas senoidais
sin_wave = np.sum(amps * np.exp(1j * phases) * np.exp(2j * np.pi * freqs * t), axis=1)  # Criando as ondas senoidais

# Somando as ondas senoidais criadas para obter a aproximação do sinal original
approx_signal = np.sum(sin_wave)

# Plotando o sinal original e a aproximação
plt.plot(t, data, label='Original Signal')
plt.plot(t, approx_signal.real, label='Approximated Signal')
plt.legend()
plt.show()
