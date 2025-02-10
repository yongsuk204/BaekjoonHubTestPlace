a = int(input())


for _ in range(a): # 입력받은 a만큼 반복
    list = []       # 빈 리스트 생성 / 리스트 안에 집합을 넣어서 교집합을 구할 것이다.
    for i in map(int, input().split()): # 입력받은 숫자를 공백을 기준으로 리스트로 만들어서 i에 넣는다. / 54, 24 순서대로 
        empty = set()   # 빈 집합 생성
        for f in range(1,int(i**0.5)+1):    # 1부터 i의 제곱근까지 반복 / 제곱근까지 반복하는 이유는 제곱근 이후로는 중복되기 때문에
            # print(f)
            if i % f == 0:
                # print(f)
                # print(i//f)
                empty.add(f)    # 제곱근 이하의 약수를 집합에 추가, 집합은 중복을 허용하지 않기 때문에 중복되지 않는다.
                empty.add(i//f) # 제곱근 이상의 약수를 집합에 추가, 집합은 중복을 허용하지 않기 때문에 중복되지 않는다.
        list.append(empty) # 리스트에 집합을 추가한다.
    # print(type(list[0]))
    # print(list)

    b = list[0].intersection(list[1])   # 교집합을 구한다.
    print(max(b))   # 교집합 중 가장 큰 값을 출력한다.

# import math

# a, b = map(int, input().split())
# print(math.gcd(a, b))  # 최대공약수 출력