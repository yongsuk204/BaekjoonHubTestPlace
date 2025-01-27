while True:
    i = input()  # 한 줄씩 입력받음
    if i == '0':  # 입력이 0이면 종료
        break
    if i == i[::-1]:  # 문자열이 거꾸로 해도 동일하면 팰린드롬
        print('yes')
    else:
        print('no')