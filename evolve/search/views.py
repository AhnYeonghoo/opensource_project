from django.shortcuts import render, redirect, get_object_or_404
import requests
from . import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook
import pandas as pd
import os
from src import load_data
from django.contrib.auth.decorators import login_required
URL_LOGIN = '/authenticated/login'
# Create your views here.

def index(request):
    
    '''
    main page render를 위한 함수
    '''
    
    return render(request, "index.html")

@login_required(login_url=URL_LOGIN)
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
        
        
@login_required(login_url=URL_LOGIN)
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
    
@login_required(login_url=URL_LOGIN)
def goto_recomand(request):
    
    return render(request, "recomand.html")

@login_required(login_url=URL_LOGIN)
def goto_upload_file(request):
    
    return render(request, "upload-file.html")

def contact(request):
    
    return render(request, "contact.html")

def calculator(request):
    """
    입학년도와 파일이름을 입력받아 해당 내용들을 calculator.html로 보내줌.
    """
    year = request.POST.get("year")
    file_name = request.POST.get("file_name")

    my_info = load_data.MyInfo()
    element = []
    major = []
    selection = []
    for field, my_score in my_info.my_ge.field.items():
        a = {"field":field, "my_score":my_score, "min_score":my_info.min_ge.field[field], "sub_field":[]}
        if my_info.is_specific(field):
            for sub_field, m_score in my_info.my_ge.sub_field[field].items():
                b = {"sub_field":sub_field,"my_score":m_score, "min_score":my_info.min_ge.sub_field[field][sub_field], "lec_info":[]}
                if m_score < b["min_score"]:
                    b["lec_info"]=my_info.print_ge(sub_field)
                a["sub_field"].append(b)
        elif field == "전공필수":
            major=my_info.print_need_lec()
        elif field == "전공선택":
            selection = my_info.print_ge("전공선택")
        element.append(a)
    
    context = {
        "sd":element,
        "major":major,
        "selection":selection,
    }
    #c.print_my_lec()
    return render(request, "calculator.html", context)

@login_required(login_url=URL_LOGIN)
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
        

@login_required(login_url=URL_LOGIN)
def get_my_lecture(request):

    return render(request, "upload-file.html")

def get_my_lecture(request):

    return render(request, "upload-file.html")


def calculator(request):
    
    if request.POST.get("calculator"):
        document = models.Document.objects.all()
        context = {"doc": document}
    else:
        document = models.Document.objects.all()
        context = {"doc": document}
        
    return (request, "calculator.html", context)