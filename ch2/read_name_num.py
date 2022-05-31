import openpyxl as excel

book = excel.Workbook()
sheet = book.active

cell = sheet["C2"]
(row, col) = (cell.row, cell.column)
print("C2=({},{})".format(row, col))

cell = sheet.cell(row=2, column=3)
cdt = cell.coordinate
print("(2,3)={}".format(cdt))
