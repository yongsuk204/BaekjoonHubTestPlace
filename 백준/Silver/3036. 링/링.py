import math # math.gcd 사용을 위한 import

a = int(input())    # 원의 갯수

circle_list = list(map(int, input().split()))   # 원의 반지름 리스트
# print(circle_list)
for i in range(a-(a-1)):    # 0부터 a-1까지 반복 = 첫번째 원에 대해서만 계산하는 의미 / range(a)로 하면 모든 원에 대해 회전비율 계산
    for j in range(i+1, a): # 기준원에 대해서 다음 원부터 마지막 원까지 반복
        # print(i, j)
        gcd_bunsu = math.gcd(circle_list[i], circle_list[j])    # 두개 원의 반지름의 최대공약수를 구해서 나누기 위한 분모로 사용
        print(f'{int(circle_list[i]/gcd_bunsu)}/{int(circle_list[j]/gcd_bunsu)}')   # 기약분수형태로 출력