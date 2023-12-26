import pandas as pd
from scipy.stats import linregress, pearsonr
import matplotlib.pyplot as plt

#Tratando os dados do arquivo
def read_file_to_list(filename="DADOS.tsv"):
    data_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            row = line.strip().split('\t')  # split by tab
            if row:  # check if row is not empty
                data_dict[row[0]] = [float(val.replace(',', '.')) if val.replace(',', '.').replace('.', '', 1).isdigit() else val for val in row[1:]]
    return data_dict

dicionario = read_file_to_list()

#Dados extraidos e tratados

dic_diferença={}
print("Tamanho do dicionário: ", len(dicionario))

#Obtendo diferença de ide entre os generos
for chave,valor in dicionario.items():
    dic_diferença[chave]=(round(abs(valor[0]-valor[1]),1),valor[0],valor[1],valor[2])

#Carregando dados para um dataframe panda
dataframe = pd.DataFrame(dic_diferença).T 
dataframe.columns = ['DIFERENÇA DE GENERO','IDE_FEMININO','IDE_MASCULINO', '%POP ACESSO INTERNET']

#Realizando analise estatistica entre IDE Masc e %pop com acesso a internet
slope_menNet, intercept_menNet, r_pearson_menNet, p_value_menNet, std_err_menNet = linregress(dataframe['IDE_MASCULINO'], dataframe['%POP ACESSO INTERNET'])
# Gráfico de dispersão
plt.figure(figsize=(10,6))
plt.scatter(dataframe['IDE_MASCULINO'], dataframe['%POP ACESSO INTERNET'], color='blue', edgecolors='k', alpha=0.6, label='Dados')
plt.title('Relação entre ide masculino e acesso a internet no país')
plt.xlabel('IDE MASCULINO')
plt.ylabel('%População com internet')
plt.figtext(0.10,0.03,f'Coeficiente de pearson:{round(r_pearson_menNet,3)}')

# Adicionando a linha de regressão
x = dataframe['IDE_MASCULINO']
y_pred = slope_menNet * x + intercept_menNet
plt.plot(x, y_pred, color='red', label='Linha de regressão')

plt.legend()
plt.grid(True)
plt.show()

#Realizando analise estatistica entre IDE Fem e %pop com acesso a internet
slope_womanNet, intercept_womanNet, r_pearson_womanNet, p_value_womanNet, std_err_womanNet = linregress(dataframe['IDE_FEMININO'], dataframe['%POP ACESSO INTERNET'])
# Gráfico de dispersão
plt.figure(figsize=(10,6))
plt.scatter(dataframe['IDE_FEMININO'], dataframe['%POP ACESSO INTERNET'], color='blue', edgecolors='k', alpha=0.6, label='Dados')
plt.title('Relação entre ide feminino e acesso a internet no país')
plt.xlabel('IDE FEMININO')
plt.ylabel('%População com internet')
plt.figtext(0.10,0.03,f'Coeficiente de pearson:{round(r_pearson_womanNet,3)}')

# Adicionando a linha de regressão
x = dataframe['IDE_FEMININO']
y_pred = slope_womanNet * x + intercept_womanNet
plt.plot(x, y_pred, color='red', label='Linha de regressão')

plt.legend()
plt.grid(True)
plt.show()

#Realizando analise estatistica entre diferença do ide entre generos e %pop com acesso a internet
slope_difGenderNet, intercept_difGenderNet, r_pearson_difGenderNet, p_value_difGenderNet, std_err_difGenderNet = linregress(dataframe['DIFERENÇA DE GENERO'], dataframe['%POP ACESSO INTERNET'])
# Gráfico de dispersão
plt.figure(figsize=(10,6))
plt.scatter(dataframe['DIFERENÇA DE GENERO'], dataframe['%POP ACESSO INTERNET'], color='blue', edgecolors='k', alpha=0.6, label='Dados')
plt.title('Relação entre diferença de ide entre generos e acesso a internet no país')
plt.xlabel('DIFERENÇA DE GENERO')
plt.ylabel('%População com internet')
plt.figtext(0.10,0.03,f'Coeficiente de pearson:{round(r_pearson_difGenderNet,3)}')

# Adicionando a linha de regressão
x = dataframe['DIFERENÇA DE GENERO']
y_pred = slope_difGenderNet * x + intercept_difGenderNet
plt.plot(x, y_pred, color='red', label='Linha de regressão')

plt.legend()
plt.grid(True)
plt.show()

#Log do dataframe
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(dataframe)
 