import csv, openpyxl as excel

# 설정
in_file = './input/name_addr.csv'
template_file = './input/card-template.xlsx'
save_file = './output/csv_card.xlsx'


# CSV파일 읽기
def read_csv(fname):
    with open(fname, encoding='ansi') as f:
        reader = csv.reader(f)
        next(reader)
        return [v for v in reader]


# 엑셀 파일 읽기
book = excel.load_workbook(template_file)

# 템플릿 시ㅡㅌ 가져오기
sheet_tpl = book['Sheet']

# csv에서 고객 목록을 가져오고 한 명씩 처리
for i, person in enumerate(read_csv(in_file)):
    # csv의 한 행을 각 변수에 저장
    name, zipnum, addr = person
    # 이름표 10개가 다 차면 시트를 추가
    idx = i % 10
    if idx == 0:
        # 템플릿 시트를 복사
        sheet = book.copy_worksheet(sheet_tpl)
        sheet.title = 'page' + str(i // 10)
    # 데이터를 쓸 위치를 결정
    row = 4 * (idx % 5) + 2
    col = 2 * (idx // 5) + 2
    # print(person)

    # 셀에 데이터 쓰기
    sheet.cell(row=row + 0, column=col, value=name)
    sheet.cell(row=row + 1, column=col, value=zipnum)
    sheet.cell(row=row + 2, column=col, value=addr)

# 템플릿 시트를 삭제하고 문서를 저장
book.remove(sheet_tpl)
book.save(save_file)
