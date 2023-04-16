import pandas as pd
import numpy as np
from scipy.stats import t

data = pd.read_csv("Data05_deslocamento.csv")

# número de graus de liberdade
n = 50
df = n - 1

# cálculo das médias e dos desvios padrões
mean_x = data['x'].mean()
mean_T = data['T'].mean()
mean_V = data['V'].mean()
std_x = data['x'].std(ddof=1)
std_T = data['T'].std(ddof=1)
std_V = data['V'].std(ddof=1)
stdm_x = std_x / (n**0.5)
stdm_T = std_T / (n**0.5)
stdm_V = std_V / (n**0.5)


# determinação do valor crítico t para um nível de confiança de 95% e os graus de liberdade
t_critico = t.ppf(0.975, df)

# cálculo do intervalo de confiança
intervalo = [mean_x - t_critico * stdm_x, mean_x + t_critico * stdm_x]

# exibição do resultado
print("A média do deslocamento é:  {:.6f} μm".format(mean_x))
print("A média da temperatura é:  {:.6f} \u00B0C".format(mean_T))
print("A média da tensão é:  {:.6f} V\n".format(mean_V))

print("O desvio padrão do deslocamento é:  {:.6f} μm".format(std_x))
print("O desvio padrão da temperatura é:  {:.6f} \u00B0C".format(std_T))
print("O desvio padrão da tensão é:  {:.6f} V\n".format(std_V))

print("O desvio padrão da média do deslocamento é:  {:.6f} μm".format(stdm_x))
print("O desvio padrão da da média  temperatura é:  {:.6f} \u00B0C".format(stdm_T))
print("O desvio padrão da da média  tensão é:  {:.6f} V\n".format(stdm_V))

print("O valor da distribuição t-Student é:  {:.6f}".format(t_critico))
print("A estimativa do valor real do deslocamento com nível de probabilidade de 95% SEM CONSIDERAR INCERTEZAS é:  {:.6f} ± {:.6f} μm".format(mean_x,t_critico*std_x))