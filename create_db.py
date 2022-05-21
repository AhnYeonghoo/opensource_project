import pandas as pd


file = pd.read_csv("./교육과정/1학기_전공.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()
pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# 1학기 전공 DB
class FirstSemesterMajor:
    
    학년 = pd_file['학년']
    과목구분 = pd_file['과목구분']
    과목코드 = pd_file['과목코드']
    과목명 = pd_file['과목명']
    학점 = pd_file['학점']
    학점부여 = pd_file['학점부여']
    
    def get_info(self):
        return pd_file.values.tolist()
    
# fsm = FirstSemesterMajor()
# fsm.get_info()

file = pd.read_csv("./교육과정/2학기_전공.csv", encoding='utf-8' ,dtype=str)
file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
pd_file = pd.DataFrame(file).dropna()
# pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 2학기 전공 DB
# class SecondSemesterMajor:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# ssm = SecondSemesterMajor()
# ssm.get_info()

# file = pd.read_csv("./교육과정/1학기_소웨전공.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 1학기 소웨 전공
# class FirstSemesterSWMajor:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# fssm = FirstSemesterSWMajor()
# fssm.get_info()

# file = pd.read_csv("./교육과정/2학기_소웨전공.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 2학기 소웨 전공
# class SecondSemesterSWMajor:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# sssm = SecondSemesterSWMajor()
# sssm.get_info()

# # 전공까지 완료

# file = pd.read_csv("./교육과정/1학기_자연이공계기초.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 1학기 자연이공계기초
# class FirstNaturalScience:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# fns = FirstNaturalScience()
# fns.get_info()

# file = pd.read_csv("./교육과정/2학기_자연이공계기초.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 2학기 자연이공계기초
# class SecondNaturalScience:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# sns = SecondNaturalScience()
# sns.get_info()

# file = pd.read_csv("./교육과정/1학기_ocu.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 1학기,2학기 OCU
# class Ocu:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# ocu = Ocu()
# ocu.get_info()


# file = pd.read_csv("./교육과정/1학기_개신기초교양.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 1학기 개신기초교양
# class FirstGaesinBasicCulture:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# fgbc = BasicCulture()
# fgbc.get_info()

# file = pd.read_csv("./교육과정/2학기_개신기초교양.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 2학기 개신기초교양
# class SecondGaesinBasicCulture:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# sgbc = SecondGaesinBasicCulture()
# sgbc.get_info()

# file = pd.read_csv("./교육과정/1학기_일반교양.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 1학기 일반교양
# class FirstBasicCulture:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# fbc = FirstBasicCulture()
# fbc.get_info()

# file = pd.read_csv("./교육과정/2학기_일반교양.csv", encoding='utf-8' ,dtype=str)
# file = file.filter(['학년','과목구분', '과목코드', '과목명', '학점', '학점부여' ])
# pd_file = pd.DataFrame(file).dropna()
# # pd_file = pd_file.query("개설학과=='컴퓨터공학과' or 개설학과=='소프트웨어학과' or 개설학과=='소프트웨어학부'" )

# # 2학기 일반교양
# class SecondBasicCulture:
    
#     학년 = pd_file['학년']
#     과목구분 = pd_file['과목구분']
#     과목코드 = pd_file['과목코드']
#     과목명 = pd_file['과목명']
#     학점 = pd_file['학점']
#     학점부여 = pd_file['학점부여']
    
#     def get_info(self):
#         return pd_file.values.tolist()
    
# sbc = SecondBasicCulture()
# sbc.get_info()