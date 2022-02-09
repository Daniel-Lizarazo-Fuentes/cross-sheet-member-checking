import csv

file = open("sheets/Members_Bank_Details.csv", encoding='utf-8-sig')
csvReader = csv.reader(file)
headerCurrent = next(csvReader)

rowsCurrent = []
for row in csvReader:
    rowsCurrent.append(row)

file.close()

file = open("sheets/Rabobank_Incasso_Adresboek.csv", encoding='utf-8-sig')
csvReader = csv.reader(file)
headerOld = next(csvReader)

rowsOld = []
for row in csvReader:
    rowsOld.append(row)

file.close()

