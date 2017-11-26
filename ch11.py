# -*- coding: utf-8 -*-
# ch11 튜플과 집합

# 튜플 활용법(패킹,언패킹), 집합자료형
t3 = 1,2,3
print type(t3), type(t3[1])

t = 1234, 5432,'hello'
u = t, 1,2,3,4,5
print u

x,y,z = 1,2,3  # 튜플을 이용한 복수개의 변수에 대입
print x,y,z 

#패킹
t=1,2, 'hello'   # <- 한개의 변수에 3개 값을 묶는 것.
x,y,z = t        # <- 묶여 있는 객체를 푸는것.

# 변환함수
T = 1,2,3,4,5
L = list(T)
print L
T = tuple(L)
print T

# 사용 용도( 함수가 하나 이상의 값을 리턴, 문자열 포맷팅, 사전)
def calc(a,b):
    return a+b, a*b; # 튜플로 패킹

x, y=calc(5,4) # 리턴값으로 언패킹 
print x, y

c = "id : %s name : %s" % ('eid', 'hahahah')

# 고정된 값을 쌍으로 표현
d= {'one' :1 , 'two':2}
print d.items()  # 튜플로 묶어 주네..

#=========================================================
#집합 자료형 SET 
c = set({'a':1, 'b':2, 'c':3})
print c     # 키값만 들어감
c2 = set({'a':1, 'b':2, 'c':3}.values())
print c2    # 값만 보여줌.

print set('abc') # 정렬이 없음..

B=set([4,5,6,10,20,30])
C=set([10,20,30])

print C.issubset(B)
print C <= B
print C.issuperset(B)
print B >= C

print B.union(C)  # 합집합
print B | C
print B.intersection(C) # 교집합
print B & C
print B.difference(C) # 차집합
print B - C 
print B.symmetric_difference(C) # 배타집합
print B ^ C
print
# a b 자료형 메소드
A= set([1,2,3,4])
B=set([3,4,5,6])

A.update(B) # |=
print A
A.intersection_update([4,5,6,7]) #&=
print A
A.difference_update([6,7,8]) # -=
print A
A.symmetric_difference_update([5,6,7]) # ^=
print A
A.add(8) 
print A
A.remove(8)
print A
A.pop()# 임의의 원소 빼기
print A
A.clear()
print A
print

#실습
t1=[1,2,3,4,5]
t2=[3,4,5,6,7]
t3=list(set(t1+t2))
print t3

