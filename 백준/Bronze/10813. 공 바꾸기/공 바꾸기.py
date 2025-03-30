import sys
a, b = map(int, sys.stdin.readline().split())
# print(a,b)
first_list = [i for i in range(1,a+1)]
# print(first_list)
for h in range(b):
    c, d = map(int, sys.stdin.readline().split())
    # print(c,d)
    first_list[c-1], first_list[d-1] = first_list[d-1], first_list[c-1]

print(" ".join(map(str,first_list)))