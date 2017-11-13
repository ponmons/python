# -*- coding: utf-8 -*-
#ch04 리스트, 튜플, 사전

L = [1,2,3]
print type(L)
print len(L)
print L[1]
print L[0]
print L[-1]
print L[1:3]
print L+L
print L*3

# range() 함수를 통한 인덱스 리스트 생성
L= range(10)
print  L
print L[::2]
print L[::-1]

# 튜플 : 리스트와 유사하지만 튜플 내의 값을 변경할 수없음.
month = ('Jan', 'Feb', 'Mar');
#month[1] = '야';


# 사전 - 초기화후 값 변경 가능, 순서 없음. 
d={'one' : 'hana', 'two':'dul', 'three':'set'}
d['four'] = 'net'
print d
print d.keys(), d.values(), d.items() # 리스트 형식



# 2. 내장자료형
