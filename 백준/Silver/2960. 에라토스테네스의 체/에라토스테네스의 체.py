a,b = map(int, input().split())
count = 0
empty_list = [True] * (a+1)     # 0~입력숫자까지 리스트 만듬, 0과1은 소수가아님

# print(empty_list)
for i in range(2, a+1):     # 2~10까지 반복
    # print(i)
    if empty_list[i]:   # 해당숫자가 소수라면
        for f in range(i,a+1,i):    # 소수인 숫자부터 입력숫자까지 소수의배수들
            if empty_list[f]:   
                # 소수인 숫자 포함 소수의 배수들이 있다면 / f -> i 로해서 실수했었는데, empty_list[i]로 고정되어버리기 때문에 
                # 소수의 배수들이 지워지지 않고 하위반복문이 끝나서 상위반복문으로 들어감, 즉 empty_list[i]는 계속True로 판정하게됨
                # print(f)
                empty_list[f] = False   # 그것들 다 제외
                count += 1      # 제외할때마다 카운트
                # print(count)
                # print('----')
                if count == b:  # 원하는 지우는 횟수일때 해당숫자 출력
                    print(f)
