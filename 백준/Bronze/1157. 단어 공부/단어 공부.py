a = input().upper()
list = []
count_number = []
for i in a:
    if i not in list:
        list.append(i)
        count_text = a.count(i)
        count_number.append(count_text)

if count_number.count(max(count_number)) > 1:
    print("?")
else:
    print(list[count_number.index(max(count_number))])