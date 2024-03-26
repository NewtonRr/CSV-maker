import csv
import os

def readCsvFile(arquivo):
    with open(arquivo, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)

def create_csv(file_name, num_rows, num_columns):
    data = []
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            value = str(input(f"digite o valor para linha {i + 1}, coluna {j + 1}: "))
            row.append(value)
        data.append(row)

    with open(file_name, 'w') as file:
        for row in data:
            file.write(','.join(row) + '\n')
        print(f"Arquivo CSV '{file_name}' Criado")

def fileChecker(arquivoCheck):
    return os.path.exists(arquivoCheck)

loop = False

while loop == False:
    print('Escolha a acao que deseja realizar.\nLer arquivo(1)\nCriar arquivo(2)\nSair(3)')
    choice = int(input('(Use os respectivos numeros) : '))
    print('\n')

    if choice == 1:
        print('escolha o arquivo que deseja ler:\n(o arquivo dese estar dentro da pasta do programa)')
        arquivo = str(input('(nome do arquivo SEM extencao)') + ".csv")

        if fileChecker(arquivo):
            print('o arquivo existe')
            readCsvFile(arquivo)
        else:
            print('o arquivo nao foi encontrado\n')
    elif choice == 2:
        print('escolha o nome do novo arquivo')
        newName = str(input('(nome do arquivo SEM extencao)') + ".csv")
        numRows = int(input('escolha a quantidade de linhas do arquivo(incluindo o cabecalho): '))
        numColumns = int(input('escolha a quantidade de colunas do arquivo: '))
        create_csv(newName, numRows, numColumns)
    elif choice == 3:
        print('saindo...')
        loop = True
    else: 
        print('resposta inválida\n')

    
