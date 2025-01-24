words = []      # 입력을 받을 리스트생성

for _ in range(5):      # 5개 입력 받아서 하나의 리스트에 각각 스트링으로 담아둠
    words.append(input())

result = ''     # 세로로 읽은것을 담을 객체생성

for i in range(15):     # 입력값 가로가 1~15개
    for j in range(5):      # 입력값은 무조건 5개(줄)이다
        if i < len(words[j]):   # words(최대 5개)에서 i번째 인덱스가 있는지 없는지 확인함 // 제일 중요함!!!
            result += words[j][i]
            # out of range가 일어날 수 없는 이유는 If 조건문에서 걸러진다.

print(result)
