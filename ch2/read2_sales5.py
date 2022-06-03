import openpyxl as excel

sheet = excel.load_workbook("input/monthly_sales.xlsx", data_only=True).active

for row in sheet.iter_rows(min_row=3):
    values = [cell.value for cell in row]
    if values[0] is None: break
    print(values)
