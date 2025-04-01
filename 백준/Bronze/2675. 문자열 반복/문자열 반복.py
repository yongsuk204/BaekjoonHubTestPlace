a = int(input())

for i in range(a):
    string_1 = ""
    q,w = map(str, input().split())
    q = int(q)
    for z in w:
        string_1 += z*q
    print(string_1)