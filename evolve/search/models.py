from django.db import models
import pandas as pd

# Create your models here.


class GaesinBasicCulture(models.Model):
    
    # 개신기초교양을 제외한 나머지 모든 과목들

    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    # 학점부여 = pd_file['학점부여']
    
    # def get_info(self):
    #     return pd_file.values.tolist()

    

class Document(models.Model):
    #..
    title = models.CharField(max_length=200)
    uploaded_file = models.FileField(upload_to="result/")
    date_time_of_upload = models.DateTimeField(auto_now=True)
    
    
'''
추천 시스템을 위한 데이터베이스 테이블
'''
    
class Game(models.Model):
    '''
    게임
    '''
    lecture_name = models.CharField(max_length=200)
    
    
class Network(models.Model):
    '''
    네트워크 및 보안
    '''
    lecture_name = models.CharField(max_length=200)
   
class Application(models.Model):
    '''
    앱, 웹
    '''
    lecture_name = models.CharField(max_length=200)


class Embedded(models.Model):
    '''
    임베디드
    '''
    lecture_name = models.CharField(max_length=200)
    
class Ai(models.Model):
    '''
    인공지능
    '''
    lecture_name = models.CharField(max_length=200)