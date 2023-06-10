import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def plot_bode(m, k, c):
    # Cria a função de transferência do sistema massa-mola-amortecedor
    num = [1]
    den = [m, c, k]
    sys = signal.TransferFunction(num, den)

    # Define o intervalo de frequência
    frequencies = np.logspace(0, 6, num=1000)

    # Calcula a resposta em frequência
    w, mag, phase = signal.bode(sys, frequencies)

    # Compensação da magnitude
    reference_gain = -72  # Ganho de referência em dB
    mag -= reference_gain

    # Plota o diagrama de Bode
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    ax1.semilogx(w, mag)
    ax1.set_title('Diagrama de Bode - Magnitude')
    ax1.set_xlabel('Frequência [rad/s]')
    ax1.set_ylabel('Magnitude [dB]')
    ax1.grid(True, which='both')

    ax2.semilogx(w, phase)
    ax2.set_title('Diagrama de Bode - Fase')
    ax2.set_xlabel('Frequência [rad/s]')
    ax2.set_ylabel('Fase [graus]')
    ax2.grid(True, which='both')

    plt.tight_layout()
    plt.show()

# Valores fornecidos
massa = 0.02
constante_mola = 405000
constante_amortecedor = 64

# Chama a função para plotar o diagrama de Bode
plot_bode(massa, constante_mola, constante_amortecedor)
