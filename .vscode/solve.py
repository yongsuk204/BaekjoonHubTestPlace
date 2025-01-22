a,b = list(map(int, input().split()))       # 행과 열의 갯수를 받음

arr_1 = []      # 2차원 행렬을 리스트화해서 담을곳
arr_2 = []      # 2차원 행렬을 리스트화해서 담을곳

for _ in range(a):  # 총 a행xb열짜리 행렬
    arr_1.append(list(map(int, input().split())))       # 2차원 리스트화 한거 1개
        # [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
for _ in range(a):
    arr_2.append(list(map(int, input().split())))       # 2차원 리스트화 한거 1개(총2개)
        # [[3, 3, 3], [4, 4, 4], [5, 5, 100]]

for i in range(a):      # 2차원 시킨 리스트화끼리 각각 a개의 행에서[0~2]
    for j in range(b):  # 위에서 반복된 i[0,1,2]행에서 b열끼리[0~2] 더한다
        f = arr_1[i][j] + arr_2[i][j]
        print(f, end=' ')       # 더해진 3개의 열(4,4,4)은 여기서 마치고 줄바꿈대신 공백한칸포함해서 출력을 마침
    print()     # i 반복문(상위반복문)에 해당되어 하위반복문이 끝나면 실행됨 즉, 하위반복문이 끝나면 줄바꿈을 하겠다는 의미
