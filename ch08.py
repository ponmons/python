# -*- coding: utf-8 -*-
# ch08 문자열 메소드
s= 'i like programming'
print s.upper() ,s.lower(), s.swapcase(), s.capitalize();
print s.title() # 각 단어의 첫글자는 대문자.

print s.count('like')
print s.find('like', 2)
print s.startswith('i like') # 대소문자 정확히 반영
print s.endswith('swimming'), s.endswith('progr')

print s.strip() #좌우 공백 제거
print s.rstrip() , s.lstrip() # 오, 왼 제거..
print s.strip('i')
print s.split() # 리스트로 띄어쓰기 기준으로 분리
print s.split('like')

t= s.split()
print t
t2 = ':'.join(t)
print t2 , type(t2)
t3 = ','.join(t)
print t3


u2 = u"스팸 햄 계란 치즈"
t2 = u2.split()
print t2
print t2[0], t2[1], t2[2], t2[3]

lines = ''' first line
second line
third line '''
print lines.split()
print lines.splitlines() # 한줄씩 자름


# 정렬 
print
c = s.center(60, '-')
print type(c)
print c
print s.ljust(60, '-')
print s.rjust(60, '-')

#------------------------------
# 문자열 포맷팅 (튜플, 사전)
print 'name = %s, age =%s' % ( 'csj', '345')

letter = ''' 
안녕하세요 %s님
오늘 밤 배그로 불태워 보실래요? 
컴온 '''
name = '이사'
print letter % name
print 
names = ['한', '이', '삼']
for name in names:
    print letter % name
    print '-' * 40
    print

# %r, %c, %d, %f
print "%s -- %s -- %d -- %5.2f -- %e" % ((1,2), [3,4,5], 5, 5.345 , 101.3)
print letter % repr(1)

# %d %o %x 10, 8, 16진수
# 사전을 활용한 것
print '%(이름)s -- %(전화번호)s' % {'이름': '홍길동' , '전화번호' : '5293'}

# 실습
s= " 1, 2   , 3,   4,  5  "
l=s.split(',')
i=0
while i < len(l) :
    l[i] = l[i].strip()
    i = i+1
print l

# 정답이라는데... 하.. 이상한데?
s = "1, 2   , 3,   4,  5  "
parts = s.split(",")
l = []
for i in range(len(parts)):
    parts[i] = parts[i].strip()
    l.append(parts[i])
print l

# isdigit() : 문자열 내 character가 모두 숫자인가?
#isalpha() : 문자열 내 character가 모두 영문자인가?
#isalnum() : 문자열 내 character가 모두 영문자 또는 숫자인가?
#islower() : 소문자?
#isupper() : 대문자? 
#isspace() : 문자열 내 character이 모두 공백문자인가?istitle() : 문자열이 title 형식(각 단어의 첫글자가 대문자) 인가?s.zfill(5) : 5글자 자리 확보 후 문자열 쓰고, 남은 공백에 0 채움

