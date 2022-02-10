import csv

rowsCurrent = []
rowsOld = []
headerOld = []
headerCurrent = []

# Add rows/headers to lists
with open("sheets/Members_Bank_Details.csv", encoding='utf-8-sig') as file:
    csvReader = csv.reader(file)
    headerCurrent = next(csvReader)

    for row in csvReader:
        rowsCurrent.append(row)
# Add rows/headers to lists
with open("sheets/Rabobank_Incasso_Adresboek.csv", encoding='utf-8-sig') as file:
    csvReader = csv.reader(file)
    headerOld = next(csvReader)

    for row in csvReader:
        rowsOld.append(row)

for row in rowsOld:
    row[3] = row[3].replace(" ", "")
    row[3] = row[3].upper()

for row in rowsCurrent:
    row[2] = row[2].replace(" ", "")
    row[2] = row[2].upper()

# For each row in the Rabobank sheet check if a corresponding IBAN is present in the current members list
# If not present remove row
for row in rowsOld[:]:
    rowPresent = False
    for checkRow in rowsCurrent:
        if row[3] == checkRow[2]:
            rowPresent = True
    if not rowPresent:
        rowsOld.remove(row)

# Check if there are any members present in the current list which are not present in the Rabo list
for checkRow in rowsCurrent[:]:
    rowPresent = False
    for row in rowsOld:
        if checkRow[2] == row[3]:
            rowPresent = True
    if rowPresent:
        rowsCurrent.remove(checkRow)

# Create csv of members missing from new Rabolist
with open('sheets/Members_not_in_RaboList.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(headerCurrent)
    write.writerows(rowsCurrent)

# Create csv of rabolist excluding people who are no longer members
with open('sheets/Checked_Rabobank_Incasso.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(headerOld)
    write.writerows(rowsOld)
