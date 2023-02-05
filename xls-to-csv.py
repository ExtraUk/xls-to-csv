import pandas as pd
import os

if(os.path.isfile('result.csv')):
    open('result.csv', 'w').write('IDE;Peso;Categoria;Dias;Fecha\n')

dir_list = os.listdir('input')
for dir in dir_list:
    file = pd.ExcelFile('./input/' + dir)
    sheet = pd.read_excel('./input/' + dir, sheet_name=(len(file.sheet_names)-1))
    sheet.to_csv("result.csv", mode='a', sep=';', index = None, header=False)