import openpyxl as excel

book = excel.load_workbook("output/write_cellname.xlsx")
sheet = book.active

for y in range(2, 5):
    r = []
    for x in range(2, 5):
        v = sheet.cell(row=y, column=x).value
        r.append(v)
    print(r)
