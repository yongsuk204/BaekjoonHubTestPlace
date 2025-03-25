import sys

list_1 = [-1] * 30
list_2 = []
for i in range(28):
    idx_number = int(sys.stdin.readline())
    list_1[idx_number-1] = idx_number

for idx, i in enumerate(list_1):
    if i == -1:
        list_2.append(idx+1)

print(list_2[0])
print(list_2[1])