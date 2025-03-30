import sys

a, b = map(int, sys.stdin.readline().split())

first_list = list(map(int, sys.stdin.readline().split()))

print(" ".join(map(str,list(filter(lambda x:x<b, first_list)))))