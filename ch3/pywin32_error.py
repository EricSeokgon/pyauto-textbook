import win32com.client as com
import os

# 절대 경로 형식으로 파일명 지정
src_file = os.path.abspath(__file__)
src_dir = os.path.dirname(src_file)
in_file = os.path.join(src_dir, 'output', 'pywin32_save.xlsx')

# 엑셀 실행하기
app = com.Dispatch("Excel.Application")
app.Visible = False
app.DisplayAlerts = False

try:
    book = app.Workbooks.Open(in_file)
    sheet = book.ActiveSheet
    print("A1:", sheet.Cells(1, 1).Value)
    print("B2:", sheet.Cells(2, 2).Value)
    print("C3:", sheet.Cells(3, 3).Value)

    # 인위적으로 예외 발생시키기
    if True:
        raise Exception("엑셀을 읽던 도중 예외가 발생했습니다.")
    print("예외가 발생하지 않으면 이 부분이 싱행됩니다.")
except Exception as e:
    # 예외가 발생했ㅇ르 때 실행
    print('에러 메시지::', e)
else:
    # 예외가 발생하지 않았을 때 실행
    print('else 문이 실행되었습니다.')
finally:
    # 예외 발생과 상관없이 실행
    app.Quit()
    print('엑셀이 종료되었습니다.')
