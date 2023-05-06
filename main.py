import openpyxl
from openpyxl import load_workbook
import random

book = load_workbook('C:\\Users\\Mahad\\Desktop\\Crazy-Cat-Facts\\CatFactLib.xlsx')

sheet = book.active

randnum = random.randint(2, 76)

print(f"{sheet[f'A{randnum}'].value} - {sheet[f'B{randnum}'].value}")


