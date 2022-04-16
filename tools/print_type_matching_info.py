import pandas as pd
from os.path import join

path_file = join('.', 'source','2022lecture.xlsx') # 상대경로로 만들기

data=pd.read_excel(path_file)   # 엑셀 파일 읽기

df_list=data.values.tolist()    # 리스트화

def get_type_matching_info(subject_type):     # 분야에 맞는 강의의 모든 정보 출력
    get_list=[]
    for i in range(len(df_list)-1):
        if subject_type in df_list[i]:
           get_list.append( df_list[i] )
    return get_list