a = int(input())

for _ in range(a):
    for i in input().split():
        print(f'{i[0]}{i[-1]}')