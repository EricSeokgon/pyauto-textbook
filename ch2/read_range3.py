import openpyxl as excel

book = excel.load_workbook("output/write_cellname.xlsx")
sheet = book.active

it = sheet.iter_rows(
    min_row=2, min_col=2,
    max_row=4, max_col=4)

for row in it:
    r = []
    for cell in row:
        r.append(cell.value)
    print(r)
