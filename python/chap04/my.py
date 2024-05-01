'''
리스트는 변경이 가능한 mutable이다. 
len은 길이
append, insert.꼽사리, del.인덱스= pop, remove.해당값 자체
call by value
call by reference구분 잘 하기 

'''
'''
#피타고라스의 정리를 만족하는 세 정수를 찾아보자
n_list = [(x,y,z) for x in range (1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print(n_list)'''


'''
#23
string = 'PYTHON'
print(string[::-1])
'''
'''
#25
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
'''
'''
#27
url = "http://sharebook.kr"
surl = url.split(".")
print(surl[-1])
'''
'''
#35
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
'''
'''
#40
data = "   삼성전자    "
print(data.strip())
'''
'''
#43
#upper, lower, capitalize
a ="hello"
a = a.capitalize()
print(a)
'''
'''
#endswith, startswith

file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
'''
'''
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove("럭키")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)
'''
'''
#66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))
'''

'''
#73 숫자 1 이 저장된 튜플을 생성하라.
tp = (1,)
print(tp)
'''

'''
#75 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print(type(t))
'''

'''
#79다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
'''

'''
#81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)
'''

'''
#98 update
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
'''

'''
#99 zip
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
a = dict(zip(keys, vals))
print(a)
'''

'''
#116
tt = input("현재 시각은? (입력 __:__) ")
if tt.endswith("00"):
    print("정각입니다.")
else:
    print('정각이 아님')
'''
'''
#123
m = {"달러":1167, "엔":1.096, "유로":1268, "위안":171}
user_money, user_nation = input("환율 계산").split()
print(m[user_nation]*int(user_money),"원")
'''
'''
#129
num = input("주민번호를 입력하시오 : ").split("-")
check_n = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
check_n1 = check_n[:6]
check_n2 = check_n[-6:]
sum = 0

for i in range(len(check_n1)):
    sum += int(num[0][i])*check_n1[i]

for j in range(len(check_n2)):
    sum += int(num[1][j])*check_n2[j]

a = 11 - sum % 11
print(a)
print(num[1][-1])
#제발ㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹㄹ str int 구분하기
if a != int(num[1][-1]):
    print("유효하지 않은 주민등록번호입니다.")
else :
    print("유효")
'''
'''
#174
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])
'''
'''
#177
my_list = my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1,0,-1):
    print(my_list[i], my_list[i-1])
'''

'''import datetime
a = datetime.datetime.now() 
print(a)
'''

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

print(icecream['메로나'])
