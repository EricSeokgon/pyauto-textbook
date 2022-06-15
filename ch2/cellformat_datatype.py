import openpyxl as xl

book = xl.Workbook()
sheet = book.active

cell = sheet["A1"]
cell.value = 345
sheet["B1"] = "data_type=" + cell.data_type

cell = sheet["A2"]
cell.value = "abc"
sheet["B2"] = "data_type=" + cell.data_type

cell = sheet["A3"]
from datetime import date

cell.value = date(2021, 4, 1)
sheet["B3"] = "data_type=" + cell.data_type
book.save("output/cellformat_datatype.xlsx")
