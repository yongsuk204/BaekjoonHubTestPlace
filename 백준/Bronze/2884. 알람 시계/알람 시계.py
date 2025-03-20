import sys

a, b = map(int, sys.stdin.readline().split())
minute = (b + 15 ) % 60  
# '분'은 60분 단위이기 때문에 -45분은 +15분과 같다. 이유는 원을 그려보면 뒤로 n 만큼가는 것은 앞으로 60-n 만큼
# 가는것과 같기 때문이다. 그리고 60분단위로 나눈후 나머지가 '분'이다.
# '시간'은 '분'이 45보다 작은경우 시간이 줄어들고 마찬가지로 -1시간은 +23시간과 같다. 24로 나누고 남은 나머지가 '시간이다'

if b < 45:
    hour = ( a + 23 ) % 24
else:
    hour = a

print(hour, minute)