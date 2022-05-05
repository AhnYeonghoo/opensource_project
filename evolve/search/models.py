from django.db import models
import pandas as pd

# Create your models here.


file = pd.read_csv("../etc/1학기_전공.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()
# pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )


class FirstSemesterMajor(models.Model):
    
    # 1학기 전공에 대한 정보
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    


# pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )


class SecondSemesterMajor(models.Model):
    
    # 2학기 전공
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    

file = pd.read_csv("../etc/1학기_소웨전공.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()


class FirstSemesterSWMajor(models.Model):
    
    # 1학기 소웨 전공
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    

file = pd.read_csv("../etc/2학기_소웨전공.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()


class SecondSemesterSWMajor(models.Model):
 
    # 2학기 소웨 전공
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    



file = pd.read_csv("../etc/1학기_자연이공계기초.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()


class FirstNaturalScience(models.Model):
    
    # 1학기 자연이공계기초
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    def get_info(self):
        return pd_file.values.tolist()


file = pd.read_csv("../etc/2학기_자연이공계기초.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()



class SecondNaturalScience(models.Model):
    
    # 2학기 자연이공계기초
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    


file = pd.read_csv("../etc/1학기_ocu.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()



class Ocu(models.Model):
    
    # 1학기,2학기 OCU
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    


file = pd.read_csv("../etc/1학기_개신기초교양.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()



class FirstGaesinBasicCulture(models.Model):
    
    # 1학기 개신기초교양
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()


file = pd.read_csv("../etc/2학기_개신기초교양.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()


class SecondGaesinBasicCulture(models.Model):
    
    # 2학기 개신기초교양
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    


# file = pd.read_csv("../etc/1학기_일반교양.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()



class FirstBasicCulture(models.Model):
    
    # 1학기 일반교양
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    


file = pd.read_csv("../etc/2학기_일반교양.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()



class SecondBasicCulture(models.Model):
    
    # 2학기 일반교양
    
    학년 = models.CharField("학년", max_length=150)
    # 학년 = pd_file['학년'].to_string()
    과목구분 = models.CharField("과목구분", max_length=150)
    # 과목구분 = pd_file['과목구분']
    과목코드 = models.CharField("과목코드", max_length=150)
    # 과목코드 = pd_file['과목코드']
    과목명 = models.CharField("과목명", max_length=200)
    # 과목명 = pd_file['과목명']
    학점 = models.CharField("학점", max_length=150)
    # 학점 = pd_file['학점']
    학점부여 = models.CharField("학점부여", max_length=150)
    # 학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
