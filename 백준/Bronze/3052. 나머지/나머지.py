import sys

list_1 = []
for i in range(10):
    a = int(sys.stdin.readline())
    list_1.append(a%42)

b = len(list(set(list_1)))
print(b)