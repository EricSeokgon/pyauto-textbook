import openpyxl as excel

# 고객 명부 문서 열기
book = excel.load_workbook("input/all-customer.xlsx")

#명부 시트 선택
sheet = book["명부"]


