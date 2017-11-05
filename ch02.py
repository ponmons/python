# -*- coding: utf-8 -*-
import keyword

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

_a=10           # 동적 변수에 값을 할당.. 타입 선언이 없네.
_A=20
print _a,_A

b=2
print b 
del b
#print b

## 3. 파이썬 기초 문형
a=1
b=3
if(a==1) and \
(b==3) :
    print 'connected lined'

