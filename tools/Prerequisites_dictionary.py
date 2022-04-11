class Prerequisites:
    def __init__(self, key, value):
        self.key=key
        self.value=value 

upper_subject=['5110007',   #c++
                '5110011',  #컴퓨터구조 
                '5110013',  #선형대수학
                '5110025',  #데이터베이스시스템
                '5110089',  #분산컴퓨팅시스템
                '5110099',  #알고리즘
                '5110107']  #마이크로프로세서

lower_subject=[ '0914002',  # 기초컴퓨터프로그래밍
                '5110128',  # 논리회로및설계
                '0621003',  # 수학2
                '5110014',  # 데이터구조
                '5110012',  # 정형문법 및 자동화 이론
                '5110014',  # 데이터 구조
                '5110011']  # 컴퓨터구조

d = {} # 빈 딕셔너리 생성

for i in range(0,6+1):    #  for문으로 딕셔너리에 상위과목코드(key) : 선수과목코드(value) 의 형태추가
    temp=Prerequisites(upper_subject[i],lower_subject[i])
    d[temp.key]=temp.value

print(d)