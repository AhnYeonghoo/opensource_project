from django.shortcuts import render, redirect, get_object_or_404
import requests
from . import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook
import pandas as pd
import os

# Create your views here.

def index(request):
    
    '''
    main page render를 위한 함수
    '''
    
    return render(request, "index.html")

def upload_file(request):
    
    '''
    사용자에게 파일 업로드 받아서 원하는 title대로 DB에 저장해주는 함수
    '''
    
    if request.method == "POST":
        title = request.POST.get('title')
        uploaded_file = request.FILES['uploaded_file']
        
        document = models.Document(
            title = title,
            uploaded_file = uploaded_file
        )
        document.save()
        documents = models.Document.objects.all()
        
        return render(request, "upload-file.html", context={
            "files" : documents
        })
    else:
        title = request.POST.get('title')
        uploaded_file = request.FILES['uploaded_file']
        
        document = models.Document(
            title = title,
            uploaded_file = uploaded_file
        )
        document.save()
        documents = models.Document.objects.all()
        
        return render(request, "upload-file.html", context={
            "files" : documents
        })
        
        

def recomand(request):
    
    '''
    게임, 앱, 네트워크, 임베디드, 인공지능 키워드에 따라 과목 출력해주는 함수
    '''
    
    if request.POST.get("game"):
        game_list = models.Game.objects.all()
        context = {"game" : game_list}
        return render(request, 'game_list.html', context)
    
    elif request.POST.get('ai'):
        ai_list = models.Ai.objects.all()
        context = {"ai": ai_list}
        return render(request, "ai_list.html", context)
    
    elif request.POST.get('embedded'):
        embed_list = models.Embedded.objects.all()
        context = {"embedded": embed_list}
        return render(request, "embed_list.html", context)
    
    elif request.POST.get('network'):
        network_list = models.Network.objects.all()
        context = {"network": network_list}
        return render(request, "network_list.html", context)
    
    elif request.POST.get('app'):
        app_list = models.Application.objects.all()
        context = {"app": app_list}
        return render(request, "app_list.html", context)
    
    
def goto_recomand(request):
    
    return render(request, "recomand.html")

def goto_upload_file(request):
    
    return render(request, "upload-file.html")

def contact(request):
    
    return render(request, "contact.html")

def get_my_lecture(request):
    
    file_name= models.Document.title
    file = models.Document.uploaded_file
    
    df = pd.read_excel(file, usecols=[i for i in range(0, 9)], dtype=str)
    df.columns = ["구분", "영역", "세부영역", "수강년도", "학기", "과목코드", "과목명", "학점", "이수구분"]
        
    df = df.sort_values(["과목코드"]).dropna(subset="과목코드").reset_index(drop=True)
    if(type == "all"):
        return df
    else:
        return df["과목코드"].tolist()
    

def read_user_lecture(request):
    
    file = pd.read_csv("../media/result/learned.csv", dtype="str")
    lecture_name = file["교과목명"]
    all_lecture = models.GaesinBasicCulture.objects.all()
    context = {}
    if all_lecture["과목명"] in lecture_name:
        context["complete"] = lecture_name
    else:
        context["not_com"] = lecture_name
    
    return (request, "result-user-lecture.html", context)
        
    

def calculator(request):
    
    if request.POST.get("calculator"):
        document = models.Document.objects.all()
        context = {"doc": document}
    else:
        document = models.Document.objects.all()
        context = {"doc": document}
        
    
    return (request, "calculator.html", context)

def get_my_lecture(request):
    
    
    if request.POST.get("my_lec"):
        df =  pd.read_csv("../media/result/learned.csv",usecols=[i for i in range(0,9)])
        df.columns = ["구분", "영역", "세부영역", "수강년도", "학기", "과목코드", "과목명", "학점", "이수구분"]
        df = df.sort_values(["과목코드"]).dropna(subset="과목코드").reset_index(drop=True)
        context = {"my_lec":df}
        return (request, "my-lecture.html", context)
    else:
        redirect(request)
        


