import math # math 라이브러리 사용

a = list(map(int, input().split())) # a, b 입력받기
b = list(map(int, input().split()))

# print(a ,b)

bunja = (a[0] * b[1]) + (a[1] * b[0])   # 분자
bunmo = a[1] * b[1] # 분모

gcd = math.gcd(bunja, bunmo)    # 분자와 분모의 최대공약수

print(bunja // gcd, bunmo // gcd)   # 분자와 분모에 최대공약수를 각각 나누면 기약분수가 나온다.