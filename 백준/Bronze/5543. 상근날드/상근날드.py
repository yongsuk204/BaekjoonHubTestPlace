menu_price_list = []
drink_price_list = []
set_total_price_list = []

for i in range(3):
    menu_price_list.append(int(input()))

for i in range(2):
    drink_price_list.append(int(input()))

for i in menu_price_list:
    for f in drink_price_list:
        set_total_price_list.append(i+f-50)
print(min(set_total_price_list))