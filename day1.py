"""
1번

i = 1
a = 0

while i < 100:
    if i % 3 == 0:
        a += i
    i += 1

print(a)
"""

"""
2번
i = 1
a = 0

while i < 100:
    if i % 3 == 0 and i % 2 != 0:
        a += i
    i += 1

print(a)
"""

"""
3번
cnt =1
arr = []
ans = 0

for i in range(1, 100, 2):
    if cnt % 2 != 0:
       arr.append(-i)
    else:
        arr.append(i)
    cnt += 1
i = 0
while i <= 49:
    ans = ans + arr[i]
    i += 1

print(ans)

"""

"""
4번
i = 0

while i <= 5:
    print('*'*i)
    i += 1

"""

"""
5번
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(i,'*',j, '=',i*j)
        j += 1
    i += 1

"""

"""
6번
import random

num = random.randint(1, 10)

while True :
    a = int(input())
    if a == num:
        print("정답!")
        break
    else:
        print("실패")
        continue
"""

"""
7번
while True:
    a, b, c, d = map(str, input().split())
    d = int(d)
    c = int(c)
    mon = 0
    tax = 0
    year = 2022 - d

    if year <= 3:
        mon = 500000
    elif 4 <= year <= 8:
        mon = 1000000
    elif 9 <= year:
        mon = 1500000

    if c + mon >= 5000000:
        tax = (c+mon) * 0.03
    elif 5000000 > c + mon >= 4000000:
        tax = (c+mon) * 0.02
    elif 4000000 > c:
        tax = (c+mon) * 0.01

    print(a, b, c, year, mon, tax, c+mon-tax)
    print("계속하시겠습니까? [Y/N]")
    answ = input()
    if answ == 'Y':
        continue
    else:
        break


"""

"""
8번
panmae = [55,67,100]
insa = [50,60,100]

for i in range(3):
    print(panmae[i] - insa[i])

"""

"""
9번

ans = 0

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
       ans += i

print(ans)
"""

"""
10번
for i in range(2, 10):
    for j in range(1,10):
        print(i, '*', j, '=', i*j)

"""