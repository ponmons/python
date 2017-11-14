# -*- coding: utf-8 -*-
# ch07 문자열과 포맷팅

# 1. 시퀀스 자료형 - 문자열, 리스트, 튜플
# 인덱싱, 슬라이싱, 확장 슬라이싱, 연결, 반복, 길이정보, 멤버쉽테스트

s= 'abcdf'
l = [100, 200, 300]
print s[0]
print s[1]
l[1] = 900
print l;

print s[1:3] # 마지막 3은 포함되지 않는다. 1,2
print s[1:]
print s[:]
print s[-100:100];

print s[::2] # 인덱스 2개 건너뛰어서
print s[::-1] # 거꾸로.

t=(1,2,3,4,5)
print 2 in t
print 10 in t

print 'ab' in 'abcd'

# in에는 컨테이너 자료형이 가능하다.
for c in 'abcd' : # 시퀀스 자료형이 아닌 것 :사전
    print c, '\n'


print '\\abc\tdef\nghi'
s = 'spam and egg'
s= s[:4] + ', chessze ' +s[9:]
print s

# 유니코드
c = u'가나다라'
print type(c)
d = unicode('한글', 'utf-8')
print d
print '한글'

print len('한글') # 제대로 숫자를 못 세네...
print len(u'한글') # u를 꼭 써줘야함.

# 실습
s= 'a,b,d,e'
s= s[:3] +',c' +s[3:]
print s, len(s)
