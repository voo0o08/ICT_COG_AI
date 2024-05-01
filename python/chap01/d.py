'''
a,b = map(int,input().split())
score = [x for x in input().split() if int(x)<b]
print(' '.join(score))
'''
'''
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        exit()
        
N = int(input())
L = list(n for n in map(int, input().split()))
print(min(L),max(L))
'''
'''
price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)
'''
'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
'''
'''
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print("naver", "kakao", "samsung", sep=";")
'''
import random
a = [1,23,4,5,6]
print(random.choice(a))