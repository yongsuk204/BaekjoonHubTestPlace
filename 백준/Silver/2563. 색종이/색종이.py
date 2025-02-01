total_place = []    # 전체 도화지의 크기
total_number = 0    # 색종이의 면적
a = int(input())    # 색송이 갯수
for i in range(100):    # 전체 도화지 만들기
    total_one_row = [0] * 100    # 0이 100개인 행 1개를 만듬 => 이부분이 반복문 밖에있으면 전역변수라서 모든행이 같거로 인식해서 수정도 전체 다이루어 지기때문에, 반복문 안에두어서 서로 각각다른 행을 만듦으로 영향을 주지않게함
    total_place.append(total_one_row)    # 만든 행1개를 도화지에 차곡차곡 넣음
for _ in range(a):    # 색종이 붙이는 작업 a개 만큼
    b,c = map(int, input().split()) # 꼭짓점이 b,c인 색종이
    # print(b,c)
    for h in range(10):    # 색종이 행의 길이 = 10
        for f in range(10):    # 색종이 열의 길이 = 10
            total_place[c+h-1][b-1+f] = 1    # 색종이의 면적을 0에서 1로 채움
for q in total_place:
    total_number += sum(q)    # 전체 도화지 0 에서 색종이가 붙은 1을 모두 더함, 곂친부분은 2가아니라 1이기 때문에 반영되었다고 볼 수 있음
print(total_number)