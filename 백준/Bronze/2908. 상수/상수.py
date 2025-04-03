list_1= list(map(str, input().split()))

for idx, i in enumerate(list_1):
    list_1[idx] = int(i[::-1])
print(max(list_1))