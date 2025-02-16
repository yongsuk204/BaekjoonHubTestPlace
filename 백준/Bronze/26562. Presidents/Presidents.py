name_price = {'Franklin':100, 'Grant':50, 'Jackson':20, 'Hamilton':10, 'Lincoln':5, 'Washington':1} # 가격표만들기
bill_time = int(input())    # 몇 번 지폐를 샐건지지

for _ in range(bill_time):
    total_price = 0 # 지폐의 초기값값
    for i in map(str, input().split()): # 대통령 성을 하나씩 가져옴옴
        # print(i)
        total_price += name_price[i]    # 대통령 성에 맞는 가격을 더함함
    print(f'${total_price}')