# def sieve_of_eratosthenes(M, N):
#     # N까지의 소수를 구하기 위해 크기 N+1 배열 생성
#     primes = [1] * (N + 1)  # prinmes = [0~N] 처음에는 0부터N까지 숫자가 모두 소수라고 가정 (1은 소수)

#     # 0과 1은 소수가 아니므로 0으로 설정
#     primes[0] = 0
#     primes[1] = 0

#     # 2부터 N까지 반복
#     for i in range(2, int(N ** 0.5) + 1):  # √N까지만 반복 그 이후 배수는 이전에 지워져서 제곱근까지만,
#         if primes[i] == 1:  # i가 소수일 때
#             for j in range(i * i, N + 1, i):  # i의 배수를 모두 0으로 설정
#                 primes[j] = 0
#             print(primes)

#     # M부터 N까지 소수 출력
#     for i in range(M, N + 1):
#         if primes[i] == 1:  # 소수는 1로 표시됨
#             print(i)

# # 입력 받기
# M, N = map(int, input().split())

# # 소수 구하기
# sieve_of_eratosthenes(M, N)
empty_number = []       # 9x9 행렬을 받을 빈 리스트 생성
greates_number = [0] * 3       # 최댓값, 최댓값의 행, 최댓값을 열  <- 이 3가지를 넣을 0으로 된 리스트 생성 = 최대값과 위치 초기화

for _ in range(9):      # 9열짜리가 총 9행이기 때문에 행 9번 반복
    empty_number.append(list(map(int, input().split())))       # 9열짜리 1개의 행가져옴 / 9번 반복

for index_row, item in enumerate(empty_number):     # 2차원으로 된 리스트에서 9열짜리 1개의 행리스트와 행 위치에 맞는 인덱스 가져옴
    # print(max(item), index_row+1, item.index(max(item))+1)    # 해당 행에서 가장큰값 / 행의 숫자 / 열의 숫자
    if (greates_number[0] < max(item)) or (greates_number[0] == max(item)):     # 행의 최대값과, 기존 최대값의 비교
        greates_number[0] = max(item)   # 최댓값 갱신
        greates_number[1] = index_row+1     # 최대값의 행 갱신
        greates_number[2] = item.index(max(item))+1     # 최댓값의 열 갱신
print(greates_number[0])
print(greates_number[1], greates_number[2])     # 출력