class Old_and_new:
    
    '''
    신설과목, 삭제된 과목 구분함
    
    '''
    list_ = [
     ['5110090', '설계포트폴리오I','5110122','미래설계탐색','동일'], 
     ['5110091', '설계포트폴리오II', '5110123', '미래설계준비', '동일'],
     ['5110006', '컴퓨터공학개론', '5110134', '인공지능', '동일'],
     ['5110046', '정보처리실험', '5110125', '오픈소스기초프로젝트', '동일'],
     ['5110092', '설계포트폴리오III', '5110121', '미래설계구현', '동일'],
     ['5110093', '전기전자회로', '5110124', '전자회로및설계', '동일'],
     ['5110003', '디지털공학', '5110128', '논리회로및설계', '동일' ],
     ['5110094', '설계포트폴리오IV', '5110126', '창업탐색', '동일'],
     ['5110009', '전자및디지털회로설계실험', '5110129', '오픈소스개발프로젝트', '동일'],
     ['5110012', '정형문법및자동화이론', '5110127', '오토마타이론', '동일'],
     ['5110095', '설계포트폴리오V', '5110130', '창업기획', '동일'],
     ['5110096', '설계포트폴리오VI', '5110131', '창업설계', '동일'],
     ['5110082', '응용프로그램실험', '5110132', '오픈소스전문프로젝트', '동일'],
     ['5110097', '컴퓨터공학설계', '5110133', '산학프로젝트(종합설계)', '동일'],
     ['5110086', '캡스톤디자인I', '5110135', '캡스톤디자인', '동일'],
     ['5110048', '산학초청세미나I', '5100012', '창업산학초청세미나I', '동일'],
     ['5110088', '캡스톤디자인II', '5110165', '창업파일럿프로젝트(캡스톤디자인)', '동일'],
     ['5110049', '산학초청세미나II', '5100013', '창업산학초청세미나II', '동일'],
     ['5110110', '인공신경망개론', '5110140', '인공신경망', '동일'],
     ['5110023', '디지털신호처리', '5110136', '머신러닝', '동일'],
     ['', '', '5110137', '사이버물리시스템', '신설'],
     ['', '', '5110138', '소프트웨어실전영어', '신설'],
     ['', '', '5110141', '자연언어처리', '신설'],
     ['', '', '5110142', '데이터마이닝', '신설'],
     ['5110008', '공학수학', '', '', '삭제'],
     ['5110100', '설계포트폴리오VII', '', '', '삭제'],
     ['5110024', '컴파일러', '', '', '삭제'],
     ['5110103', '응용프로그래밍II', '5110145', '컴퓨터프로그래밍', '동일'],
     ['5110055', '회로이론', '5110147', '논리회로', '동일'],
     ['5110115', '알고리즘기초', '5110151', '알고리즘', '동일'],
     ['5110104', 'Java프로그래밍', '5110152', '객체지향프로그래밍', '동일'],
     ['5110071', '현장실무I', '5110157', '산학프로젝트', '동일'],
     ['5110076', '현장실무II', '5110162', '창업파일럿프로젝트', '동일'],
     ['5110112', '분산컴퓨팅', '5110159', '클라우드컴퓨팅', '동일'],
     ['', '', '5110146', '고급컴퓨터프로그래밍' , '신설'],
     ['', '', '5110148', '컴퓨터응용프로그래밍' , '신설'],
     ['', '', '5110149', '확률및통계' , '신설'],
     ['', '', '5110150', '오토마타' , '신설'],
     ['', '', '5110153', '컴퓨터공학설계' , '신설'],
     ['', '', '5110154', '소프트웨어실전영어' , '신설'],
     ['', '', '5110155', '인공지능' , '신설'],
     ['', '', '5110156', '정보보호' , '신설'],
     ['', '', '5110158', '오픈소스소프트웨어' , '신설'],
     ['', '', '5110160', '머신러닝' , '신설'],
     ['', '', '5110161', '빅데이터' , '신설'],
     ['5110102', 'C프로그래밍I', '', '', '삭제'],
     ['5110053', '디지털공학', '', '', '삭제'],
     ['5110059', '컴퓨터그래픽', '', '', '삭제'],
     ['5110113', 'H/W응용시스템설계', '', '', '삭제'],
     ['5110114', '디지털게임설계및제작', '', '', '삭제'],
     ['5110116', '시스템설계및분석', '', '', '삭제'],
     ['5110073', '엔터테인먼트공학', '', '', '삭제'],
     ['5110117', '디지털컨텐츠제작', '', '', '삭제'],
     ['5110075', '멀티미디어저작기술', '', '', '삭제'],
     ['5110077', '휴먼인터페이스', '', '', '삭제'],
     ['5110078', '엔터테인먼트융합', '', '', '삭제'],
     ['5110105', '리눅스시스템', '', '', '삭제'],
     ]
    
    # 신설 과목만 뱉기 
    def get_new_lecture(self):
       new_lecture = []
          
       for i in range(len(self.list_) - 1):
           if len(self.list_[i]) != 0 and self.list_[i][0] == '':
               new_lecture.append([x for x in self.list_[i]])
    
       return new_lecture
   
    # 삭제 과목만 뱉기
    def get_old_lecture(self):
       old_lecture = []

       for i in range(len(self.list_) - 1):
           if len(self.list_[i]) != 0 and self.list_[i][2]=='':
               old_lecture.append([x for x in self.list_[i]])
        
       return old_lecture
   
   # 모든 과목 뱉기
    def get_all_lecture(self):
       return self.list_
   
   # 개정된 과목만 뱉기
    def get_revision_lecture(self):
       revision_lecture = []
       
       for i in range(len(self.list_) - 1):
           if len(self.list_[i]) != 0 and not self.list_[i][0] == '' and not self.list_[i][2] == '':
               revision_lecture.append([x for x in self.list_[i]])
           
       return revision_lecture

