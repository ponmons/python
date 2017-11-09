# -*- coding: utf-8 -*-
import keyword # 모듈 (파이썬 예약어 목록)

print keyword.kwlist
print
print len(keyword.kwlist)

print min(1,2)
print min([1,2,3])
print pow(2,-1) #2의 -1승
print pow(3,3) # 3의 3승
print 
print chr(97)
print chr(65)
print chr(48)
print
print str('한글도되나')
print range(10)
print range(3,11)
print range(3,10,2)     # start , stop , step 3,5,7,9
print
print type(-1)
print type('abc')  
print type([1,2,3])     # 임의의 객체 object의 자료형을 반환

_2a=10           # 동적 변수에 값을 할당.. 타입 선언이 없네.
_A=20
print _2a,_A

b=2
print b 
del b
#print b

## 3. 파이썬 기초 문형
a=1
b=3
if(a==1) and \
(b==3) :      # \ 하나의 줄로 이어주는 역할.
    print 'connected lined'

# 확장 할당문
a=1
a +=4
print a

# 콘솔 입력
r = int(raw_input('int r : '))
print r
# 콘솔 출력 
print 1; print 2 , r*2*3.14

result= range(2, 99, 2)
print result
