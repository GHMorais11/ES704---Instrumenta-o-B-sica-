import csv
import matplotlib.pyplot as plt
import numpy as np

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
print(f"Pressão Máxima: {pressao_maxima:.2e} Pa")
print(f"Pressão Média: {pressao_media:.2e} Pa")
print(f"Pressão RMS: {pressao_rms:.2e} Pa")

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
print(f"Força RMS: {forca_rms:.2f} N")

# Exibição do gráfico da força em uma janela separada
plt.show()
