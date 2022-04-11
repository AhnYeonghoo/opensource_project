from numpy import minimum
import pandas as pd
import os
from load_my_lecture import learned_list

class min_GE_score: 
    def __init__(self, year=2019):
        self.year = year
        if(self.year == 2019):
            self.filed = {"개신기초교양":15, "일반교양":12, "확대교양":3, "자연이공계기초과학":12, "전공필수":34, "전공선택":44}
            self.specific_filed = {"개신기초교양": {"인성과비판적사고":3, "의사소통":3, "영어":3,"정보문해":6}, \
                                "일반교양":{"인간과문화":3, "사회와역사":3, "자연과과학":3}, \
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와 취업":3,"예술과체육":0}}
            self.req_essential_code = {"자연이공계기초과학": ["0941002", "0941003", "0941006", "0941007"], \
                                    "전공필수": ['5110090',	'5110091',	'5110003',	'5110005',	'5110046',	'5110092',	'5110009',	'5110011',	'5110014',	'5110094',	'5110016',	'5110095',	'5110107',	'5110023',	'5110096',	'5110097',	'5110086',	'5110100']}
        elif(self.year >= 2020):
            self.filed = {"개신기초교양":15, "일반교양":9, "확대교양":3, "자연이공계기초과학":6, "전공필수":28, "전공선택":50}
            self.specific_filed = {"개신기초교양":{"인성과비판적사고":3, "의사소통":3, "영어":3,"정보문해":6},\
                                "일반교양":{"인간과문화":3, "사회와역사":3, "자연과과학":3},\
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":0,"예술과체육":0}}
            self.req_essential_code = {"전공필수": ['5110001',	'5110122',	'5110123',	'5110005',	'5110121',	'5110014',	'5110032',	'5110126',	'5110011',	'5110016',	'5110018',	'5110130',	'5110131',	'5110133',	'5110135']}

class my_info:
    def __init__(self, year=2019, file_name = "learned.xlsx"):
        self.year = year
        self.min_GE = min_GE_score(year)
        self.my_min_grade = self.get_my_grade()
        self.my_lecture = learned_list(file_name)
    def get_my_grade(self):
        #for i in len(self.my_lecture):
        print(1)
        
        

c  = my_info(year = 2020)

for i in range(len(c.my_lecture)):
    print(c.my_lecture.iat[i,1])

#print(my_lec)

