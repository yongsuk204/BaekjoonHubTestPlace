import sys
from collections import deque

input_time = int(sys.stdin.readline())

list_1 = deque()

def push(x):
    list_1.append(x)
def pop():
    if not list_1:
        return -1
    else:
        return list_1.popleft()
def size():
    return len(list_1)
def empty():
    if not list_1:
        return 1
    else:
        return 0
def front():
    if not list_1:
        return -1
    else:
        return list_1[0]
def back():
    if not list_1:
        return -1
    else:
        return list_1[-1]
    
for i in range(input_time):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())
    else:
        break