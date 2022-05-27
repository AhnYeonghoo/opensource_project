import pandas as pd
import numpy as np
from os.path import join

# 분야에 맞는 강의의 모든 정보 출력 함수 시작
path_file = join('.', 'source','2022lecture.xlsx') # 상대경로로 만들기

data = pd.read_excel(path_file)   # 엑셀 파일 읽기

df_list = data.values.tolist()    # 리스트화

def get_type_matching_info(subject_type):     # 분야에 맞는 강의의 모든 정보 출력
    get_list=[]
    for i in range(len(df_list)-1):
        if subject_type in df_list[i]:
           get_list.append( df_list[i] )
    return get_list

# 과목코드에 따른 학점 불러오는 함수 시작
path_file2 = join('.','source','all_lecture.xlsx') # 상대경로 조합

data2 = pd.read_excel(path_file2, dtype=str) 
# 엑셀 파일 읽기, 과목코드가 0부터 시작하므로 문자열로 읽어야함

df_list2 = data2.values.tolist() # 리스트화

def get_grade(lecture_code): # 과목코드에 따른 학점 불러오기
    grade=''
    for i in range(len(df_list2)-1):
        if lecture_code in df_list2[i]:
            grade = df_list2[i]
    return grade[9]  # str 타입