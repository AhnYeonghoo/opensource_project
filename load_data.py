from dataclasses import field
from numpy import minimum
import pandas as pd
import os

from pyparsing import nestedExpr
from load_my_lecture import get_my_lecture
from tools import contrast_old_and_new as con

all_ON_lecture = con.Old_and_new().get_all_lecture()
all_lecture = pd.read_excel("./source/all_lecture.xlsx",dtype=str)
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

    def get_my_score(self):
        self.my_ge = lec_field()
        #8 : 이수구분 1:영역 2:세부영역 5:과목코드 7:학점
        for i in range(len(self.my_lecture)):
            field = self.my_lecture.iat[i,1]
            score = self.my_lecture.iat[i,7]
            specific_field = ''
            if("전공" == field):
                field = self.my_lecture.iat[i,8]
            elif("자연이공계기초과학"!=field):
                specific_field = self.my_lecture.iat[i,2]
            self.add_score(score,field,specific_field)
        return self.my_ge

    def print_need_lec(self):
            require_major_codes = self.min_GE.essential_code["전공필수"]
            my_major = self.my_lecture[self.my_lecture["영역"].isin(["전공"])]
            
            for lec_code in require_major_codes:
                flag = False
                idx = all_lecture['과목코드'].tolist().index(lec_code)
                print("\t",all_lecture['학점'].iloc[idx],end="")

                if(lec_code in my_major["과목코드"].tolist()):
                    print("(수강함)",end="")
                    flag = True
                
                print(all_lecture['과목명'].iloc[idx], end="")

                for onn_lec in all_ON_lecture:
                    if(lec_code == onn_lec[0] and flag == False):
                        if(onn_lec[4] == "동일"):
                            print("->", onn_lec[3], " 변경되었습니다.",end="")
                        elif(onn_lec[4] == "삭제"):
                            print("는 폐강되었습니다",end="")
                print()

    def is_specific(self, field):
        return field in self.my_ge.specific_field.keys()

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