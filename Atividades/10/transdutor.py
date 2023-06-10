import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
data = pd.read_csv('Data10.csv')

# Obter os valores de tensão em mV
tensao = data

# Converter a tensão em posição
posicao = (tensao/1000)/200  # Converter mV para V usando o ganho K

# Calcular o tempo em segundos
tempo = data.index / 1000  # Taxa de aquisição é 1 kHz, então dividimos por 1000

# Plotar o gráfico posição x tempo
plt.plot(tempo, posicao)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Posição em função do tempo')
plt.grid(True)
plt.show()
