count = 0
a, b = map(int, input().split())
while True:
    if a == b:
        break
    count += 1
    a,b =  max(a,b) - min(a,b), min(a,b)
print(count)