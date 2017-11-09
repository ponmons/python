# -*- coding: utf-8 -*-
# 과제1 
#사용자로부터 원의 지름을 입력받아 원의 둘레 및 넓이를 구하는 프로그램을 작성하라. 
# 원의 둥레는 2*파이*반지름, 넓이는 파이*반지름*반지름이다. (파이는 3.14이다)

pi = 3.14
r = int(raw_input('int r : '))
#if(type(r) == 'int' and r > 0) 
print '원의 둘레는 '
print  2*pi*r
print
print '넓이는 ' , pi*r*r   # , 는 한칸 띄워줄 수 있음.


#else print '잘못된 값입니다.(int만 가능)'