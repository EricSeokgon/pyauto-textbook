# pywin32(win32com) 라이브러리 불러오기
import win32com.client as com

# 엑셀 실행하기
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# 엑셀 에 신규 문서 생성
book = app.Workbooks.Add()
# 활성 시트 가져오기
sheet = book.ActiveSheet

#시트에 값 쓰기
sheet.Range("B2").Value = "안녕하세요."