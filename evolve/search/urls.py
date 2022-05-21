from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "search"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("upload-file/", views.upload_file, name="upload_file"),
    path('recomand/', views.recomand, name="recomand"),
    path('goto_recomand/', views.goto_recomand, name="goto_recomand"),
    path('goto_upload_file/', views.goto_upload_file, name="goto_upload_file"),
    path("contact/", views.contact, name="contact"),
    path("read_user_lecture", views.read_user_lecture, name="read_user_lecture"),
    path("calculator", views.calculator, name="calculator"),
    path("get_my_lecture", views.get_my_lecture, name="get_my_lecture"),
    path("fuck", views.fuck, name="fuck"),
]
