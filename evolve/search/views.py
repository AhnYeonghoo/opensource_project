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

def print_my_ge_lec(specific_field):    # 나의 이수 강의 출력
    
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