import numpy as np
import math
import matplotlib.pyplot as plt

# Definir o número de ponto
n_points = 100

# Definir a frequência da função seno
freq = 10

# Gerar um array de valores de tempo
time = np.linspace(0, 10, n_points)

# Gerar o conjunto de dados com base na função seno e ruído aleatório
data = np.sin(2 * math.pi * freq * time) + 0.1 * np.random.randn(n_points)

# Plotar os dados gerados
plt.plot(time, data, label='Dados originais')

# Calcular a FFT dos dados
fft_data = np.fft.fft(data)

# Obter as amplitudes e frequências das componentes senoidais
amplitudes = np.abs(fft_data) / n_points
frequencies = np.fft.fftfreq(n_points, 1 / n_points)

# Definir o número de componentes senoidais a serem usadas na reconstrução
n_components = 10

# Gerar um array vazio para armazenar a forma de onda reconstruída
reconstructed_data = np.zeros_like(data)

# Gerar a forma de onda reconstruída usando as amplitudes e frequências das componentes senoidais
for i in range(n_components):
    reconstructed_data += amplitudes[i] * np.cos(2 * math.pi * frequencies[i] * time)

# Plotar a forma de onda reconstruída
plt.plot(time, reconstructed_data, label='Dados reconstruídos')

plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
