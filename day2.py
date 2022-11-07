# #3번

# su = 1; tot = 0; n = 1

# while su < 100:
#     if n % 2 == 0 :
#         tot += su
#         print(su)
        
#     else:
#         k = -1 * su
#         tot += k
#         print(k)
    
#     n += 1
#     su += 2

# print(tot)

# #4번
# i = 0

# while i <= 5:
#     print('*'*i)
#     i += 1


# 5번
# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i,'*',j, '=',i*j)
#         j += 1
#     i += 1

# #6번
# import random

# num = random.randint(1, 10)

# while True :
#     a = int(input())
#     if a == num:
#         print("정답!")
#         break
#     else:
#         print("실패")
#         continue

#7번

# 입력 : 사번, 이름, 기본급, 입사년
# 출력 : 사번, 이름, 기본급, 근무년수, 근속수당, 공제액, 수령액

# import time

# yn = 'y'
# count = 0

# result = ''
# now = time.localtime()

# today = int(now.tm_year)

# while yn == 'y':
#     data = input('사번, 이름, 기본급, 입사년도 입력하세요:')
    
#     list = data.split(',')
    
#     no = list[0]
#     name = list[1]
#     pay = int(list[2])
#     year = int(list[3])
#     year2 = int(today) - int(year)
    
#     if year2 >= 9:
#         pay2 = 1500000
#     elif year2 >= 6:
#         pay2 = 1000000
#     else:
#         pay2 = 500000
        
#     totalpay = pay + pay2
    
#     if totalpay >= 5000000:
#         tax = totalpay * 0.03
#     elif totalpay >= 4000000:
#         tax = totalpay * 0.02
#     else : 
#         tax = totalpay * 0.01
#     #실수령액    
#     realpay = totalpay - tax
#     #처리건수 증가
#     count += 1
#     #출력
#     result += '%s\t%s\t%d\t%d\t%d\t%d\t%d\n' %(no, name, pay, year2, pay2, tax, realpay)
#     yn = input('계속 입력하시겠습니까? [y/n]')
    
    

# print('사번\t이름\t기본급\t근무년수\t근속수당\t공제액\t수령액\n')
# print(result)
# print('처리 건수: %d' %count)

#Function

# def addfn(a,b):
#     res = a + b
#     return res

# print(addfn(10,20))
# print(addfn(25.6, 50.9))

# def func(name):
#     print("Hello!", name)

# print(func('seungsu'))

# def add(a,b):
#     ans = a + b
#     return ans
    
# def sub(a,b):
#     ans = a - b
#     return ans
    
# def mul(a,b):
#     ans = a * b
#     return ans
    
# def div(a,b):
#     ans = a / b
#     return ans


# def iso(arg):
#     return arg % 2 == 1

# res = {x : x * 2 for x in range(1,11) if iso(x)}

# print(type(res))
# print(res)

# player = 'golbal'

# def func():
#     name = 'hongil'
#     print(name, player)
    
    
# func()


# def add(*x):
#     return x + x

# print(add(100,20,50,99))

### lambda 
#print((lambda x, y : x + y)(10,20))

# print(list(filter(lambda x: x % 2 , range(10))))

# res = list(map(lambda x: x ** 2, range(10)))
# print(res)

###reduce(함수, 시퀀스(ordered))
# from functools import reduce
# res = reduce(lambda x, y: x + y, [0,1,2,3,4,5,6,7])
# print(res)

# res = list(filter(lambda x: x < 10, range(100)))
# print(res)


###재귀함수

# def func(x):
#     if x == 0:
#         print('END')
        
#     else:
#         print(x, end= ' ')
#         func(x-1)

# func(5)

# def func(x):
#     print(x)
    
#     if x == 1:
#         print("FIN!")
#         return True
#     return x + func(x-1)
# a = 10
# re = func(a)
# print(a, '까지 합은?', re)

###factorial
# def factorial(x):
#     if x == 0:
#         return 1
#     print(x)
#     return x * factorial(x-1)

# ans = factorial(10)
# print(ans)

# # 1번
# data = [1,3,5,7,9,2,4,6]

# def check(data, a):
#     if a in data:
#         print(a, ': 있어요')
#     else:
#         print(a, ': 없어요')

# ans = check(data, 8)
# print(ans)


##내가 만든 모듈~
# import day2_module

# arr1 = [1,2,3]
# arr2 = [2,3,4]

# day2_module.kbs()

###class 설명
# #클래스
# class Human():
#     #초기화 함수
#     def __init__(self,name,addr,gender) -> None:
#         self.name = name
#         self.addr = addr
#         self.gender = gender
        
#     def __str__(self) -> str:
#         return "{}님의 주소는 {}이고, 성별은 {}입니다.".format(self.name, self.addr, self.gender)
        
# #인스턴스

# you = Human('seungsu', 'Goyang', 'man')
# me = Human('yeounji', 'Seoul', 'woman')

# print(you)
# print(me)

##prac

# class Food():
    
#     def __init__(self,name,price,star) -> None:
#         self.name = name
#         self.price = price
#         self.star = star
    
#     def __str__(self) -> str:
#         if self.star >= 4:
#             return "추천메뉴"
#         elif self.star >= 2:
#             return "일반메뉴"
#         else:
#             return "개발필요"
        
# menu1 = Food('ramen', 8000, 5)
# menu2 = Food('gogi', 10000, 3)

# print(menu1)
# print(menu2)


