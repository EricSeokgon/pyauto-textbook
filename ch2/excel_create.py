import openpyxl as excel

book = excel.Workbook()

sheet = book.active

sheet["A1"] = "안녕하세요."

book.save("./oupput/hello.xlsx")