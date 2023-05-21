import pandas as pd
import numpy as np
from scipy.stats import t

data = pd.read_csv("Data06_temperatura.csv")

# número de graus de liberdade
n = 1000
df = n - 1

# cálculo das médias e dos desvios padrões
mean_e13 = data['e13'].mean()
mean_T = data['T'].mean()
std_e13 = data['e13'].std(ddof=1)
std_T = data['T'].std(ddof=1)
stdm_e13 = std_e13 / (n**0.5)
stdm_T = std_T / (n**0.5)

# determinação do valor crítico t para um nível de confiança de 95% e os graus de liberdade
t_critico = t.ppf(0.975, df)

# cálculo do intervalo de confiança
intervalo = [mean_e13 - t_critico * stdm_e13, mean_e13 + t_critico * stdm_e13]

# exibição do resultado
print("A média da tensão é:  {:.6f} mV".format(mean_e13))
print("A média da temperatura é:  {:.6f} \u00B0C".format(mean_T))

print("O desvio padrão da tensão é:  {:.6f} mV".format(std_e13))
print("O desvio padrão da temperatura é:  {:.6f} \u00B0C".format(std_T))

print("O desvio padrão da média da tensão é:  {:.6f} mV".format(stdm_e13))
print("O desvio padrão da da média  temperatura é:  {:.6f} \u00B0C".format(stdm_T))

print("O valor da distribuição t-Student é:  {:.6f}".format(t_critico))
print("A estimativa do valor real da temperatura com nível de probabilidade de 95% SEM CONSIDERAR INCERTEZAS é:  {:.6f} ± {:.6f} °C".format(mean_T,t_critico*std_T))