# -*- coding: utf-8 -*-
# ch05 파이썬 각종 연산자 ( 산술, 관계, 논리)

# 지수연산
print 2 ** 2 ** 3 # 왼쪽 <- 오른쪽 256
print 7/4
print -7/4
print -(7/4)
print
#관계 연산
print 6==9
print 6!=9
print 1>3
print 4<=5
print
print 'abcd' > 'abd'        # c가 d보다 앞서므로 C<D false
print (1,2,4) < (2,1,0)
print [1,3,2] == [1,2,3]
print
# 서로 다은 자료형 같의 크기 비교
#숫자 < 사전 < 리스트 < 문자열 < 튜플 

L = [ 1,2,3,'abc','a','z', (1,2,3), [1,2,3], {1:2}, ['abc']]
L.sort()
print L
print
# 객체 레퍼런스 비교
x=[1,2,3]
y=[1,2,3]
z=y

print x==y
print x==z
print x is y
print x is z
print y is z
print

# bool() 내장함수로 논리값
print bool(0)
print bool(1)
print bool(100)
print bool(0.0)
print bool(0.1)
print bool([])
print bool([0])
print bool({})
