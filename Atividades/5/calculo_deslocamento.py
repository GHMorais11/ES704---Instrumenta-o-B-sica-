import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV para um DataFrame
data = pd.read_csv('Data05.csv')

# Cria a nova coluna com base nas colunas existentes e na equação
data['x'] = 100*data['V'] / (data['T'] - 4)

# Escreve o DataFrame resultante em um novo arquivo CSV
data.to_csv('Data05_deslocamento.csv', index=False)

data_x = pd.read_csv('Data05_deslocamento.csv')

# ordenar os valores por uma coluna específica
dados_sorted = data_x.sort_values(by='x')

# criar um novo arquivo csv com os valores ordenados
dados_sorted.to_csv('Data05_deslocamento_sorted.csv', index=False)

# Calcula a média dos valores na coluna 'nome_da_coluna'
media = data_x['x'].mean()

# Imprime o resultado
print('A média dos valores na coluna {} é: {:.2f}'.format('nome_da_coluna', media))

# Extrai as colunas de interesse
T = dados_sorted['T']
x = dados_sorted['x']

# Plota a função y(t)
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim([min(T), max(T)])
ax.tick_params(axis='both', labelsize=20)
plt.scatter(T, x, marker='o', label='Coeficientes angulares') # criar gráfico de dispersão

ax.set_xlabel('Temperatura [\u00B0C]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_ylabel('Deslocamento [um]', fontsize=20, color='black', labelpad=12, fontweight='bold') 
ax.set_title('Deslocamento x Temperatura', fontsize=28, color='black', fontweight='bold', pad=20) 
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5) 

fig.tight_layout() 
plt.show()