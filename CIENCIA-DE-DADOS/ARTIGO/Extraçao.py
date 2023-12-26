def read_file_to_list(filename="DADOS.tsv"):
    data_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            row = line.strip().split('\t')  # split by tab
            if row:  # check if row is not empty
                data_dict[row[0]] = [float(val.replace(',', '.')) if val.replace(',', '.').replace('.', '', 1).isdigit() else val for val in row[1:]]
    return data_dict

result = read_file_to_list()
print(result)
print("Tamanho do dicionário: ", len(result))

for i,j in result.items():
    print(i,j) 

 