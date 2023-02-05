import pandas as pd
import os

dir_list = os.listdir('input')
flag = True
sheet_num = int(input('Sheet Number: '))

for dir in dir_list:
    if dir.endswith('xls') or dir.endswith('xlsx'):
        if flag:
            open('result.csv', 'w').write((pd.read_excel('./input/' + dir).head(0).to_csv(header=True, index=False, sep=';').removesuffix('\n')))
            flag = False
        file = pd.ExcelFile('./input/' + dir)
        sheet = pd.read_excel('./input/' + dir, sheet_name=sheet_num-1)
        sheet.to_csv("result.csv", mode='a', sep=';', index = None, header=False)