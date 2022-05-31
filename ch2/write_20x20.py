import openpyxl as excel

book = excel.Workbook()

sheet = book.active

for y in range(1, 21):
    for x in range(1, 21):
        cell = sheet.cell(row=y, column=x)
        cell.value = x * y
book.save("output/write_21x21.xlsx")
