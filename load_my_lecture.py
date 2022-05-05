import pandas as pd
import os

def get_my_lecture(file_name="learned.xlsx", type="all"):
    """
    들었던 강의 리스트
    type=(str) (default)all : Dataframe , list : List of Lecture Code
    return = dataframe
    """
    file_name = "./source/" + file_name
    if(os.path.isfile(file_name) == False):
        return []
    else:
        df =  pd.read_excel(file_name,usecols=[i for i in range(0,9)],dtype=str)
        df.columns = ["구분", "영역", "세부영역", "수강년도", "학기", "과목코드", "과목명", "학점", "이수구분"]
        df = df.sort_values(["과목코드"]).dropna(subset="과목코드").reset_index(drop=True)
        if(type == "all"):
            return df
        else:
            return df["과목코드"].tolist()