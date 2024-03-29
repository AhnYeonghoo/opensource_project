"""Provide Class MyInfo and some data

<list> all_ON_lecture
<data frame> all_lecture
<data frame> lecture_in_2022
<dictionary> prerequisites
<class> MyInfo

"""
import pandas as pd
import os
from src import contrast_old_and_new as con
from src import Prerequisites_dictionary as pre

def get_my_lecture(file_name="learned.xlsx", type="all"):
    """
    들었던 강의 리스트
    type=(str) (default)all : Dataframe , list : List of Lecture Code
    return = dataframe
    """
    file_name = "./media/result/" + file_name
    print(file_name)
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


all_ON_lecture = con.Old_and_new().get_all_lecture()
all_lecture = pd.read_excel("./data/all_lecture.xlsx",dtype = str)
lecture_in_2022 = pd.read_excel("./data/2022lecture.xlsx", dtype = str)
prerequisites = pre.Prerequisites().subject_pair_dic
class MyInfo:
    """Input my lecture info, automatically calculate score
    
    need:
        learned.xlsx

    feature:
        void print_my_lec()

    """
    def __init__(self, year=2019, file_name = "learned.xlsx"):
        self.year = year
        self.my_lecture = get_my_lecture(file_name)
        self.min_ge = LecField().get_field(self.year)
        self.my_ge = self.get_my_score()

    def add_score(self, score='0', field='', sub_field=''):
        """
        :param score: string ; available turn to int (yyyy)
        :param field: string 
        :param specific_field: string 
        :return: void

        """
        self.my_ge.field[field] += int(float(score))
        if sub_field != '':
            self.my_ge.sub_field[field][sub_field] += int(float(score))

    def get_course_info(self, i):
        field = self.my_lecture.iat[i,1]
        score = self.my_lecture.iat[i,7]
        sub_field = ''
        if "전공" == field:
            field = self.my_lecture.iat[i,8]
        elif "자연이공계기초과학"!=field:
            sub_field = self.my_lecture.iat[i,2]
        return score, field, sub_field

    def get_my_score(self):
        self.my_ge = LecField()
        #8 : 이수구분 1:영역 2:세부영역 5:과목코드 7:학점
        for i in range(len(self.my_lecture)):
            info =self.get_course_info(i)
            self.add_score(info[0], info[1], info[2])
        return self.my_ge

    def print_need_lec(self):
        lec_list = []
        require_major_codes = self.min_ge.essential_code["전공필수"]
        my_major = self.my_lecture[self.my_lecture["영역"].isin(["전공"])]
        for lec_code in require_major_codes:
            lec_info = {"isClear":"","name":"","changed":"","prerequire":"","score":"", "new_name":""}
            lec_info["isClear"]="(미이수)"
            flag = False
            idx = all_lecture['과목코드'].tolist().index(lec_code)
            #print(end="\t")
            if lec_code in my_major["과목코드"].tolist():
                #print("(수강함)",end="")
                lec_info["isClear"]="(이  수)"
                flag = True
            #print(all_lecture['과목명'].iloc[idx], end="")
            lec_info["name"]=all_lecture['과목명'].iloc[idx]
            for onn_lec in all_ON_lecture:
                if flag is False:
                    if lec_code == onn_lec[0]:
                        lec_info["new_name"]=onn_lec[3]
                        if onn_lec[4] == "동일":
                            #print("->", onn_lec[3], "(변경)",end="")
                            lec_info["changed"]="(변경)"
                        elif onn_lec[4] == "삭제":
                            #print("(폐강)",end="")
                            lec_info["changed"]="(삭제)"
                        elif onn_lec[4] == "신설":
                            lec_info["changed"]="(신설)"
            
            
            if lec_code in prerequisites and self.year < 2020:
                idx2 = all_lecture['과목코드'].tolist().index(prerequisites[lec_code])
                #print("   ", all_lecture['과목명'].iloc[idx2]," (필요)",end="")
                lec_info["prerequire"]=all_lecture['과목명'].iloc[idx2]

            #print(all_lecture['학점'].iloc[idx],end="")
            #print()
            lec_info["score"]=all_lecture['학점'].iloc[idx]
            lec_list.append(lec_info)
        return lec_list
        

    def is_specific(self, field):
        return field in self.my_ge.sub_field.keys()

    def print_major_selection(self):
        lec_list = []
        if self.year < 2020:
            codes = self.my_lecture[self.my_lecture["이수구분"]=="전공선택"]["과목코드"].tolist()
            changed_codes = codes.copy()
            for lec in all_ON_lecture:
                if lec[0] in codes:
                    changed_codes[codes.index(lec[0])] = lec[2]

            all_lecture_code_df = all_lecture.set_index("과목코드",drop=True)

            for lec1, lec2 in zip(codes, changed_codes):
                lec_info = {"isClear":"", "lecture_name":"", "grade": "", "previous_lecture_name":""}
                if lec1 != lec2:
                    lec_info["previous_lecture_name"]=all_lecture_code_df.loc[lec1, "과목명"]
                    # print("\t(이수)", all_lecture_code_df.loc[lec1, "과목명"], "->", \
                    #     all_lecture_code_df.loc[lec2, "과목명"], all_lecture_code_df.loc[lec2, "학점"])
                # else:
                #     print("\t(이수)", all_lecture_code_df.loc[lec1, "과목명"], all_lecture_code_df.loc[lec2, "학점"])
                lec_info["isClear"] = "(이  수)"
                lec_info["lecture_name"]=all_lecture_code_df.loc[lec2, "과목명"]
                lec_info["grade"] = all_lecture_code_df.loc[lec2, "학점"]
                lec_list.append(lec_info)
            for lec in lecture_in_2022[lecture_in_2022["분야"]=="전공선택"].values.tolist():
                lec_info = {"isClear":"", "lecture_name":"", "grade": "", "previous_lecture_name":""}
                if lec in codes:
                    continue
                lec_info["isClear"] = "(미이수)"
                lec_info["lecture_name"]=lec[4]
                lec_info["grade"] = lec[5]
                #print("\t(미이수)", lec[4], lec[5])
                lec_list.append(lec_info)
        else:
            lec_list = self.print_ge("전공선택")
        return lec_list

    def print_my_lec(self):
        for field, my_score in self.my_ge.field.items():
            require_score = self.min_ge.field[field]
            print(f"{field} : ( {my_score} / {require_score})")

            if self.is_specific(field): #세부영역이 필요한 경우
                for specific_field, my_score in self.my_ge.sub_field[field].items():
                    require_score = self.min_ge.sub_field[field][specific_field]
                    print(f"\t {specific_field} : ({my_score} / {require_score})")
                    if my_score < require_score:
                        self.print_ge(specific_field)
            elif field == "전공필수":
                self.print_need_lec()
            elif field == "전공선택":
                self.print_major_selection()

    def print_my_ge_lec(self, specific_field):      # 분야에 맞는 교과목명 출력
        my_ge_lec = pd.DataFrame(lecture_in_2022, columns = \
                                            ['분야', '교과목명']).values.tolist()
        my_ge_lec_list=[]

        for i in len(my_ge_lec):
            my_ge_lec_info={"lecture_name":""}
            if my_ge_lec[i][0] == specific_field:
                #print(f"\t{my_ge_lec[i][1]}")
                my_ge_lec_info["lecture"] = my_ge_lec[i][1]
            my_ge_lec_list.append(my_ge_lec_info)

        return my_ge_lec_list

    def print_ge(self, specific_field):        # 세부영역 이수 여부 출력
        my_learned_list = pd.DataFrame(self.my_lecture, columns= \
                                        ['과목코드']).values
        df_all_list = pd.DataFrame(lecture_in_2022, columns = \
                                        ['분야', '교과목번호', '교과목명', "학점"]).values.tolist()
        lec_list=[]

        for lec in df_all_list:
            lec_info = {"isClear":"", "lecture_name":"", "grade":"", "previous_lecture_name":""}
            if lec[0] == specific_field:
                if lec[1] in my_learned_list:
                    #print(f"\t\t(이  수) {lec[2]} {lec[3]}")
                    lec_info["isClear"]="(이  수)"
                else:
                    #print(f"\t\t(미이수) {lec[2]} {lec[3]}")
                    lec_info["isClear"]="(미이수)"
                
                lec_info["lecture_name"] = lec[2]
                lec_info["grade"] = lec[3]
                lec_list.append(lec_info)
            
        
        return lec_list

