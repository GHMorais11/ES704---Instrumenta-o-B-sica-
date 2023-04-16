import pandas as pd
import numpy as np
from scipy.stats import t

data = pd.read_csv("Data05_deslocamento.csv")

# cálculo da média e do desvio padrão
mean = data['x'].mean()
std = data['x'].std(ddof=1)

# número de graus de liberdade
n = 50
df = n - 1

# determinação do valor crítico t para um nível de confiança de 95% e os graus de liberdade
t_critico = t.ppf(0.975, df)

# cálculo do intervalo de confiança
intervalo = [mean - t_critico * std / (n**0.5), mean + t_critico * std / (n**0.5)]

# exibição do resultado
print("A média é:  {:.6f} μm".format(mean))
print("O desvio padrão é:  {:.6f} μm".format(std))
print("O valor da distribuição t-Student é:  {:.6f}".format(t_critico))
print("A estimativa do valor real de V com nível de probabilidade de 95% é:  {:.6f} ± {:.6f} μm".format(mean,t_critico*std))
print("O intervalo de confiança com um nível de probabilidade de 95% é:   [{:.6f} , {:.6f}] μm\n".format(intervalo[0],intervalo[1]))

