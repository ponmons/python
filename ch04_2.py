# -*- coding: utf-8 -*-
l1 = [4,5]
l1[1]=10
print l1

# 내장자료형
# 수치형, 문자열, 리스트, 튜플, 사전
# 표를 암기해야함

print type(None) # 아무것도 없다. null..?
print """
ㅁ아아아앙아아ㅏ아아
아아아아아
"""

a= 500
b =a 
print id(a)  # 식별자... 같을까?
print id(b) # 같다..

print type(l1) == type(a)

# is 키워드 : 두객체의 식별자가 동일한지 boolean
c=[1,2,3]
d=[1,2,3]
print id(c), id(d);
print c is d

# == 키워드 : 두 객체의 내용값을 비교한다.

