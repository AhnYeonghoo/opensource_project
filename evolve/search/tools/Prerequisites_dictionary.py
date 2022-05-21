class Prerequisites:
    subject_pair_dic = {  # 상위과목 : 선수과목
        '5110007' : '0914002',   # c++ : 기초컴퓨터프로그래밍
        '5110011' : '5110128',   # 컴퓨터구조 : 논리회로및설계
        '5110013' : '0621003',   # 선형대수학 : 수학2
        '5110025' : '5110014',   # 데이터베이스시스템 : 데이터구조
        '5110089' : '5110012',   # 분산컴퓨팅시스템 : 정형문법 및 자동화 이론
        '5110099' : '5110014',   # 알고리즘 : 데이터구조
        '5110107' : '5110011'    # 마이크로프로세서 : 컴퓨터구조
    }

    def get_lower_code(self, upper_code):
        for i in self.subject_pair_dic:
            if i == upper_code:
                return self.subject_pair_dic[i]