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

# Imprime o resultado
print('A média dos valores na coluna {} é: {:.3f}'.format('nome_da_coluna', media))

# Cria a nova coluna com base nas colunas existentes e na equação
#if data['v'] <= 1.589 == True:
  #data['T'] = -((((1.537-data['e13'])/(1.537-1.589))*(30-31))-30)
#else:
data['T'] = -((((2.374-data['e13'])/(2.374-2.427))*(46-47))-46)

# Escreve o DataFrame resultante em um novo arquivo CSV
data.to_csv('Data06_temperatura.csv', index=False)

data_T = pd.read_csv('Data06_temperatura.csv')

T = data['T']

# Calcula a média dos valores na coluna 'nome_da_coluna'
media = data['T'].mean()

# Imprime o resultado
print('A média dos valores na coluna {} é: {:.2f}'.format('nome_da_coluna', media))

# Plota a função y(t)
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim([min(t), max(t)])
ax.tick_params(axis='both', labelsize=20)
ax.plot(t, T, linewidth=1.5, color='blue') 

ax.set_xlabel('tempo [\u00B0C]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_ylabel('Temperatura [°C]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_title('Temperatura x tempo', fontsize=28, color='black', fontweight='bold', pad=20) 
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5) 

fig.tight_layout() 
plt.show()