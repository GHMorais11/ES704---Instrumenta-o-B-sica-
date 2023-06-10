import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parâmetros do sistema
m = 0.02  # massa
k = 405000  # constante da mola
c = 64  # coeficiente de amortecimento

# Função de transferência do sistema
num = [1]
den = [m, c, k]
sys = signal.TransferFunction(num, den)

# Resposta em frequência
w, mag, phase = signal.bode(sys)

# Plot da resposta em frequência
plt.figure()
plt.semilogx(w, mag)  # Magnitude em escala logarítmica
plt.xlabel('Frequência [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.title('Resposta em Frequência')
plt.grid(True)
plt.show()

# Resposta ao degrau
t, y = signal.step(sys)

# Plot da resposta ao degrau
plt.figure()
plt.plot(t, y)
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title('Resposta ao Degrau')
plt.grid(True)
plt.show()
