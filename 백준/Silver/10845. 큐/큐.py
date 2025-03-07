import sys

a = int(sys.stdin.readline())
ampty_list = []
for i in range(a):
    b = sys.stdin.readline().split()
    comand_1 = b[0]
    if comand_1 == "push":
        ampty_list.append(b[1])
    elif comand_1 == "pop":
        if ampty_list:
            print(int(ampty_list.pop(0)))
        else:
            print(-1)
    elif comand_1 == "size":
        print(int(len(ampty_list)))
    elif comand_1 == "empty":
        if ampty_list:
            print(0)
        else:
            print(1)
    elif comand_1 == "front":
        if ampty_list:
            print(ampty_list[0])
        else:
            print(-1)
    elif comand_1 == "back":
        if ampty_list:
            print(ampty_list[-1])
        else:
            print(-1)