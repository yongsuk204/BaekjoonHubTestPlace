what_time = int(input())
total_price = int(input())

for _ in range(what_time-1):
    total_price += int(input())
print(total_price)