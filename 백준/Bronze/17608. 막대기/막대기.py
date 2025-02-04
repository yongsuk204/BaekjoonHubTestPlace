import sys

a = int(sys.stdin.readline())
empty_list = []

for _ in range(a):
    b = int(sys.stdin.readline())
    empty_list.append(b)
# print(empty_list)
count = 0
max_num = empty_list[-1]

for i in empty_list[::-1]:
    if i > max_num:
        count +=1
        max_num = i
print(count+1)