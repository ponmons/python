# -*- coding: utf-8 -*-
# 파이썬 장점:직관적인 문법구조, 빠른 개발속도, 우수한 자료형(내장)
# 목표 : 수치 자료형, 문자열

# 정수형 상수 10진, 8진, 16진
a=23 ; b=023; c=0x23;
print a,b,c

import sys
print sys.maxint    # 메모리 자리수 최대값

# 실수형 
a=1.2; b=3.5e3 ; c=-0.2e-4; 
print a,b,c

# 복소수형
a=10 + 20j
print a
b=10 + 5j
print a+b 

# 수치 연산과 내장함수
print complex(3.2, 5) ; print complex(6);
print divmod(5,2), pow(2,3), pow(2.3,4.5)  # 몫/나머지 , 제곱승

# 수학연산시 필요 모
import math
print math.pi
print math.e
print math.sin(1.0)
print math.sqrt(2)  # 2의 제곱근

# 문자열 인덱싱과 슬라이싱
s="Hello World!"
print s[1] ,s[2] , s[-1], s[-2] # 인덱싱..
print s[1:3], s[0:5]    # 자르기
print s[1:], s[:3]      # 인덱스1부터 뒤에 문자출력
print s[::2] , s[::-1]  # 인덱스 2칸씩 건너뛰어서. -1은 뒤에서 부터

# 문자열을 바꾸려면 슬라이싱을 사용해야 한다.
# 문자열 연결/ 반복 (+, *)
# 문자열 길이
print len("hello world") 

# 문자열 내 포함관계 여부
s="world"
print "world" in s
print "World" in s
print "World" not in s