from numpy import minimum
import pandas as pd
import os

from pyparsing import nestedExpr
from load_my_lecture import learned_list
from tools import contrast_old_and_new as con

class my_info:
    def __init__(self, year=2019, file_name = "learned.xlsx"):
        self.year = year
        self.min_GE = min_GE_score(year)
        self.my_lecture = learned_list(file_name)
        self.my_GE = self.get_my_grade()
    def get_my_grade(self):
        my_ge = lec_filed()
        #8 : 이수구분 1:영역 2:세부영역 5:과목코드 7:학점
        for i in range(len(self.my_lecture)):
            #print(c.my_lecture.iat[i,8], c.my_lecture.iat[i,1], c.my_lecture.iat[i,2])
            if("전공" in self.my_lecture.iat[i,8]):
                my_ge.filed[self.my_lecture.iat[i,8]] += int(self.my_lecture.iat[i,7])
            elif("자연이공계기초과학"==self.my_lecture.iat[i,1]):
                my_ge.filed[self.my_lecture.iat[i,1]] += int(self.my_lecture.iat[i,7])
            else:
                my_ge.filed[self.my_lecture.iat[i,1]] += int(self.my_lecture.iat[i,7])
                my_ge.specific_filed[self.my_lecture.iat[i,1]][self.my_lecture.iat[i,2]] += int(self.my_lecture.iat[i,7])
        return my_ge

    def need_lec(self):
            onn_lecs = con.Old_and_new().get_all_lecture()
            all_lec = pd.read_excel("./source/all_lecture.xlsx",dtype=str)
            req_major = self.min_GE.req_essential_code["전공필수"]
            my_major = self.my_lecture[self.my_lecture["영역"].isin(["전공"])]
            
            for lec_code in req_major:
                flag = False
                for onn_lec in onn_lecs:
                    if(lec_code == onn_lec[0]):
                        flag = True
                        print("\t", end="")
                        if(onn_lec[0] in my_major['과목코드'].tolist()):
                            print("(수강함)", onn_lec[1])
                        elif(onn_lec[4] == "동일"):
                            print(onn_lec[1], "->", onn_lec[3], " 변경되었습니다.")
                        elif(onn_lec[4] == "삭제"):
                            print(onn_lec[1], "는 폐강되었습니다")
                        else:
                            print(onn_lec[1], "는 신설되었습니다")
                if(flag == False):
                    print("\t",end="")
                    if(lec_code in my_major["과목코드"].tolist()):
                        print("(수강함)",end="")
                    idx = all_lec['과목코드'].tolist().index(lec_code)
                    print(all_lec['과목명'].tolist()[idx])
                    

    def leanred_lec(self):
        for filed, fscore in self.my_GE.filed.items():
            print(filed,": (",fscore,"/",self.min_GE.filed[filed],")")
            if(filed in self.my_GE.specific_filed.keys()): #영역의 키값에 교양이 포함된 경우
                for spe_filed, spscore in self.my_GE.specific_filed[filed].items():
                     print('\t',spe_filed,": (",spscore,"/",self.min_GE.specific_filed[filed][spe_filed], ")")
            elif(filed == "전공필수"):
                self.need_lec()

    

                
    
class min_GE_score: 
    def __init__(self, year=2019):
        self.year = year
        if(self.year == 2019):
            self.filed = {"개신기초교양":15, "일반교양":12, "확대교양":3, "자연이공계기초과학":12, "전공필수":34, "전공선택":44}
            self.specific_filed = {"개신기초교양": {"인성과비판적사고":3, "의사소통":3, "영어":3,"정보문해":6}, \
                                "일반교양":{"인간과문화":3, "사회와역사":3, "자연과과학":3}, \
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":3,"예술과체육":0}}
            self.req_essential_code = {"자연이공계기초과학": ["0941002", "0941003", "0941006", "0941007"], \
                                    "전공필수": ['5110090',	'5110091',	'5110003',	'5110005',	'5110046',	'5110092',	'5110009',	'5110011',	'5110014',	'5110094',	'5110016',	'5110095',	'5110107',	'5110023',	'5110096',	'5110097',	'5110086',	'5110100']}
        elif(self.year >= 2020):
            self.filed = {"개신기초교양":15, "일반교양":9, "확대교양":3, "자연이공계기초과학":6, "전공필수":28, "전공선택":50}
            self.specific_filed = {"개신기초교양":{"인성과비판적사고":3, "의사소통":3, "영어":3,"정보문해":6},\
                                "일반교양":{"인간과문화":3, "사회와역사":3, "자연과과학":3},\
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":0,"예술과체육":0}}
            self.req_essential_code = {"전공필수": ['5110001',	'5110122',	'5110123',	'5110005',	'5110121',	'5110014',	'5110032',	'5110126',	'5110011',	'5110016',	'5110018',	'5110130',	'5110131',	'5110133',	'5110135']}
    
class lec_filed:
    def __init__(self):
        self.filed = {"개신기초교양":0, "일반교양":0, "확대교양":0, "자연이공계기초과학":0, "전공필수":0, "전공선택":0}
        self.specific_filed = {"개신기초교양": {"인성과비판적사고":0, "의사소통":0, "영어":0,"정보문해":0}, \
                                "일반교양":{"인간과문화":0, "사회와역사":0, "자연과과학":0}, \
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":0,"예술과체육":0}}