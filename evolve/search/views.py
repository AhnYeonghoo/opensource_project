from django.shortcuts import render, redirect, get_object_or_404
import requests
from . import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook

# Create your views here.

def index(req):
    
    '''
    main page render를 위한 함수
    '''
    
    return render(req, "index.html")

def upload_file(req):
    
    '''
    사용자에게 파일 업로드 받아서 원하는 title대로 DB에 저장해주는 함수
    '''
    
    if req.method == "POST":
        title = req.POST.get('title')
        uploaded_file = req.FILES['uploaded_file']
        
        document = models.Document(
            title = title,
            uploaded_file = uploaded_file
        )
        document.save()
        documents = models.Document.objects.all()
        
        return render(req, "upload-file.html", context={
            "files" : documents
        })
    else:
        title = req.POST.get('title')
        uploaded_file = req.FILES['uploaded_file']
        
        document = models.Document(
            title = title,
            uploaded_file = uploaded_file
        )
        document.save()
        documents = models.Document.objects.all()
        
        return render(req, "upload-file.html", context={
            "files" : documents
        })
        
        

def recomand(req):
    
    '''
    게임, 앱, 네트워크, 임베디드, 인공지능 키워드에 따라 과목 출력해주는 함수
    '''
    
    if req.POST.get("game"):
        game_list = models.Game.objects.all()
        context = {"game" : game_list}
        return render(req, 'game_list.html', context)
    
    elif req.POST.get('ai'):
        ai_list = models.Ai.objects.all()
        context = {"ai": ai_list}
        return render(req, "ai_list.html", context)
    
    elif req.POST.get('embedded'):
        embed_list = models.Embedded.objects.all()
        context = {"embedded": embed_list}
        return render(req, "embed_list.html", context)
    
    elif req.POST.get('network'):
        network_list = models.Network.objects.all()
        context = {"network": network_list}
        return render(req, "network_list.html", context)
    
    elif req.POST.get('app'):
        app_list = models.Application.objects.all()
        context = {"app": app_list}
        return render(req, "app_list.html", context)
    
    
def goto_recomand(req):
    
    return render(req, "recomand.html")

def goto_upload_file(req):
    
    return render(req, "upload-file.html")

def contact(req):
    
    return render(req, "contact.html")