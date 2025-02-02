import sys

def sieve_of_eratosthenes(M, N):
    is_prime = [True] * (N + 1)  # M~N 까지의 숫자가 모두 소수라고 가정
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(N**0.5) + 1):  # 2부터 N의 제곱근 까지만 검사, 그 이후는 배수처리에 의해서 사라짐
        if is_prime[i]:  # i가 소수라면, 인덱스 번호와 실제 숫자는 일치함
            for j in range(i * i, N + 1, i):  # i의 배수들을 False로 마킹
                # i*i 이전의 숫자는 이미 False 처리가 되었음
                is_prime[j] = False     # 여기까지는 0부터 N까지 숫자중에 소수만 True로 바뀜

    # M 이상 N 이하의 소수만 출력
    for num in range(M, N + 1):
        if is_prime[num]:       # 인덱스의 위치와 실제 번호의 위치는 동일함함
            print(num)

# 입력 받기
M, N = map(int, sys.stdin.readline().split())
sieve_of_eratosthenes(M, N)
