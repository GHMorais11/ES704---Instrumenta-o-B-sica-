import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fator_gauge = 2.2
tensao_fonte = 12

# Carregar dados do arquivo CSV
dados = pd.read_csv("Data09.csv")

# Converter tensão de saída para deformação
d = (dados["Tensao(mV)"] / 1000) / (fator_gauge * tensao_fonte)
deformacao = d * 1000000  # micrometros
dadosmili = dados["Tensao(mV)"]

# Calcular a média da deformação
media_deformacao = np.mean(deformacao)

# Calcular a sensibilidade (slope) da curva de calibração
sensibilidade = (deformacao.iloc[-1] - deformacao.iloc[0]) / (dados.index[-1] - dados.index[0])

# Calcular a faixa dinâmica
faixa_dinamica = deformacao.max() - deformacao.min()

# Calcular a resolução do sensor
resolucao = np.std(deformacao)

# Traçar a curva de calibração de deformação versus tempo
plt.plot(dadosmili, deformacao, label="Dados de Deformação")
plt.xlabel("Tensão (mV)")
plt.ylabel("Deformação (µm)")
plt.title("Curva de Calibração: Deformação x Tensão")
plt.grid(True)

# Ajustar um polinômio de grau 1 (linear) aos dados
coef = np.polyfit(dadosmili, deformacao, 2)
tendencia = np.poly1d(coef)

# Imprimir os resultados
print("Sensibilidade: ", sensibilidade, "µm/mV")
print("Faixa Dinâmica: ", faixa_dinamica, "µm")
print("Resolução: ", resolucao, "µm")

# Mostrar a legenda
plt.legend()

# Exibir o gráfico
plt.show()
