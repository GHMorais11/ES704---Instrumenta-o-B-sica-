import pandas as pd
import numpy as np
from scipy.stats import t

# Importar o arquivo .csv e subdvidir os 4 trechos
data = pd.read_csv("Data04.csv")
data_parts = np.array_split(data, 4)

#faixa a ser calculada (0=0oC; 1=20oC; 2=40oC; 3=60oC)
faixaTemperatura = 3

# cálculo da média e do desvio padrão
mean = data_parts[faixaTemperatura]['V'].mean()
std = data_parts[faixaTemperatura]['V'].std(ddof=1)

# número de graus de liberdade
n = 50
df = n - 1

# determinação do valor crítico t para um nível de confiança de 95% e os graus de liberdade
t_critico = t.ppf(0.975, df)

# cálculo do intervalo de confiança
intervalo = [mean - t_critico * std / (n**0.5), mean + t_critico * std / (n**0.5)]

# exibição do resultado
print("\nPara a temperatura {}\u00B0C:\n".format(data_parts[faixaTemperatura]['T'][faixaTemperatura*50]))
print("A média é: {:.6f} mV".format(mean))
print("O desvio padrão é: {:.6f} mV".format(std))
print("O valor da distribuição t-Student é: {:.6f}".format(t_critico))
print("O intervalo de confiança com um nível de probabilidade de 95% é: {:.6f} ± {:.6f} mV ---> {} \n".format(mean, t_critico*std, intervalo))

