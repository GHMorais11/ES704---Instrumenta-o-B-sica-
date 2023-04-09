import pandas as pd
import numpy as np
from scipy.stats import t

# Importar o arquivo .csv
data = pd.read_csv("Data04.csv")
data_parts = np.array_split(data, 4)

# Calcular a média e o desvio padrão de V
media = np.mean(data_parts[0]['V'])
desvio_padrao = np.std(data_parts[0]['V'], ddof=1)

# Calcular o intervalo de confiança de 95% para a média
n = len(data_parts[0]['V'])
erro_padrao = desvio_padrao / np.sqrt(n)
intervalo_confianca = media + t.ppf(0.025, n - 1) * erro_padrao, media + t.ppf(0.975, n - 1) * erro_padrao

# Imprimir o resultado
print("A estimativa do valor real de V com um nível de probabilidade de 95% é:", intervalo_confianca)
