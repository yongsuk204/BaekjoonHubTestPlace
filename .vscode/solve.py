import sys
a = int(sys.stdin.readline())

ampty_list = [i for i in range(1, a+1)]
# for i in range(a):
#     ampty_list.append(i+1)

while ampty_list:
    print(ampty_list.pop(0))
    if ampty_list:
        ampty_list.append(ampty_list.pop(0))