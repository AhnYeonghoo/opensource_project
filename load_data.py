from dataclasses import field
from numpy import minimum
import pandas as pd
import os

from load_my_lecture import get_my_lecture
from tools import contrast_old_and_new as con
from tools import Prerequisites_dictionary as pre

all_ON_lecture = con.Old_and_new().get_all_lecture()
all_lecture = pd.read_excel("./source/all_lecture.xlsx",dtype=str)
lecture_in_2022 = pd.read_excel("./source/2022lecture.xlsx")
prerequisites = pre.prerequisites().subject_pair_dic
class my_info:
    def __init__(self, year=2019, file_name = "learned.xlsx"):
        self.year = year
        self.my_lecture = get_my_lecture(file_name)
        self.min_GE = lec_field().get_field(self.year)
        self.my_ge = self.get_my_score()

    def add_score(self, score='0', field='', specific_field=''):
        self.my_ge.field[field] += int(score)
        if(specific_field != ''):
            self.my_ge.specific_field[field][specific_field] += int(score)

    def get_cource_info(self, i):
        field = self.my_lecture.iat[i,1]
        score = self.my_lecture.iat[i,7]
        specific_field = ''
        if("전공" == field):
            field = self.my_lecture.iat[i,8]
        elif("자연이공계기초과학"!=field):
            specific_field = self.my_lecture.iat[i,2]
        return score, field, specific_field

    def get_my_score(self):
        self.my_ge = lec_field()
        #8 : 이수구분 1:영역 2:세부영역 5:과목코드 7:학점
        for i in range(len(self.my_lecture)):
            info =self.get_cource_info(i)
            self.add_score(info[0], info[1], info[2])
        return self.my_ge

    def print_need_lec(self):
            require_major_codes = self.min_GE.essential_code["전공필수"]
            my_major = self.my_lecture[self.my_lecture["영역"].isin(["전공"])]
            
            for lec_code in require_major_codes:
                flag = False
                idx = all_lecture['과목코드'].tolist().index(lec_code)
                if(lec_code in prerequisites.keys()):
                    idx2 = all_lecture['과목코드'].tolist().index(prerequisites[lec_code])
                    print("   ", all_lecture['과목명'].iloc[idx2]," (필요)",end="")
                
                print("\t",all_lecture['학점'].iloc[idx],end="")
                
                if(lec_code in my_major["과목코드"].tolist()):
                    print("(수강함)",end="")
                    flag = True
                
                print(all_lecture['과목명'].iloc[idx], end="")

                for onn_lec in all_ON_lecture:
                    if(flag == False):
                        if(lec_code == onn_lec[0]):
                            if(onn_lec[4] == "동일"):
                                print("->", onn_lec[3], "(변경)",end="")
                            elif(onn_lec[4] == "삭제"):
                                print("(폐강)",end="")
                            
                
                print()

    def is_specific(self, field):
        """
        :return type = bool 
        """
        return field in self.my_ge.specific_field.keys()

    def print_major_selection(self):
        self.my_lecture

    def print_my_lec(self):
        for field, require_score in self.my_ge.field.items():
            my_score = self.min_GE.field[field]
            print(f"{field} : ( {require_score} / {my_score})")

            if(self.is_specific(field)): #세부영역이 필요한 경우
                for specific_field, require_score in self.my_ge.specific_field[field].items():
                    my_score = self.min_GE.specific_field[field][specific_field]
                    print(f"\t {specific_field} : ( {require_score} / {my_score})")
            elif(field == "전공필수"):
                self.print_need_lec()

    def print_my_ge_lec(self, specific_field):
        df = pd.read_excel("./source/2022lecture.xlsx", dtype = str)
        my_ge_lec = pd.DataFrame(df, columns = ['분야', '교과목명'])
        my_ge_lec_list = my_ge_lec.values.tolist()
        for i in range(len(my_ge_lec_list)):
            if(my_ge_lec_list[i][0] == specific_field):
                print(my_ge_lec_list[i][1])

    def print_GE(self, specific_field):         # 세부영역 이수 여부 출력
        df_learned= pd.read_excel("./source/learned_mc.xlsx", dtype = str)
        my_learned= pd.DataFrame(df_learned, columns=['영역','세부영역','교과목번호','교과목명','이수구분'])
        my_learned_list = my_learned.values.tolist()

        df = pd.read_excel("./source/2022lecture.xlsx", dtype = str)
        df_all = pd.DataFrame(df, columns = ['분야', '교과목번호', '교과목명'])
        df_all_list = df_all.values.tolist()

        for i in range(len(df_all_list)):
            if df_all_list[i][0] == specific_field:
                    flag=0
                    for j in range(len(my_learned_list)):
                            if df_all_list[i][1] == my_learned_list[j][2]:
                                    flag=1
                    if flag == 1:
                            print("{} (이수)".format(df_all_list[i][2]))
                    else:
                            print("{} (미이수)".format(df_all_list[i][2]))

class lec_field:
    def __init__(self):
        self.field = {"개신기초교양":0, "일반교양":0, "확대교양":0, "자연이공계기초과학":0, "전공필수":0, "전공선택":0}
        self.specific_field = {"개신기초교양": {"인성과비판적사고":0, "의사소통":0, "영어":0,"정보문해":0}, \
                                "일반교양":{"인간과문화":0, "사회와역사":0, "자연과과학":0}, \
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":0,"예술과체육":0}}
        self.essential_code = {}
    
    def get_field(self, year = 2019):
        if(year == 2019):
            self.field = {"개신기초교양":15, "일반교양":12, "확대교양":3, "자연이공계기초과학":12, "전공필수":34, "전공선택":44}
            self.specific_field = {"개신기초교양": {"인성과비판적사고":3, "의사소통":3, "영어":3,"정보문해":6}, \
                                "일반교양":{"인간과문화":3, "사회와역사":3, "자연과과학":3}, \
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":3,"예술과체육":0}}
            self.essential_code = {"자연이공계기초과학": ["0941002", "0941003", "0941006", "0941007"], \
                                    "전공필수": ['5110090',	'5110091',	'5110003',	'5110005',	'5110046',	'5110092',	'5110009',	'5110011',	'5110014',	'5110094',	'5110016',	'5110095',	'5110107',	'5110023',	'5110096',	'5110097',	'5110086',	'5110100']}
        elif(year >= 2020):
            self.field = {"개신기초교양":15, "일반교양":9, "확대교양":3, "자연이공계기초과학":6, "전공필수":28, "전공선택":50}
            self.specific_field = {"개신기초교양":{"인성과비판적사고":3, "의사소통":3, "영어":3,"정보문해":6},\
                                "일반교양":{"인간과문화":3, "사회와역사":3, "자연과과학":3},\
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":0,"예술과체육":0}}
            self.essential_code = {"전공필수": ['5110001',	'5110122',	'5110123',	'5110005',	'5110121',	'5110014',	'5110032',	'5110126',	'5110011',	'5110016',	'5110018',	'5110130',	'5110131',	'5110133',	'5110135']}
        return self