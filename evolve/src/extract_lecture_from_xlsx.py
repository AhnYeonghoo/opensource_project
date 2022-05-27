"""
[사용방법]
강의 목록이 담긴 xlsx파일이 필요합니다.
[개신누리] -> [수업/성적] -> [수업정보] -> [교육과정조회]
년도 : (원하는 년도)
학기 : (일반, 전체)
강의구분 : (일반)
교과목코드/명 : (공란으로 두시면 됩니다.)
과목구분 : (전공, 교양 각각 하나씩)
ㄴ 전공 선택 시 전자정보대학, 교양 선택 시 전체
[조회]를 누르고 엑셀 다운로드를 누르십시오.
xlsx 파일의 이름은 전공의 경우 20xx전공 교양의 경우 20xx교양으로 수정
"""
import pandas as pd
import openpyxl
import os.path
import warnings

def extract_xlsx(file_name=""):
    if os.path.isfile(file_name) == False:
        print(file_name, "이 존재하지 않습니다")
        return
    
    print(file_name,"에서 데이터를 추출합니다")

    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        lecture_dataframe = pd.read_excel(file_name,skiprows=1, usecols=[i for i in range(1,10)],dtype=str,engine="openpyxl")

    lecture_dataframe.columns = ['대학', '학과', '학년', '일반', '학기', '구분', '과목코드', '과목명', '학점']
    print("추출완료!")
    
    out_file_name = file_name.split('.')[0] +"수정.xlsx"
    lecture_dataframe.to_excel(out_file_name)
    print(out_file_name,"에 추출한 데이터를 저장합니다")

start_year = 2019
end_year = 2022

for i in range(start_year,end_year+1): #start_year부터 end_year까지의 교양 및 전공 목록을 읽어옵니다.
    GE_file_name = str(i)+"교양.xlsx"
    MJ_file_name = str(i)+"전공.xlsx"
    #print(GE_file_name, MJ_file_name)
    extract_xlsx(GE_file_name)
    extract_xlsx(MJ_file_name)