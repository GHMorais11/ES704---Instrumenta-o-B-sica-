import numpy as np
import matplotlib.pyplot as plt

Q = [16.96e-4, 25.44e-4, 33.92e-4]
d_1 = 0.06
rho = 998
vc = 9e-7

d_0 = np.linspace(0.02, 0.06, 100)  # Valores de d0 para o gráfico
P = []

for q in Q:
    area_orificio = np.pi * (d_0 / 2) ** 2
    b = d_0 / d_1
    Re = (4 * q) / (np.pi * d_1 *vc)
    k = (1 / ((1 - b ** 4) ** 0.5)) * (0.5959 + (0.0312 * (b ** 2.1)) - (0.184 * (b ** 8)) + (91.71 * (b ** 2.5)) * (Re **-0.75))
    p = ((q / (k*area_orificio)) ** 2) * rho/2
    P.append(p)

# Conversao de unidade
P = np.array(P) / 1000
d_0 = np.array(d_0) * 100

# Plotando as curvas para diferentes valores de Q
for i, q in enumerate(Q):
    plt.plot(d_0, P[i], label='$Q = {:.2f} \cdot 10^{{-4}} m^3/s$'.format(q*10000))

plt.axhline(y=24680/1000, color='r', linestyle='--', label='$P_{max} = 24.68 kPa$')
plt.axvline(x=0.0325*100, color='black', linestyle='--', label='$d_0 = 3.25 cm$')

plt.xlabel('$d_0 [cm]$')
plt.ylabel('$P [kPa]$')
plt.legend(loc='best', fancybox=True, shadow=True, framealpha=1, fontsize='small', ncol=2, title='Parâmetros', title_fontsize='medium')
plt.grid(True)
plt.show()
