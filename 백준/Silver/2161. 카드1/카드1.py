import sys
ampty_list = []
a = int(sys.stdin.readline())
for i in range(a):
    ampty_list.append(i+1)

while ampty_list:
    print(ampty_list.pop(0))
    if ampty_list:
        ampty_list.append(ampty_list.pop(0))