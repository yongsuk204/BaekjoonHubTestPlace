from collections import deque
import sys

a, b = map(int, sys.stdin.readline().split())

deque_1 = deque([i for i in range(1,a+1)])

total_list=[]

while deque_1:
    deque_1.rotate(-(b-1))
    total_list.append(deque_1.popleft())
print("<" + ", ".join(map(str, total_list)) + ">")  # 리스트를 요소사이에 ", "를 넣은 문자열로 변환 하고 양옆에 < 와 > 를 문자열로 더함