class LecField:
    def __init__(self):
        self.field = {"개신기초교양":0, "일반교양":0, "확대교양":0, "자연이공계기초과학":0, "전공필수":0, "전공선택":0}
        self.sub_field = {"개신기초교양": {"인성과비판적사고":0, "의사소통":0, "영어":0,"정보문해":0}, \
                                "일반교양":{"인간과문화":0, "사회와역사":0, "자연과과학":0}, \
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":0,"예술과체육":0}}
        self.essential_code = {}
    def get_field(self, year = 2019):
        if year == 2019:
            self.field = {"개신기초교양":15, "일반교양":12, "확대교양":3, \
                            "자연이공계기초과학":12, "전공필수":34, "전공선택":44}
            self.sub_field = {"개신기초교양": {"인성과비판적사고":3, "의사소통":3, "영어":3,"정보문해":6}, \
                                "일반교양":{"인간과문화":3, "사회와역사":3, "자연과과학":3}, \
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":3,"예술과체육":0}}
            self.essential_code = {"자연이공계기초과학": ["0941002", "0941003", "0941006", "0941007"], \
                                    "전공필수": ['5110090',	'5110091',	'5110003',	'5110005',	'5110046',	'5110092',	\
                                        '5110009',	'5110011',	'5110014',	'5110094',	'5110016',	'5110095',	'5110107',	\
                                        '5110023',	'5110096',	'5110097',	'5110086',	'5110100']}
        elif year >= 2020:
            self.field = {"개신기초교양":15, "일반교양":9, "확대교양":3, "자연이공계기초과학":6, "전공필수":28, "전공선택":50}
            self.sub_field = {"개신기초교양":{"인성과비판적사고":3, "의사소통":3, "영어":3,"정보문해":6},\
                                "일반교양":{"인간과문화":3, "사회와역사":3, "자연과과학":3},\
                                "확대교양":{"미래융복합":0,"국제화":0,"진로와취업":0,"예술과체육":0}}
            self.essential_code = {"전공필수": ['5110001',	'5110122',	'5110123',	'5110005',	\
                                    '5110121',	'5110014',	'5110032',	'5110126',	'5110011',	'5110016',	'5110018',	\
                                    '5110130',	'5110131',	'5110133',	'5110135']}
        return self
