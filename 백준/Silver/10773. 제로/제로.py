total_list = []        # 합을 구할 빈 리스트
total_money_count = int(input())    # 몇개 주어지는지

for _ in range(total_money_count):    # 주어지는만큼 반복
    money_count = int(input())    # 여기부터 들어오는수가 주어지는수
    if money_count == 0:    # 0이면,
        total_list.pop()    # 선입후출 = 맨마지막에 들어간거 다시 빼냄
    else:
        total_list.append(money_count)    # 맨 마지막에 집어넣음

print(sum(total_list))    # 남아있는 요소의 합