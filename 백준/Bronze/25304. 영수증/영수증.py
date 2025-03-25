import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
price_number = 0
for i in range(b):
    f,g = map(int, sys.stdin.readline().split())
    price_number += f*g

if price_number == a:
    print("Yes")
else:
    print("No")