class Prerequisites:
    subject_pair_dic = {  # 상위과목 : 선수과목
        '5110007' : '0914002',   # c++ : 기초컴퓨터프로그래밍
        '5110011' : '5110128',   # 컴퓨터구조 : 논리회로및설계
        '5110013' : '0621003',   # 선형대수학 : 수학2
        '5110025' : '5110014',   # 데이터베이스시스템 : 데이터구조
        '5110089' : '5110012',   # 분산컴퓨팅시스템 : 정형문법 및 자동화 이론
        '5110099' : '5110014',   # 알고리즘 : 데이터구조
        '5110107' : '5110011'    # 마이크로프로세서 : 컴퓨터구조
    }

    def get_lower_code(self, upper_code):
        for i in self.subject_pair_dic:
            if i == upper_code:
                return self.subject_pair_dic[i]

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

all_ON_lecture = Old_and_new().get_all_lecture()
all_lecture = pd.read_excel("../source/all_lecture.xlsx",dtype = str)
lecture_in_2022 = pd.read_excel("../source/2022lecture.xlsx", dtype = str)
prerequisites = Prerequisites().subject_pair_dic

def print_my_ge_lec(specific_field):
        
    my_ge_lec_list = pd.DataFrame(lecture_in_2022, columns = \
                                        ['분야', '교과목명']).values.tolist()
    for i in range(len(my_ge_lec_list)):
        if(my_ge_lec_list[i][0] == specific_field):
            print("\t{}".format(my_ge_lec_list[i][1]))

def print_ge(specific_field):         # 세부영역 이수 여부 출력
       
    my_learned_list = pd.DataFrame(my_lecture, columns= \
                                    ['영역','세부영역','교과목번호','교과목명','이수구분']).values.tolist()
    df_all_list = pd.DataFrame(lecture_in_2022, columns = \
                                    ['분야', '교과목번호', '교과목명']).values.tolist()
    
    for i in range(len(df_all_list)):
        if df_all_list[i][0] == specific_field:
            flag=0
            for j in range(len(my_learned_list)):
                if df_all_list[i][1] == my_learned_list[j][2]:
                    flag=1
            if flag == 1:
                print("\t\t{} (이수)".format(df_all_list[i][2]))
            else:
                print("\t\t{} (미이수)".format(df_all_list[i][2]))