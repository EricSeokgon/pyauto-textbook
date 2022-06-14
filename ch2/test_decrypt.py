import msoffcrypto
import openpyxl as excel

fin = open("input/monthly_sales_encrypt.xlsx", "rb")
msfile = msoffcrypto.OfficeFile(fin)

msfile.load_key(password="abcd")
fout = open("output/monthly_sales_decrypt.xlsx", "wb")
book = excel.load_workbook("output/monthly_sales_decrypt.xlsx", data_only=True)
sheet = book.active
for row in sheet["A2:F99"]:
    values = [v.value for v in row]
    if values[0] is None: break
    print(values)
