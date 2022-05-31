import openpyxl as excel

# 워크북 열기
book = excel.load_workbook("output/write_cellname.xlsx")
# 워크시트 읽기
sheet = book.active

print(sheet["H2"].value)

cell = sheet.cell(row=2, column=8)
print(cell.value)
