import win32com.client as com
import os

# 절대 경로 형식으로 파일명 지정
src_file = os.path.abspath(__file__)
src_dir = os.path.dirname(src_file)
in_file = os.path.join(src_dir, 'input', 'stock-data.xlsx')
pdf_file = os.path.join(src_dir, 'output', 'pywin32_pdf.pdf')

# 엑셀 실행하기
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# 엑셀에서 기존 문서 열기
book = app.Workbooks.Open(in_file)
# 문서를 PDF로 보내기
xlTypePDF = 0
book.ExportAsFiexdFormat(xlTypePDF, pdf_file)

# 엑셀 종료
app.Quit()
