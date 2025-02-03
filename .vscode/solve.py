total_list = []
total_money_count = int(input())

for _ in range(total_money_count):
    money_count = int(input())
    if money_count == 0:
        total_list.pop()
    else:
        total_list.append(money_count)

print(sum(total_list))