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