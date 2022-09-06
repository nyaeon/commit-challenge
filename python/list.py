#1----------------------
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨") #  insert(인덱스, 원소) 메소드로 특정 위치에 값을 끼어넣기
print(movie_rank)

"""
<결과값> 
['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
"""

#2----------------------
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2 # 두 리스트를 더하여 생성할 수 있다.
print(langs)

"""
<결과값>
['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
"""

#3----------------------
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums)) # 최댓값 출력
print("min: ", min(nums)) # 최솟값 출력

"""
<결과값>
max:  7
min:  1
"""

#4----------------------
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest)) # join 메소드> 리스트를 문자열로 붙일 수 있다.

"""
<결과값>
삼성전자
LG전자
Naver
SK하이닉스
미래에셋대우
"""

#5----------------------
string = "삼성전자/LG전자/Naver"
interest = string.split("/") # split> 문자열을 나눌 때 사용한다.
print(interest)

"""
<결과값>
['삼성전자', 'LG전자', 'Naver']
"""
