import sys

a = int(sys.stdin.readline())

score_list = list(map(int, sys.stdin.readline().split()))

c = int(sys.stdin.readline())

print(score_list.count(c))