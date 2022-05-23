from django.shortcuts import render, redirect, get_object_or_404
import requests
from . import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook
import pandas as pd
import os
from src import load_data

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

def calculator(request):
    c = load_data.MyInfo()
    l = []
    for field, my_score in c.my_ge.field.items():
        a = {"field":field, "my_score":my_score, "min_score":c.min_ge.field[field], "sub_field":[]}
        if c.is_specific(field):
            for sub_field, m_score in c.my_ge.sub_field[field].items():
                b = {"sub_field":sub_field,"my_score":m_score, "min_score":c.min_ge.sub_field[field][sub_field], "lec_info":[]}
                if m_score < b["min_score"]:
                    b["lec_info"]=c.print_ge(sub_field)
                a["sub_field"].append(b)
        l.append(a)
    
    context = {
        "sd":l
    }
    #c.print_my_lec()
    return render(request, "calculator.html", context)
    

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
        
def get_my_lecture(request):

    return render(request, "upload-file.html")


