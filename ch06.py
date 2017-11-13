# -*- coding: utf-8 -*-
#제어문과 함수 기초

sum =0
for x in range(1,11):
    sum = sum + x
print x

l = ['cat', 'dog', 'bird', 'pig']
for k, animal in enumerate(l):
    print k, animal
    
for x in range(10):
    if x <8:
        continue
    print x

for x in range(10):
    if x >3:
        break
    print x

for x in range(2,4):
    for y in range(2,10):
        print x, '*' ,y, '=', x*y
    print

a=0
while a<10:
    a = a+1
    sum = sum +a
print sum

x=0
while x < 10:
    print x,#콤마(,) 때문에 줄이 바뀌지 않는다. 
    x=x+1
else :  # while문에도 else를 쓸 수 있다.
    print 'else block'
print 'done'


# 함수 
def add(a,b):
    return a+b

f=add   # 함수도 객체 
print f(4,5)
print f
print f is add
print

def myobs(x):
    if x <0 :
        x = -x
    return x
def addobs(a,b):
    c = add(a,b)
    return myobs(c)
print addobs(-5,-7)


def calc(x,y):
    return x+y , x-y , x*y ,x/y 
print calc(3,4)     #튜플 타입으로 저장됨


# 재귀함수
def sum1(N):
    if N==1:
        return 1
    return N + sum1(N-1)
print sum1(10)