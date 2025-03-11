from collections import deque
import sys

a, b = map(int, sys.stdin.readline().split())
list_1 = deque([i for i in range(1, a+1)])
ampty_list = []

while list_1:
    list_1.rotate(-(b-1))
    ampty_list.append(list_1.popleft())
# print(ampty_list)
print("<"+", ".join(map(str, ampty_list))+">")