import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Estilo
plt.style.use('default')

data = pd.read_csv('Data06.csv')

# Extrai as colunas de interesse
t = data['t']
v = data['v']

# Cria a nova coluna com base nas colunas existentes e na equação
data['e13'] = data['v'] + 1.174
data['e13min'] = data['v'] + 1.071
data['e13max'] = data['v'] + 1.277
#e13 = data['e13']
#data['v30'] = 1.589

#if data['e13'].values <= 1.589:
 # data['T'] = -((((1.537-data['e13'])/(1.537-1.589))*(30-31))-30)

# Escreve o DataFrame resultante em um novo arquivo CSV
data.to_csv('Data06_tensao.csv', index=False)

data_e13 = pd.read_csv('Data06_tensao.csv')

e13 = data['e13']

# Calcula a média dos valores na coluna 'nome_da_coluna'
media = data['e13'].mean()
media1 = data['e13min'].mean()
media2 = data['e13max'].mean()

# Imprime o resultado
print('A média dos valores na coluna {} é: {:.3f}'.format('nome_da_coluna', media))
print('A média dos valores na coluna {} é: {:.3f}'.format('nome_da_coluna', media1))
print('A média dos valores na coluna {} é: {:.3f}'.format('nome_da_coluna', media2))

# Cria a nova coluna com base nas colunas existentes e na equação
#if data['v'] <= 1.589 == True:
  #data['T'] = -((((1.537-data['e13'])/(1.537-1.589))*(30-31))-30)
#else:
data['T'] = -((((2.374-data['e13'])/(2.374-2.427))*(46-47))-46)
data['Tmin'] = -((((2.269-data['e13min'])/(2.269-2.322))*(44-45))-44)
data['Tmax'] = -((((2.480-data['e13max'])/(2.480-2.532))*(48-49))-48)

# Escreve o DataFrame resultante em um novo arquivo CSV
data.to_csv('Data06_temperatura.csv', index=False)

data_T = pd.read_csv('Data06_temperatura.csv')

T = data['T']
Tmin = data['Tmin']
Tmax = data['Tmax']

# Calcula a média dos valores na coluna 'nome_da_coluna'
media = data['T'].mean()
maximo = data['Tmax'].max()
maximo1 = data['T'].max()
maximo2 = data['Tmin'].max()

# Imprime o resultado
print('A média dos valores na coluna {} é: {:.2f}'.format('nome_da_coluna', media))
print('O máximo dos valores na coluna {} é: {:.2f}'.format('nome_da_coluna', maximo))
print('O máximo dos valores na coluna {} é: {:.2f}'.format('nome_da_coluna', maximo1))
print('O máximo dos valores na coluna {} é: {:.2f}'.format('nome_da_coluna', maximo2))

# Plota a função y(t)
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim([min(t), max(t)])
ax.tick_params(axis='both', labelsize=20)
ax.plot(t, T, linewidth=1.5, color='blue')
ax.plot(t, Tmin, linewidth=1.5, color='red')
ax.plot(t, Tmax, linewidth=1.5, color='red')

ax.set_xlabel('tempo [min]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_ylabel('Temperatura [°C]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_title('Temperatura x tempo', fontsize=28, color='black', fontweight='bold', pad=20) 
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5) 

fig.tight_layout() 
plt.show()