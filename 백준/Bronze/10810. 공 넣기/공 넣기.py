import sys

a,b = map(int, sys.stdin.readline().split())

basket_list = [0] * a

for _ in range(b):
    i,k,j = map(int, sys.stdin.readline().split())
    basket_list_1 = [j]*a
    basket_list[i-1:k] = basket_list_1[i-1:k]

print(" ".join(map(str, basket_list)))