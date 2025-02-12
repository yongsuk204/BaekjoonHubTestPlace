import math # 최대공약수를 구하기위해 math 모듈 사용
a = int(input())    # 몇 개 최대공약수 구할건지 입력받기

for i in range(a):  # a개 만큼 반복
    empty_list = [] # 빈 리스트 생성
    for f in map(int, input().split()): # 입력받은 숫자들을 리스트에 넣기
        empty_list.append(f)    # 리스트에 넣어서 최대공약수 구할 준비
    # print(empty_list)
    gcd_sum_value = 0   # 최대공약수의 합을 구할 변수 생성 / 하위 for문에서 최대공약수를 더하고 초기화하기위해
    for i in range(1,empty_list[0]+1):  # 리스트첫번째는 최대공약수를 구할 숫자의 갯수이기때문에 1부터 시작, 두번째 숫자부터 마지막 숫자까지 인덱스추출
        for j in range(i+1, empty_list[0]+1):   # 리스트의 두번째부터 비교할 숫자까지 인덱스추출 / (1,2), (1,3), (1,4), (2,3), (2,4), (3,4) 이런식으로 비교하기위해
            gcd_value = math.gcd(empty_list[i], empty_list[j])  # 인덱스에 맞춰서 최대공약수 구하기
            gcd_sum_value += gcd_value  # 최대공약수의 합을 구하기위해 더하기
    print(gcd_sum_value)    # 최대공약수의 합 출력