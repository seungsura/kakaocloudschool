
# class Counter:
    
#     def __init__(self, limit):
#         self.limit = limit
#         self.value = 0
#         #인스턴스를 생성할 때 limit만 값을 받고, value는 0으로 초기화
#     def set(self, new_value):
#         self.value = new_value if new_value >= 0 and new_value < self.limit else 0
        
#     def tick(self):
#         #value 값을 1 증가시킴
#         self.value += 1
        
#         if self.value == self.limit:
#             self.value = 0
#             return True
#         return False
    
#     def __str__(self):
#         #zfill : 자릿수만큼 출력
#         return str(self.value).zfill(2)
    
# #인스턴스 생성

# count1 = Counter(30)


# for i in range(45):
#     count1.tick()
#     print(count1)
    
# #타이머 값을 0으로 세팅
# count1.set(5)
# print(count1)

# class Singer:
#     title_song = '아리랑'
    
#     def sing(self):
#         msg = '노래는'
#         print(msg, self.title_song, '룰루랄라~')
        
# boys = Singer() #객체생성
# print('타이틀 곡은~', Singer.title_song)
# print('boys:')
# boys.sing()

# girls = Singer()
# print('girls:')
# girls.sing()

# girls.title_song = '댄싱퀸'
# girls.sing()
# girls.co = 'FM'
# print('소속사:', girls.co)

# print(Singer.title_song)
# Singer.title_song = '아름다운 강산'
# print('타이틀 노래는~', Singer.title_song)
# boys.sing()
# girls.sing()
# print(Singer.title_song)