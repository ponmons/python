# -*- coding: utf-8 -*-
# ch09 리스트의 기초

l=[1,2,"Great"]
print l[0]

l = range(10)
print l
print l[::2] # 슬라이싱 두칸씩 건너뜀
print l*2, l+[3,4,5,2], len(l)
print ;
a=['spam', 'eggs', 123,1234]
a[0:2] = [1,12]
print a
a[0:1] = [1,2,3] 
print a
a[:1:] = ['ham'] # 치환 
print a 
a[:0] = ['two'] # 앞자리에 삽입
print a 

s=[1,2,3]
t=['begin', s, 'end'] # 중첩 리스트 
print t[1][1]

mon, tue, wed, thur, fri, sat, sun = range(7)
print mon, tue, wed, thur, fri, sat, sun 

it = [('one',1), ('two',2), ('one',3), ('four',4)]
for t in it:
    print 'name = %s age =%s ' %t
    
#-------------------------------------------
# 리스트메소드

s= [1,2,3] 
s.append(5)     # 맨 마지막에 5추가
print s
s.insert(3,4)   # 4번째 앞에 숫자 4 추가
print s
print s.index(3) # 값 3의 인덱스 반환
print s.count(2) # 값 2의 개수 반환

s.sort(), s.reverse() # timsort(변형된 merge sort)
print s

s=range(10,51,10)
print s
print s.remove(10)          # 왜 remove가 안되지?!
print s.extend([60,70])

# 스택, 큐
s = [10,20,30,40,50]
s.append(60)    # 마지막의 원소 값 넣기
print s.pop()  # 마지막 원소값 가져오기
print s
print s.pop(1) # 인덱스 1번값을 스택에서 빼옴
print s

# 실습
element =[]
for s in range(1,11):
    element.append(s)
print element
for i in range(1,5):
    print element.pop()
print element