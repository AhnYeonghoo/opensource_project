from django.shortcuts import render, redirect, get_object_or_404
import requests
from . import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook

# Create your views here.

def index(req):
    gaesin = models.Lecture.objects.all()
    context = {"gaesin" : gaesin }
    return render(req, "index.html", context)

def upload_file(req):
    
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
        