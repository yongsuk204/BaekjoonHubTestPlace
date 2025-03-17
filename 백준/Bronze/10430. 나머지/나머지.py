import sys

A, B, C = map(int, sys.stdin.readline().split())

print(f'{(A+B)%C}\n{((A%C) + (B%C))%C}\n{(A*B)%C}\n{((A%C)*(B%C))%C}')