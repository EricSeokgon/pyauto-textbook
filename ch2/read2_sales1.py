import openpyxl as excel

book = excel.load_workbook("input/monthly_sales.xlsx", ddata_only=True)
sheet = book.active

rows = sheet["A3":"F9"]
for row in rows:
    values = [cell.value for cell in row]
    print(values)
