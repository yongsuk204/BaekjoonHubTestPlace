def fibonacci(n, b=None):
    if b is None :
        b = [-1] * (n+1) # 임시 저장공간을 만듬, +1하는 이유는 인덱스가 0부터 시작하기 때문
    
    if n <= 1:
        return n
    
    if b[n] != -1 :    # 임시저장공간에 -1이 아닌 수가 있으면 그 수를 바로 쓰도록함
        return b[n]
    b[n] = fibonacci(n-1, b) + fibonacci(n-2, b)  # b[n]에 있는 숫자가 만들어진 과정
    return b[n]                                   # 그 과정을 b[n]에 저장함


import sys
from collections import deque
a = int(sys.stdin.readline())
list = []
for i in range(3, a + 1):        # 인덱스 3부터 시작하는이유는 0,1 일때는 안쓰는 거로해서
    list.append(fibonacci(i))
print(f'{fibonacci(a)} {len(list)}')