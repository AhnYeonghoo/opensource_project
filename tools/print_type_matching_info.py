import pandas as pd
from os.path import join

path_file = join('..', 'source','2022lecture.xlsx') # 상대경로로 만들기

data=pd.read_excel(path_file)   # 엑셀 파일 읽기

df_list=data.values.tolist()    # 리스트화

def print_type_matching_info(type): # 해당 분야에 맞는 과목 출력
    for i in range(len(df_list)-1):
        if type in df_list[i]:
           print(df_list[i])