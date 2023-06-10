import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
data = pd.read_csv('Data10.csv')

# Obter os valores de tensão em mV
tensao = data

# Converter a tensão em posição
posicao = (tensao / 1000) / 200  # Converter mV para V usando o ganho K

# Calcular o tempo em segundos
tempo = data.index / 1000  # Taxa de aquisição é 1 kHz, então dividimos por 1000

# Calcular a velocidade em função do tempo
velocidade = posicao.diff() / (tempo[1] - tempo[0])

# Calcular a aceleração em função do tempo
aceleracao = velocidade.diff() / (tempo[1] - tempo[0])

# Configurar o layout dos subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# Plotar o gráfico posição x tempo
ax1.plot(tempo, posicao)
ax1.set_ylabel('Posição (m)')
ax1.set_title('Posição em função do tempo')

# Plotar o gráfico velocidade x tempo
ax2.plot(tempo, velocidade)
ax2.set_ylabel('Velocidade (m/s)')
ax2.set_title('Velocidade em função do tempo')

# Plotar o gráfico aceleração x tempo
ax3.plot(tempo, aceleracao)
ax3.set_xlabel('Tempo (s)')
ax3.set_ylabel('Aceleração (m/s^2)')
ax3.set_title('Aceleração em função do tempo')

# Ajustar o espaçamento entre os subplots
plt.tight_layout()

# Exibir o gráfico
plt.show()
