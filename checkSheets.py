import csv

rowsCurrent = []
rowsOld = []
headerOld = []
headerCurrent = []

with open("sheets/Members_Bank_Details.csv", encoding='utf-8-sig') as file:
    csvReader = csv.reader(file)
    headerCurrent = next(csvReader)

    for row in csvReader:
        rowsCurrent.append(row)

with open("sheets/Rabobank_Incasso_Adresboek.csv", encoding='utf-8-sig') as file:
    csvReader = csv.reader(file)
    headerOld = next(csvReader)

    for row in csvReader:
        rowsOld.append(row)

    for row in rowsOld[:]:
        rowPresent = False
        for checkRow in rowsCurrent:
            if row[3].replace(" ", "") == checkRow[2].replace(" ", ""):
                rowPresent = True
        if not rowPresent:
            rowsOld.remove(row)

with open('sheets/Checked_Rabobank_Incasso.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(headerOld)
    write.writerows(rowsOld)
