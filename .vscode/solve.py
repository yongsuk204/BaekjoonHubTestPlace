def sieve_of_eratosthenes(M, N):
    # N까지의 소수를 구하기 위해 크기 N+1 배열 생성
    primes = [1] * (N + 1)  # prinmes = [0~N] 처음에는 0부터N까지 숫자가 모두 소수라고 가정 (1은 소수)

    # 0과 1은 소수가 아니므로 0으로 설정
    primes[0] = 0
    primes[1] = 0

    # 2부터 N까지 반복
    for i in range(2, int(N ** 0.5) + 1):  # √N까지만 반복 그 이후 배수는 이전에 지워져서 제곱근까지만,
        if primes[i] == 1:  # i가 소수일 때
            for j in range(i * i, N + 1, i):  # i의 배수를 모두 0으로 설정
                primes[j] = 0
            print(primes)

    # M부터 N까지 소수 출력
    for i in range(M, N + 1):
        if primes[i] == 1:  # 소수는 1로 표시됨
            print(i)

# 입력 받기
M, N = map(int, input().split())

# 소수 구하기
sieve_of_eratosthenes(M, N)