total_price = int(input())
book_price = 0
for _ in range(9):
    book_price += int(input())
print(total_price - book_price)