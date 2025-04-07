total_list = [[0] * 100 for i in range(100)]

what_time = int(input())
for i in range(what_time):
    a, b = map(int, input().split())
    for j in range(a-1, a+9):
        for k in range(b-1, b+9):
            total_list[j][k] = 1

print(sum(map(sum,total_list)))
    