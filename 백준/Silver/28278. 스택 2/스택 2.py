import sys
input_time = int(sys.stdin.readline())        # 함수의 갯수
reset_list = []    # 정수들어갈 빈리스트
    
for _ in range(input_time):     # 입력된 함수의 갯수만큼 반복
    a = sys.stdin.readline().split()    # 리스트로 가져옴
    if a[0] == '1':    
        reset_list.append(int(a[1]))    # 푸쉬다음 숫자를 정수로 받아서 리스트에 넣음
    elif a[0] == '5':
        if not reset_list:
            print(f'{-1}')    # 리스트에 정수가 없으면 -1 출력
        else:
            print(reset_list[-1])    # 정수가 있으면 가장 마지막에 들어간 숫자출력
    elif a[0] == '3':
            print(len(reset_list))    # 리스트의 길이
    elif a[0] == '4':
        if reset_list:        # 리스트가 비어있으면 False, 뭐라도 있으면 True
            print(f'{0}')        # 뭐라도 있으면 0 출력
        else:
            print(f'{1}')    # 비어있으면 1 출력
    elif a[0] == '2':
        if not reset_list:        # 리스트가 비어있으면 -1 출력
            print(f'{-1}')
        else:
            print(reset_list.pop())        # 비어있지않으면 마지막에 들어간 정수출력