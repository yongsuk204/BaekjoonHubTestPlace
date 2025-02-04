import sys        # 빠른입력을위한 가져오기

a = int(sys.stdin.readline())    # 받아올 숫자갯수
empty_list = []    # 숫자를 받을 빈 리스트 생성

for _ in range(a):    # 받아올 숫자만큼 반복함
    b = int(sys.stdin.readline())    # 막대기 받아옴
    empty_list.append(b)    # 받아온막대기 왼쪽부터 채워넣음
# print(empty_list)
count = 1
max_num = empty_list[-1]    # 오른쪽 첫번째 막대기가 가장 크다고 가정하고 시작 = 오른쪽 첫번째 막대기 1개는 무조건 보인다

for i in empty_list[::-1]:    # 왼쪽부터 채워넣어진 막대기를 오른쪽부터 순서대로 꺼내옴
    if i > max_num:    # 오른쪽 순서대로 가져로는 막대기가 가장큰 막대기 보다크면
        count +=1        # 보이는 막대기라서 카운팅
        max_num = i    # 가장큰 막대기 새로갱신
print(count)
