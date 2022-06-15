import openpyxl as xl

book = xl.Workbook()
sheet = book.active

sheet.append(["서식", "예시 1", "예시 2"])


def set_cell(cname, value, fmt):
    c = sheet[cname]
    c.value = value
    c.number_format = fmt


digit3_fmt = '#,##0'
sheet["A2"] = digit3_fmt
set_cell("B2", 12345, digit3_fmt)
set_cell("C2", 123456789, digit3_fmt)

cur_fmt = '"\"#,##0;"\"-#,##0'
sheet["A3"] = cur_fmt
set_cell("B3", 12345, cur_fmt)
set_cell("C3", -12345, cur_fmt)

num_fmt = '#,##0;[red]"△ "#,##0'
sheet["A4"] = num_fmt
set_cell("B4", 12345, num_fmt)
set_cell("C4", -12345, num_fmt)
book.save("output/cellformat_num2.xlsx")
