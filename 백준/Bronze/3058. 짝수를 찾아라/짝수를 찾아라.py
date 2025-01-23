a = int(input())

for i in range(a):
    i_list = []
    for j in map(int, input().split()):
        if j % 2 ==0:
            i_list.append(j)
    print(sum(i_list), end=' ')
    print(min(i_list))