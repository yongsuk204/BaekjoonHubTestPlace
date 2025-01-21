a, b = list(map(int, input().split()))

while True :
    if (a == 0) and (b == 0):
        break
    elif b % a == 0:
        print('factor')
    elif a % b ==0:
        print('multiple')
    else:
        print('neither')