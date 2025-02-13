import math
number = 0
for i in map(int, input().split()):
    a = i**2
    number += a
number = number % 10
print(number)