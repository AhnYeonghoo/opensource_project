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
    
    def get_info(self):
        return pd_file.values.tolist()


file = pd.read_csv("../etc/2학기_개신기초교양.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()



class Lecture(models.Model):
    
    # 개신기초교양만(10과목)
    
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
    
    def get_info(self):
        return pd_file.values.tolist()
    


file = pd.read_csv("../etc/2학기_일반교양.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()



