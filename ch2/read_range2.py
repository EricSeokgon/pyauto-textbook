import openpyxl as excel

book = excel.load_workbook("output/write_cellname.xlsx")
sheet = book.active

for row in sheet["B2":"D4"]:
    r = []
    for cell in row:
        r.append(cell.value)
    print(r)
