# [Bronze III] 최댓값 - 2562 

[문제 링크](https://www.acmicpc.net/problem/2562) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현

### 제출 일자

2025년 1월 21일 21:39:39

### 문제 설명

<p>9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.</p>

<p>예를 들어, 서로 다른 9개의 자연수</p>

<p>3, 29, 38, 12, 57, 74, 40, 85, 61</p>

<p>이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.</p>

### 입력 

 <p>첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.</p>

### 출력 

 <p>첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.</p>

 ### 제출 

<p>total_list = []        # 새로운 리스트 만듬

    for _ in range(9):      # 9번 반복문 두드림
        i = int(input())    # 두드려질때마다 인풋값 가져옴(순서대로)
        total_list.append(i)    # 인풋값가져온거 리스트에 넣음
        max_value = max(total_list)     # 리스트중의 최대값
        max_idx = total_list.index(max_value)+1     # 최대값의 인덱스위치
    print(int(max_value))       # 문자열을 정수화시킴
    print(max_idx)

오답풀이 1
    total_list = []        

    for _ in range(9):      
        i = input().split()    # .split()은 list를 반환함, 그리고 input()는 str을 반환하기때문에 결과적으로 i = [str,str,str,str,str] 인셈이다.
        total_list += i     # total_list에 넣으려면 i 가 리스트인경우는 이게 가능하지만(리스트+리스트), i가 int라면 리스트+정수 가 안되기때문에 .append()를 써야 리스트안에 정수가 들어감.
        max_value = max(total_list)     
        max_idx = total_list.index(max_value)+1     
        print(int(max_value))       # 이렇게 하면 마지막 값만 정수로 바뀜 즉, 반복문 모든 입력값에 대해서 int가 아님 이부분 주의 해야함
        print(max_idx)

오답풀이 2
total_list = []       

for _ in range(9):      
    i = input().split()
    total_list += i

print(max(total_list))    
print(total_list.index('85')+1)         # 현재는 리스트에 '85' 가들어가있는게 맞지만, i 가 정수로 바뀌면 85 가 들어가야함