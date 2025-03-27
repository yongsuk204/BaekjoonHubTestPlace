import sys

nomal_list = [1,1,2,2,2,8]
adjust_list = list(map(int, sys.stdin.readline().split()))
need_list = []

for idx, i in enumerate(adjust_list):
    need_list.append(nomal_list[idx] - i)

print(" ".join(map(str, need_list)))