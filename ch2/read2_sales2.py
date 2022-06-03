import openpyxl as excel

book = excel.load_workbook("input/monthly_sales.xlsx", data_only=True)
sheet = book.active

rows = sheet["A3":"F9"]
for row in rows:
    values = []
    for cell in row:
        values.append(cell.value)
