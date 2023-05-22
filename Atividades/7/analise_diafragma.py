import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import spectrogram

# Nome do arquivo CSV
nome_arquivo = 'Data07.csv'

# Lista para armazenar os valores de deflexão
valores_deflexao = []

# Leitura do arquivo CSV e extração dos valores de deflexão
with open(nome_arquivo, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        valor = float(linha[0])  # Supondo que os valores sejam números
        valores_deflexao.append(valor)

# Cálculo do vetor de tempo
frequencia = 100  # Frequência em Hz
tempo = np.arange(len(valores_deflexao)) / frequencia

# converte a deflexão de mm para metro
valores_deflexao_metro = np.array(valores_deflexao) / 1000

# Cálculo do vetor de pressão
fator_conversao = 7.6526e-14
valores_pressao = np.array(valores_deflexao_metro) / fator_conversao

# Cálculo do vetor de força
raio = 3  # Raio da região circular em mm
area = np.pi * (raio ** 2)  # Área da região circular em mm^2
valores_forca = valores_pressao * area

# Gráfico da pressão
plt.figure()
plt.plot(tempo, valores_pressao)
plt.title('Gráfico da Pressão ao longo do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Pressão (Pa)')

# Cálculo das estatísticas da pressão
pressao_maxima = np.max(valores_pressao)
pressao_media = np.mean(valores_pressao)
pressao_rms = np.sqrt(np.mean(np.square(valores_pressao)))

# Impressão das estatísticas da pressão
print(f"\nPressão Máxima: {pressao_maxima:.2e} Pa")
print(f"Pressão Média: {pressao_media:.2e} Pa")
print(f"Pressão RMS: {pressao_rms:.2e} Pa\n")

# Exibição do gráfico da pressão em uma janela separada
plt.show()

# Gráfico da força
plt.figure()
plt.plot(tempo, valores_forca)
plt.title('Gráfico da Força ao longo do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Força (N)')

# Cálculo das estatísticas da força
forca_maxima = np.max(valores_forca)
forca_media = np.mean(valores_forca)
forca_rms = np.sqrt(np.mean(np.square(valores_forca)))

# Impressão das estatísticas da força
print(f"Força Máxima: {forca_maxima:.2f} N")
print(f"Força Média: {forca_media:.2f} N")
print(f"Força RMS: {forca_rms:.2f} N\n")

# Exibição do gráfico da força em uma janela separada
plt.show()

# Cálculo da Transformada de Fourier
fft_values = np.fft.fft(valores_pressao)
freq = np.fft.fftfreq(len(valores_pressao), 1 / frequencia)

# Gráfico da magnitude da Transformada de Fourier
plt.figure()
plt.plot(freq, np.abs(fft_values))
plt.title('Espectro de Frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, frequencia / 2)  # Mostrar apenas até a metade do espectro (frequências positivas)
plt.grid(True)

# Exibição do gráfico do espectro de frequência
plt.show()

# Parâmetros da janela de análise
window = 'hann'  # Tipo de janela (pode ser 'hann', 'hamming', 'blackman', etc.)
window_size = 128  # Tamanho da janela
overlap = 0.5  # Porcentagem de sobreposição entre janelas adjacentes

# Cálculo do espectrograma
frequencies, times, spectrogram_vals = spectrogram(valores_pressao, fs=frequencia, window=window,
                                                  nperseg=window_size, noverlap=int(window_size * overlap))

# Plot do espectrograma
plt.figure()
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_vals), shading='auto')
plt.colorbar(label='Magnitude (dB)')
plt.title('Espectrograma')
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')

# Define o intervalo do eixo das frequências
freq_min = 0  # Frequência mínima desejada
freq_max = 20 # Frequência máxima desejada
plt.ylim(freq_min, freq_max)

# Exibição do espectrograma
plt.show()
