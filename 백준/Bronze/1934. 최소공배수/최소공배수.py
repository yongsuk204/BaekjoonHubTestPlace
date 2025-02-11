import math

def lcd(a,b):
    return a*b // math.gcd(a,b) # 최소공배수 = 두 수의 곱 / 최대공약수
for _ in range(int(input())):  # 테스트 케이스 개수만큼 반복
    a, b = map(int, input().split())    # 두 수 입력
    print(lcd(a, b))  # 최소공배수 출력