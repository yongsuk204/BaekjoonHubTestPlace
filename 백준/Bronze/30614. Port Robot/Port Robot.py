a = int(input())  # 첫 번째 입력 (사용하지 않음)
log = input()  # 두 번째 입력 (로봇 동작 로그)

stack = []

for i in log:
    if i.islower():  # 소문자 → 컨테이너 저장 (push)
        stack.append(i)
    else:  # 대문자 → 컨테이너 꺼내기 (pop)
        if not stack or stack[-1].upper() != i:  # 스택이 비었거나, 맨 위와 짝이 안 맞으면 오류
            print(0)
            exit()
        stack.pop()  # 정상적으로 꺼냄

# 모든 동작이 끝난 후 스택이 비어 있어야 안정적
print(1 if not stack else 0)