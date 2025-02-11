import math

def gcd_lcd(a, b):  # 최대공약수 * 최소공배수 = a * b
    gcd = math.gcd(a, b)    # 최대공약수
    lcd = a * b // gcd  # 최소공배수
    return print(gcd), print(lcd)   # 최대공약수와 최소공배수 출력

a, b = map(int, input().split())
gcd_lcd(a, b)