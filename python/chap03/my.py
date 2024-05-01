''' 1번
for i in range(1,10):
    for k in range(1,10):
        print(i*k, end=' ')
    print("\n")
'''
'''
x = int(input("첫번째 정수를 입력하시오 : "))
y = int(input("두번째 정수를 입력하시오 : "))
i = 1
div = []
while i<=x and i<=y:
    if x % i == 0 and y % i == 0:
        div.append(i)
    i += 1
print(div[-1])
'''

''' 3번
my = 1000
year = 0
while my <= 2000:
    my += my*7/100
    year += 1
print(year,"년")
'''
'''
i = list(range(1,100,2))
k = list(range(3,102,2))
sum = 0
for j in range(len(i)):
    sum += i[j]/k[j]
print(sum)
'''

'''
for i in range(1,11):
    print(f"{i}".ljust(5),f"{i**2}".ljust(5), f"{i**3}".ljust(5), i**4)
    '''

'''
import random
for i in range(10):
    first = random.randint(1,6)
    second = random.randint(1,6)
    print(f"첫번째 주사위={first} 두번째 주사위={second}")
'''

