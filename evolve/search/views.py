from django.shortcuts import render, redirect, get_object_or_404
import requests
from . import models
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'index.html')


def print_list(req):
    gaesin = models.GaesinBasicCulture.objects.all()
    context = {}
    context["title"] = gaesin
    return redirect(req, "index.html", context)