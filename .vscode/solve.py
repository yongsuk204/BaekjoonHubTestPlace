empty_list = []
for _ in range(5):
    a = int(input())
    if a < 40 :
        a = 40
        empty_list.append(a)
    else:
        empty_list.append(a)
print(int(sum(empty_list)/5))